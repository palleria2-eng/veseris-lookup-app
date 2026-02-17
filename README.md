# Spreadsheet Lookup App (Streamlit)

This is a small web app that turns an Excel spreadsheet into a searchable, filterable lookup tool.

## Features
- Upload an `.xlsx` file (or point to a local path)
- Search across all columns
- Filter by common columns if present (Brand / Model / Lamp Type / Lamp Code)
- Choose which columns to display
- Download filtered results as CSV
- Quick row detail view

## Run locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   streamlit run app.py
   ```

## Notes
- The app works with any spreadsheet, but it provides extra filters when it detects the common columns above.
