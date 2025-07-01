# Advanced API Final Project

A production-ready RESTful API for managing **Mechanics** and **Service Tickets**, built with Flask, SQLAlchemy, Marshmallow, and PostgreSQL, with CI/CD to Render and interactive Swagger documentation.

---

## 🚀 Live Demo

**API Base URL:**  
https://advanced-api-final.onrender.com  

**Swagger UI:**  
https://advanced-api-final.onrender.com/apidocs/  

---

## 📖 Table of Contents

- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Clone & Install](#clone--install)  
  - [Environment Variables](#environment-variables)  
  - [Database](#database)  
- [Running Locally](#running-locally)  
- [Testing](#testing)  
- [CI/CD Pipeline](#cicd-pipeline)  
- [Deployment to Render](#deployment-to-render)  
- [API Endpoints](#api-endpoints)  
- [Swagger Documentation](#swagger-documentation)  
- [Postman Collection](#postman-collection)  
- [Contributing](#contributing)  
- [License](#license)

---

## 🔥 Features

- **CRUD for Mechanics**  
- **Create & list Service Tickets**  
- **Assign / remove Mechanics** on a Ticket  
- **Flask Application Factory** pattern  
- **Environment-protected** secrets (no hardcoded URIs or keys)  
- **Gunicorn** WSGI server for production  
- **CI/CD** pipeline (lint → tests → deploy) via GitHub Actions  
- **Automated Deploy** to Render on every push to `main`  
- **Interactive Swagger UI** at `/apidocs/` over HTTPS  

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Marshmallow  
- **Database:** PostgreSQL (hosted on Render)  
- **Serialization & Validation:** Marshmallow, marshmallow-sqlalchemy  
- **Production WSGI:** Gunicorn  
- **CI/CD:** GitHub Actions  
- **Hosting:** Render.com  
- **API Docs:** Flasgger (Swagger UI)  

---

## 📥 Getting Started

### Prerequisites

- Python 3.11+  
- Git  
- (Optional) virtual environment tool (`venv`, `virtualenv`, etc.)  

---

### Clone & Install

```bash
git clone https://github.com/MotherTheresa64/Advanced-API-Final.git
cd Advanced-API-Final

# create and activate a virtual environment
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt