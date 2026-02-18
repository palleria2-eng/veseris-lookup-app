# app.py
import streamlit as st
import pandas as pd
from pathlib import Path

# ────────────────────────────────────────────────
# Configuration
# ────────────────────────────────────────────────
EXCEL_FILE = "data.xlsx"
SHEET_NAME = "Sheet1"           # change if your sheet has a different name

st.set_page_config(
    page_title="Veseris Lamp Finder",
    page_icon="💡",
    layout="wide"
)

# ────────────────────────────────────────────────
# Load and prepare data
# ────────────────────────────────────────────────
@st.cache_data
def load_data():
    if not Path(EXCEL_FILE).is_file():
        st.error(f"File not found: **{EXCEL_FILE}**\nPlease place 'data.xlsx' in the same folder as app.py")
        st.stop()

    try:
        df = pd.read_excel(
            EXCEL_FILE,
            sheet_name=SHEET_NAME,
            dtype=str,                      # treat everything as string to preserve leading zeros etc.
            keep_default_na=False
        )
        # Clean column names (remove extra spaces, line breaks, etc.)
        df.columns = df.columns.str.strip().str.replace(r'\s+', ' ', regex=True)

        # Expected columns (case-insensitive match)
        expected = [
            "Brand", "Model", "Lamp Type", "Lamp Code",
            "Veseris Stock Code (Regular) - Case",
            "Veseris Stock Code (Regular) - Each",
            "Veseris Stock Code (Shatterproof) - Case",
            "Veseris Stock Code (Shatterproof) - Each",
            "Case Quantity"
        ]

        # Rename columns to standardized internal names
        rename_map = {}
        for col in df.columns:
            lower = col.lower()
            if "brand" in lower:
                rename_map[col] = "brand"
            elif "model" in lower:
                rename_map[col] = "model"
            elif "lamp type" in lower:
                rename_map[col] = "lamp_type"
            elif "lamp code" in lower:
                rename_map[col] = "lamp_code"
            elif "regular" in lower and "case" in lower:
                rename_map[col] = "reg_case"
            elif "regular" in lower and "each" in lower:
                rename_map[col] = "reg_each"
            elif "shatterproof" in lower and "case" in lower:
                rename_map[col] = "shat_case"
            elif "shatterproof" in lower and "each" in lower:
                rename_map[col] = "shat_each"
            elif "case quantity" in lower or "case qty" in lower:
                rename_map[col] = "case_qty"

        df = df.rename(columns=rename_map)

        # Group by brand
        grouped = df.groupby("brand", sort=False)
        data = {}
        for brand, group in grouped:
            brand_data = group.to_dict("records")
            # Sort models alphabetically within each brand
            brand_data.sort(key=lambda x: x.get("model", "").strip().lower())
            data[brand.strip()] = brand_data

        return data, df

    except Exception as e:
        st.error(f"Error reading Excel file:\n{e}")
        st.stop()


# Load once
data_dict, full_df = load_data()

brands = sorted(data_dict.keys())

# ────────────────────────────────────────────────
# UI
# ────────────────────────────────────────────────
st.title("Veseris UV Insect Lamp Finder")
st.markdown("**Official UV Insect Trap Cross-Reference Guide**")

st.info("Select brand and model to view the correct lamp and Veseris stock codes.")

col1, col2 = st.columns([3, 4])

with col1:
    selected_brand = st.selectbox(
        "Brand / Company",
        options=[""] + brands,
        index=0,
        key="brand_select"
    )

if selected_brand and selected_brand in data_dict:
    models = [item["model"].strip() for item in data_dict[selected_brand]]
    with col2:
        selected_model = st.selectbox(
            "Product / Model",
            options=[""] + models,
            index=0,
            key="model_select"
        )

    if selected_model:
        # Find the matching row
        entry = next(
            (item for item in data_dict[selected_brand] if item["model"].strip() == selected_model.strip()),
            None
        )

        if entry:
            st.markdown("---")

            st.subheader(f"{entry['model']}  —  {selected_brand}")

            st.markdown(f"**Lamp Code:**  `{entry.get('lamp_code', '—')}`")

            c1, c2 = st.columns([2, 3])

            with c1:
                st.markdown("### Lamp Details")
                st.write(f"**Type:** {entry.get('lamp_type', '—')}")
                qty = entry.get("case_qty", "—")
                st.write(f"**Case Quantity:** {qty} per case" if qty != "—" and qty != "N/A" else "**Case Quantity:** —")

            with c2:
                st.markdown("### Veseris Stock Codes")

                r1, r2 = st.columns(2)

                with r1:
                    st.markdown("**Regular**")
                    st.write(f"Case: **{entry.get('reg_case', '—')}**")
                    st.write(f"Each: **{entry.get('reg_each', '—')}**")

                with r2:
                    st.markdown("**Shatterproof**")
                    st.write(f"Case: **{entry.get('shat_case', '—')}**")
                    st.write(f"Each: **{entry.get('shat_each', '—')}**")

            # Optional: show raw row for debugging
            # with st.expander("Raw data row"):
            #     st.json(entry)

            if st.button("Reset / Start New Search", type="primary"):
                st.rerun()

st.markdown("---")
st.caption(
    "Data loaded from **data.xlsx**  •  "
    "For latest pricing, availability or updates please contact Veseris.  "
    f"Last app refresh: {st.session_state.get('load_time', '—')}"
)
