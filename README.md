# 🚀 TrustID: Blockchain-Powered Digital Identity Verification 
# TrustID Data Engineering



TrustID is a blockchain-powered digital identity verification system that ensures secure, tamper-proof, and verifiable credentials. Built on **Hyperledger Indy** and **PostgreSQL**, TrustID allows users to manage and share their credentials (e.g., National ID, Passports, Degrees) with organizations in a privacy-preserving, decentralized way.

## 🔹 Key Features
- ✅ **Decentralized Identifiers (DIDs)** for secure user authentication
- ✅ **Verifiable Credentials** stored on blockchain for authenticity
- ✅ **Automated Data Extraction** using OCR/AI for easy document verification
- ✅ **Revocation Registry** to track and prevent fraudulent credentials
- ✅ **Seamless Integration** for organizations to verify credentials in real-time


## 🛠 Technologies Used

| Component            | Technology Used |
|----------------------|----------------|
| **Blockchain Ledger** | Hyperledger Indy  → Decentralized Identity Ledger |
| **Database**        | PostgreSQL → User & Credential Storage |
| **Encryption**      | OpenSSL  → Encryption & Key Management |
| **Backend**        | Node.js |
| **Version Control** | Git & GitHub |
| **Dev Environment** | VS Code, Jupyter Notebook |
| **scripting** | Python|

---


## 📌 Our Mission
To provide a trustworthy, efficient, and privacy-centric digital identity system for seamless verification across industries like **finance, healthcare, and education**.


## Project Structure

📂 **trustid_data_engineering/**
```
├── **data_ingestion/** 🛠️  
│   ├── `receive_verified_data.py` ⚙️ # Accepts verified user data from backend  
│   ├── `receive_verified_credentials.py` 🔑 # Stores verified credentials  
│   ├── `__init__.py`  
│  
├── **data_processing/** 🧹  
│   ├── `clean_data.py` 🧼 # Cleans and formats data  
│   ├── `transform_data.py` 🔄 # Maps data to appropriate models  
│   ├── `encrypt_data.py` 🔒 # Handles OpenSSL encryption  
│   ├── `__init__.py`  
│  
├── **storage/** 💾  
│   ├── `postgres_models.py` 🗄️ # PostgreSQL table definitions  
│   ├── `indy_ledger.py` 📚 # Functions to interact with Hyperledger Indy  
│   ├── `openssl_keys.py` 🔑 # Manages encryption keys  
│   ├── `__init__.py`  
│  
├── **integration/** 🔗  
│   ├── `api_connector.py` 🌐 # Connects to backend API  
│   ├── `indy_connector.py` 🌍 # Connects to Hyperledger Indy  
│   ├── `__init__.py`  
│  
├── **config/** ⚙️  
│   ├── `settings.py` 🛠️ # Configuration settings  
│   ├── `database.py` 🗄️ # PostgreSQL connection  
│   ├── `__init__.py`  
│  
├── **scripts/** 📜  
│   ├── `setup_db.py` ⚙️ # Initializes PostgreSQL tables  
│   ├── `setup_indy.py` 📜 # Initializes Indy Ledger schemas  
│   ├── `__init__.py`  
│  
├── **tests/** 🔬  
│   ├── `test_data_pipeline.py` ✅ # Tests for ingestion & processing  
│   ├── `__init__.py`  
│  
├── `requirements.txt` 📑 # Python dependencies  
├── `README.md` 📖 # Project documentation  


```
# TrustID Data Engineering

## Folder Descriptions

### 1. `data_ingestion/` 🛠️  
Receives **already verified** data from the backend after user credentials are validated.

- `receive_verified_data.py` ⚙️: Accepts verified user identity data.
- `receive_verified_credentials.py` 🔑: Stores validated credentials (license, certificates, ID cards, etc.).

### 2. `data_processing/` 🧹  
Handles cleaning, transforming, and encrypting **only verified** data before storage.

- `clean_data.py` 🧼: Standardizes and removes inconsistencies.
- `transform_data.py` 🔄: Maps data into appropriate formats for structured storage.
- `encrypt_data.py` 🔒: Uses OpenSSL encryption before storing sensitive credentials.

### 3. `storage/` 💾  
Stores processed data in a **secure, structured manner** using PostgreSQL and Hyperledger Indy.

- `postgres_models.py` 🗄️: Defines PostgreSQL tables for structured storage.
- `indy_ledger.py` 📚: Manages interactions with Hyperledger Indy for storing verifiable credentials.
- `openssl_keys.py` 🔑: Handles cryptographic key storage and encryption.

### 4. `integration/` 🔗  
Manages communication between the data pipeline and external services.

- `api_connector.py` 🌐: Connects with the backend to receive verified data.
- `indy_connector.py` 🌍: Handles interactions with Hyperledger Indy for credential verification.

### 5. `config/` ⚙️  
Stores all configuration settings related to database, encryption, and system parameters.

- `settings.py` 🛠️: Contains global configuration parameters.
- `database.py` 🗄️: Manages PostgreSQL database connections and settings.

### 6. `scripts/` 📜  
Contains helper scripts for **initializing** the database and blockchain ledger.

- `setup_db.py` ⚙️: Initializes PostgreSQL database tables.
- `setup_indy.py` 📜: Configures schemas in Hyperledger Indy.

### 7. `tests/` 🔬  
Ensures that all data pipelines function correctly.

- `test_data_pipeline.py` ✅: Tests ingestion, processing, and storage components.

## Data Workflow Summary

1. **User Submission & Verification (Backend Responsibility)**  
   Users **either upload documents or manually enter credentials** (license, certificate, national ID, etc.).  
   Backend **extracts data** from uploaded documents.  
   Backend **verifies credentials** with external sources before sending them to storage.

2. **Data Ingestion**  
   Once credentials are verified, the **backend sends validated data** to the data pipeline.  
   The **data_ingestion** module receives and prepares the data for processing.

3. **Data Processing & Security**  
   Verified data is **cleaned, transformed, and encrypted** before storage.

4. **Storage & Blockchain Integration**  
   **PostgreSQL stores structured user credentials.**  
   **Hyperledger Indy stores decentralized verifiable credentials.**

5. **Integration & Retrieval**  
   Organizations or users can retrieve credentials via APIs or blockchain queries.  
   **Integration module ensures smooth data exchange between the backend and storage layers.**

This approach ensures a **secure, scalable, and reliable** system where only **verified** credentials are stored, maintaining trust and data integrity. 🚀

```
```
# Project Setup Guide

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.x
- PostgreSQL (if using local PostgreSQL setup)

## Setup Instructions

### 1. Create a Virtual Environment
It's highly recommended to create a virtual environment to manage your project dependencies.

`python3 -m venv trustid-env`


`source trustid-env/bin/activate`  # Activate the virtual environment


`Install Required Python Packages`

## Once inside your virtual environment, install the required dependencies for the project.

```
```
`pip install sqlalchemy`           # ORM for interacting with PostgreSQL
`pip install psycopg2-binary`      # PostgreSQL adapter for SQLAlchemy
`pip install indy-sdk`              # Hyperledger Indy SDK for interacting with Indy Ledger
`pip install cryptography`         # For encryption and decryption tasks
`pip install requests`              # For making HTTP requests (e.g., integration with backend)
`pip install python-dotenv`        # For loading environment variables from .env files
`pip install openSSL`            # OpenSSL bindings for Python (if needed for encryption)
`pip install pytest`               # For testing your code



