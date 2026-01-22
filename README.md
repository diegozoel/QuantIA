# QuantIA: Supply Chain Operating System

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

## System Blueprint
![QuantIA System Architecture](docs/images/system_architecture.jpg)

## Project Overview
QuantIA is a modular data engineering framework designed to optimize supply chain operations through stochastic modeling and automated reasoning.

The primary objective is to address capital inefficiency ("Dead Stock") in high-volume logistics environments. Unlike traditional ERP systems that provide retrospective reporting, QuantIA utilizes Monte Carlo simulations and Linear Programming to forecast inventory risks and optimize procurement logic.

### Theoretical Framework
This project is backed by a comprehensive analysis of supply chain inefficiencies in emerging markets.
**[Download Full Whitepaper (PDF)](docs/QuantIA_Whitepaper_2026.pdf)**

### Core Objectives
* **Capital Allocation:** Reduce idle inventory through dynamic Reorder Point (ROP) calculation.
* **Risk Mitigation:** Shift from deterministic forecasting to probabilistic demand modeling.
* **Data Integrity:** Establish a Unified Pipeline to eliminate data fragmentation.

## System Architecture
The project follows a strict Layered Architecture to ensure separation of concerns, reproducibility, and scalability:

```text
QuantIA/
├── docker/             # Containerization and environment configuration
├── src/
│   ├── data_engine/    # Stochastic generator (Log-Normal/Poisson models)
│   ├── optimization/   # Mathematical modeling algorithms (SciPy/NumPy)
│   └── main.py         # Application entry point
├── notebooks/          # Exploratory Data Analysis (EDA)
├── docs/               # Technical documentation and Whitepaper
└── tests/              # Unit and integration testing

## Technical Stack

| Domain | Technology | Application |
| :--- | :--- | :--- |
| **Core Language** | Python 3.10 | Application logic with strict type-hinting |
| **Infrastructure** | Docker | Containerized development environment |
| **Data Processing** | Pandas / NumPy | Vectorized operations for high-volume datasets |
| **Scientific Computing** | SciPy | Optimization algorithms and statistical modeling |

## Development Roadmap

- [x] **Phase 1: Foundation** - Architecture design, Environment Isolation, and Git Strategy.
- [x] **Phase 2: Stochastic Data Engine** - Implementation of Log-Normal (Cost) and Poisson (Demand) generators.
- [ ] **Phase 3: ETL Pipeline** - Ingestion logic and SQL Database integration.
- [ ] **Phase 4: Math Core** - Integration of advanced simulation and forecasting models.
- [ ] **Phase 5: Reporting** - Visualization of KPIs and stock levels.
- [ ] **Phase 6: Automation** - Deployment of autonomous recommendation agents.

---
**Author:** Diego Zoel
*Operations Strategy & Systems Engineering*