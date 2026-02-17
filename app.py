with open("data.xlsx", "rb") as f:
    file_bytes = f.read()

import io
import re
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Spreadsheet Lookup", layout="wide")

st.title("Spreadsheet Lookup App")
st.caption("Search and filter the spreadsheet, then export results.")

@st.cache_data(show_spinner=False)
def load_xlsx(file_bytes: bytes, sheet_name=None) -> pd.DataFrame:
    xls = pd.ExcelFile(io.BytesIO(file_bytes))
    use_sheet = sheet_name or xls.sheet_names[0]
    df = pd.read_excel(xls, sheet_name=use_sheet)
    return df

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    # Normalize column names
    df = df.copy()
    df.columns = [re.sub(r"\s+", " ", str(c)).strip() for c in df.columns]
    # Trim string columns
    for c in df.columns:
        if df[c].dtype == object:
            df[c] = df[c].astype(str).replace("nan", "").str.strip()
            df.loc[df[c] == "", c] = pd.NA
    # Standardize "Case Quantity" if present
    for cand in ["Case Quantity", "Case Quantity "]:
        if cand in df.columns:
            df.rename(columns={cand: "Case Quantity"}, inplace=True)
    if "Case Quantity" in df.columns:
        df["Case Quantity"] = pd.to_numeric(df["Case Quantity"], errors="coerce")
    return df

import os

DEFAULT_FILE = "data.xlsx"  # put this file in the same folder as app.py

file_bytes = None

# 1) Auto-load fixed file if present
if os.path.exists(DEFAULT_FILE):
    with open(DEFAULT_FILE, "rb") as f:
        file_bytes = f.read()

# 2) Otherwise fall back to uploader
with st.sidebar:
    st.header("Data source")
    if file_bytes is None:
        uploaded = st.file_uploader("Upload an .xlsx file", type=["xlsx"])
        if uploaded is not None:
            file_bytes = uploaded.getvalue()
    else:
        st.success(f"Loaded default file: {DEFAULT_FILE}")

if file_bytes is None:
    st.info("Upload an .xlsx file to get started.")
    st.stop()

df_raw = load_xlsx(file_bytes)
df = clean_df(df_raw)

# Basic schema-aware helpers (works even if columns differ)
all_cols = list(df.columns)

left, right = st.columns([2, 1])

with left:
    st.subheader("Search")
    q = st.text_input("Search across all columns", value="")
    st.caption("Example: 'F15T5BL', 'Gardner', 'Genus', 'shatterproof'")

with right:
    st.subheader("Display")
    shown_cols = st.multiselect("Columns to display", options=all_cols, default=all_cols)
    st.caption("Hide columns to simplify the results view.")

filtered = df

# Optional common filters if these columns exist
with st.expander("Filters", expanded=True):
    cols = st.columns(4)

    if "Brand" in filtered.columns:
        brand_sel = cols[0].multiselect(
            "Brand",
            options=sorted(filtered["Brand"].dropna().unique())
        )
        if brand_sel:
            filtered = filtered[filtered["Brand"].isin(brand_sel)]

    if "Model" in filtered.columns:
        model_sel = cols[1].multiselect(
            "Model",
            options=sorted(filtered["Model"].dropna().unique())
        )
        if model_sel:
            filtered = filtered[filtered["Model"].isin(model_sel)]

    if "Lamp Type" in filtered.columns:
        type_sel = cols[2].multiselect(
            "Lamp Type",
            options=sorted(filtered["Lamp Type"].dropna().unique())
        )
        if type_sel:
            filtered = filtered[filtered["Lamp Type"].isin(type_sel)]

    if "Lamp Code" in filtered.columns:
        code_sel = cols[3].multiselect(
            "Lamp Code",
            options=sorted(filtered["Lamp Code"].dropna().unique())
        )
        if code_sel:
            filtered = filtered[filtered["Lamp Code"].isin(code_sel)]

if q.strip():
    pattern = re.escape(q.strip())
    mask = pd.Series(False, index=filtered.index)
    for c in filtered.columns:
        s = filtered[c].astype(str)
        mask = mask | s.str.contains(pattern, case=False, na=False)
    filtered = filtered[mask]

st.markdown("### Results")
st.write(f"Rows: **{len(filtered):,}** / {len(df):,}")

st.dataframe(filtered[shown_cols], use_container_width=True, height=520)

csv = filtered[shown_cols].to_csv(index=False).encode("utf-8")
st.download_button("Download filtered results (CSV)", data=csv, file_name="filtered_results.csv", mime="text/csv")
