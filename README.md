# NGO Impact Optimizer

NGO Impact Optimizer is a small analytics workspace for exploring how NGO programs perform relative to cost, reach, and outcome quality. The repository combines Python data-science utilities, a lightweight Express backend, and a simple React frontend so you can inspect the data, run analysis scripts, and build on top of the same project structure.

## What This Repo Contains

- Python scripts for inspecting datasets, handling missing values, standardizing records, and exploring distributions.
- A small Node.js backend that exposes a basic API health endpoint.
- A React frontend starter used as the UI entry point.
- CSV datasets in different stages of processing, plus generated outputs and reports.

## Repository Layout

- `backend/` - Express API used for local development and future integration work.
- `frontend/` - React app shell with the main UI entry point.
- `data-science/` - Core analysis scripts for loading, cleaning, and visualizing NGO data.
- `scripts/` - Introductory Python examples and data-processing demonstrations.
- `dataset/` - CSV files used as raw, cleaned, and transformed inputs.
- `data/` - Organized raw and processed data folders.
- `notebooks/` - Notebook-based experiments and structure demos.
- `outputs/` - Generated reports and analysis artifacts.

## Data Workflow

1. Inspect the source data and confirm column types, shape, and completeness.
2. Clean the dataset by handling duplicates, missing values, and inconsistent records.
3. Explore distributions, outliers, and relationships between cost, reach, and impact.
4. Save summaries and visual outputs for reporting or follow-up analysis.

## Tech Stack

- Python: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- Backend: `express`, `cors`, `dotenv`
- Frontend: `react`, `react-dom`, `react-scripts`, `axios`

## Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd ngo-impact-optimizer
```

### 2. Run the Python analysis tools

The main analysis scripts expect to be run from inside the `data-science/` folder so their relative dataset paths resolve correctly.

```bash
cd data-science
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python analysis.py
```

Other useful scripts in this folder include `inspect_data.py`, `summary_statistics.py`, `handle_missing_values.py`, and `distribution_visualization.py`.

### 3. Start the backend

In a separate terminal:

```bash
cd backend
npm install
npm start
```

The API responds at `http://localhost:5000/` with a simple status message.

### 4. Start the frontend

In another terminal:

```bash
cd frontend
npm install
npm start
```

## Notes

- The backend is intentionally minimal and is ready to expand into a richer API.
- The frontend currently provides a lightweight starter interface.
- Most of the project value lives in the Python analysis layer and the curated datasets.

## Summary

This repository is a structured NGO data-analysis project that focuses on cleaning and understanding impact data, then presenting the work through a simple full-stack scaffold. It is best suited for exploratory analysis, reporting, and as a base for a more advanced decision-support tool.
