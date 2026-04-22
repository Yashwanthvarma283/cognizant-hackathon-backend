# Backend Implementation Plan (Laptop 2)

This plan is for **Laptop 2**, which will handle the **Backend API Infrastructure and Data Handling** for the Supply Chain Digital Twin Platform.

> [!NOTE]
> Make sure to install python dependencies with `pip install -r requirements.txt` and start the server with `uvicorn main:app --reload`. 
> Note your local network IP (e.g. `192.168.x.x`) to provide to Laptop 1 so the frontend can reach this API.

## Goal Description
Build a robust, scalable FastAPI service capable of handling CSV ingestions, running simulation models, and feeding data to the supplier and admin dashboard KPIs.

## Execution Steps

### 1. Configuration & Architecture Setup
- [ ] Initialize Python Virtual Environment (e.g., `python -m venv venv`) and install `fastapi M uvicorn pandas`.
- [ ] Configure `CORS` correctly in `main.py` so the React application from Laptop 1 can request data securely.

### 2. Core API Endpoints
- [ ] **Auth Module**: Mock out or implement the role-based login logic (Consumer, Supplier, Admin) responding to the Frontend's Login page.
- [ ] **Data Ingestion Module**: Implement endpoints for the "CSV Upload" matching the Consumer Dashboard. Parse the CSV files robustly (using `Pandas`).
- [ ] **Simulation Engine**: Implement logic to calculate and return Simulation Results (Cost, Time) based on uploaded supply chain nodes.
- [ ] **Statistics & KPIs**: Build `GET` endpoints delivering KPI JSON aggregates for Supplier and Admin Dashboard charts.

### 3. Application Structure Optimization
- [ ] Separate logic into `/routers` and `/models`. Keep `main.py` purely for app configuration.
- [ ] Define standardized Pydantic models for expected JSON payloads and data validation.

## Verification Plan
- [ ] Utilize the `/docs` auto-generated Swagger UI to verify every endpoint before handing them off to the frontend on Laptop 1.
