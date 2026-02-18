# Veseris UV Insect Lamp Finder

A simple web-based cross-reference tool for UV lamps used in flying insect traps.  
It helps pest control professionals find the correct replacement lamp (type, code, and Veseris stock numbers) by selecting brand and model.

Built with **Streamlit** — reads data directly from `data.xlsx`.

## Features
- Select brand → model
- Shows lamp type, code, case quantity
- Displays Veseris stock codes for **regular** and **shatterproof** versions
- Handles "N/A" entries gracefully
- Fully local/offline-capable once running

## Data Source
- Loaded from `data.xlsx` (Sheet1)
- Columns expected: Brand, Model, Lamp Type, Lamp Code, Veseris Stock Code (Regular) - Case, etc.
- Data accurate as of February 2026 (update the Excel as needed)

## How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
   cd YOUR-REPO-NAME
