# 🚀 TrustID: Blockchain-Powered Digital Identity Verification



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



---


# 🔐 TrustID Data Engineering

## 📂 Project Structure

```
trustid_data_engineering/
├── 🏗 data_ingestion/
│   ├── 📥 fetch_user_data.py  # Pulls user data from input sources
│   ├── 🔑 fetch_credentials.py  # Retrieves issued credentials
│   ├── 🛡 fetch_verification_requests.py  # Tracks verification requests
│   ├── __init__.py
│
├── 🔄 data_processing/
│   ├── 🧹 clean_data.py  # Cleans and formats data
│   ├── 🔀 transform_data.py  # Maps data to appropriate models
│   ├── 🔒 encrypt_data.py  # Handles OpenSSL encryption
│   ├── __init__.py
│
├── 🗄 storage/
│   ├── 🏛 postgres_models.py  # PostgreSQL table definitions
│   ├── 🔗 indy_ledger.py  # Functions to interact with Hyperledger Indy
│   ├── 🔐 openssl_keys.py  # Manages encryption keys
│   ├── __init__.py
│
├── 🔗 integration/
│   ├── 🌐 api_connector.py  # Connects to backend API
│   ├── ⚡ indy_connector.py  # Connects to Hyperledger Indy
│   ├── __init__.py
│
├── ⚙️ config/
│   ├── ⚙️ settings.py  # Configuration settings
│   ├── 🗃 database.py  # PostgreSQL connection
│   ├── __init__.py
│
├── 🛠 scripts/
│   ├── 🏗 setup_db.py  # Initializes PostgreSQL tables
│   ├── 🔨 setup_indy.py  # Initializes Indy Ledger schemas
│   ├── __init__.py
│
├── ✅ tests/
│   ├── 🧪 test_data_pipeline.py  # Tests for ingestion & processing
│   ├── __init__.py
│
├── 📜 requirements.txt  # Python dependencies
├── 📖 README.md  # Project documentation
```

## 📁 Folder Descriptions

### 🏗 `data_ingestion/`
Handles collecting user identity data, credentials, and verification requests from multiple sources such as APIs, files, or blockchain transactions.

- 📥 `fetch_user_data.py`: Extracts raw user data from input sources.
- 🔑 `fetch_credentials.py`: Retrieves user-issued credentials.
- 🛡 `fetch_verification_requests.py`: Tracks and processes credential verification requests.

### 🔄 `data_processing/`
Responsible for cleaning, transforming, and securing data before storage.

- 🧹 `clean_data.py`: Standardizes and removes inconsistencies from ingested data.
- 🔀 `transform_data.py`: Maps the cleaned data into appropriate formats for storage and use.
- 🔒 `encrypt_data.py`: Uses OpenSSL encryption to ensure data security before storage.

### 🗄 `storage/`
Manages both relational database storage (PostgreSQL) and blockchain storage (Hyperledger Indy).

- 🏛 `postgres_models.py`: Defines PostgreSQL tables for structured data storage.
- 🔗 `indy_ledger.py`: Handles interactions with Hyperledger Indy for storing verifiable credentials.
- 🔐 `openssl_keys.py`: Manages cryptographic key storage and encryption.

### 🔗 `integration/`
Facilitates communication between the data pipeline and external services such as backend APIs and blockchain.

- 🌐 `api_connector.py`: Connects with the backend application API to exchange data.
- ⚡ `indy_connector.py`: Handles authentication and interaction with Hyperledger Indy.

### ⚙️ `config/`
Stores configuration settings for the entire system.

- ⚙️ `settings.py`: Contains global configuration parameters.
- 🗃 `database.py`: Manages PostgreSQL database connections and settings.

### 🛠 `scripts/`
Contains helper scripts for setting up and managing the system.

- 🏗 `setup_db.py`: Initializes PostgreSQL database tables.
- 🔨 `setup_indy.py`: Configures schemas in Hyperledger Indy.

### ✅ `tests/`
Includes unit tests to ensure that each component functions correctly.

- 🧪 `test_data_pipeline.py`: Tests ingestion and processing functions.

## 🔄 Data Workflow Summary

1. **📥 Ingestion:** Data is collected from APIs, files, or blockchain sources via the `data_ingestion` module.
2. **🧹 Processing:** The raw data is cleaned, transformed, and encrypted using scripts in `data_processing`.
3. **🗄 Storage:** Processed data is stored securely in PostgreSQL (`postgres_models.py`) or Hyperledger Indy (`indy_ledger.py`).
4. **🔗 Integration:** External applications retrieve and verify data through API endpoints and blockchain interactions handled by `integration/`.
5. **⚙️ Automation & Testing:** Configuration settings (`config/`) and scripts (`scripts/`) ensure smooth deployment, while tests (`tests/`) validate system functionality.

This structured approach ensures a secure, reliable, and scalable identity verification system. 🚀


