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
│── docker/
│   ├── Dockerfile  # Defines Docker container setup
│   ├── docker-compose.yml  # Multi-container setup for API, PostgreSQL, and Indy Ledger
│   ├── .dockerignore  # Files to exclude from Docker builds
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


# TrustID System Overview

## 1️⃣ User Model
- **Description**: Stores user identity data
- **Storage**: PostgreSQL
- **Data Fields**:
  - `user_id (UUID)` - Unique user identifier
  - `first_name (String)` - User’s first name
  - `last_name (String)` - User’s last name
  - `email (String)` - User’s email
  - `phone_number (String)` - Contact number
  - `dob (Date)` - Date of birth
  - `created_at (Timestamp)` - Date of account creation
  - `updated_at (Timestamp)` - Last profile update

- **How it is Obtained**:
  - Entered by the user during registration.

- **Relationships**:
  - Links to **DID Model** (Each user gets a unique Decentralized ID)
  - Links to **Credentials** (A user can hold multiple credentials)

- **Future Changes**:
  - The user’s national ID and DID may be updated in the Hyperledger Indy Ledger for verification.

---

## 2️⃣ DID (Decentralized Identifier) Model
- **Description**: Stores unique blockchain-based ID for each user
- **Storage**: Hyperledger Indy Ledger
- **Data Fields**:
  - `did_id (UUID)` - Unique DID
  - `user_id (UUID)` - Links to the User Model
  - `public_key (String)` - Public key for verification
  - `private_key (Encrypted String)` - Private key (not stored directly; only a reference)
  - `created_at (Timestamp)`

- **How it is Obtained**:
  - Created automatically when a new user registers.

- **Relationships**:
  - Links to **User Model** (Each user has one DID)
  - Links to **Schema Model** (A DID is used to verify credentials)

- **Future Changes**:
  - DID data never changes, but if a user re-registers, a new DID can be issued.

---

## 3️⃣ Schema Model
- **Description**: Defines the structure of credentials issued
- **Storage**: Hyperledger Indy Ledger
- **Data Fields**:
  - `schema_id (UUID)` - Unique identifier
  - `schema_name (String)` - Credential name (e.g., "National ID Schema")
  - `attributes (JSONB)` - List of fields in the credential
  - `created_at (Timestamp)`

- **How it is Obtained**:
  - Created by the TrustID system admin when a new credential type is needed.

- **Relationships**:
  - Links to **DID Model** (Schemas define what can be assigned to a DID)
  - Links to **Credential Definition Model** (Schemas are used to generate credentials)

- **Future Changes**:
  - Schema updates result in new versions, but old credentials remain valid.

---

## 4️⃣ Credential Definition Model
- **Description**: Hashes of issued credentials stored for verification
- **Storage**: Hyperledger Indy Ledger
- **Data Fields**:
  - `cred_def_id (UUID)` - Unique ID
  - `schema_id (UUID)` - Links to a Schema
  - `issuer_did (UUID)` - DID of the credential issuer
  - `signature_type (String)` - Signature method used
  - `created_at (Timestamp)`

- **How it is Obtained**:
  - Generated when a user receives a credential.

- **Relationships**:
  - Links to **Schema Model** (Each Credential Definition is based on a Schema)
  - Links to **Credential Model** (Credential records use this definition)

- **Future Changes**:
  - If a schema is updated, a new credential definition must be issued.

---

## 5️⃣ Credential Model
- **Description**: Stores issued credentials
- **Storage**: PostgreSQL & Hyperledger Indy Ledger
- **Data Fields**:
  - `credential_id (UUID)` - Unique credential ID
  - `cred_def_id (UUID)` - Links to Credential Definition
  - `user_id (UUID)` - Links to the User Model
  - `attributes (JSONB)` - Contains the credential’s data
  - `status (String)` - Active, Revoked, or Expired
  - `created_at (Timestamp)`

- **How it is Obtained**:
  - Issued by an authorized organization (e.g., government agency, university).

- **Relationships**:
  - Links to **User Model** (Each user can have multiple credentials)
  - Links to **Credential Definition** (A credential follows a defined structure)
  - Links to **Revocation Registry** (Credential status is tracked)

- **Future Changes**:
  - If revoked, its status updates in PostgreSQL & Indy Ledger.

---

## 6️⃣ Revocation Registry Model
- **Description**: Tracks revoked credentials
- **Storage**: Hyperledger Indy Ledger
- **Data Fields**:
  - `revocation_id (UUID)` - Unique revocation ID
  - `credential_id (UUID)` - Links to revoked Credential
  - `revoked_at (Timestamp)`

- **How it is Obtained**:
  - Updated when a credential is revoked.

- **Relationships**:
  - Links to **Credential Model** (Stores revocation status)

- **Future Changes**:
  - Once revoked, credentials cannot be reinstated.

---

## 7️⃣ Verification Request Model
- **Description**: Tracks verification history
- **Storage**: PostgreSQL
- **Data Fields**:
  - `verification_id (UUID)` - Unique ID
  - `verifier_id (UUID)` - Organization requesting verification
  - `user_id (UUID)` - User being verified
  - `status (String)` - Pending, Verified, Failed
  - `timestamp (Timestamp)`

- **How it is Obtained**:
  - Created when an organization requests user verification.

- **Relationships**:
  - Links to **User Model** (User being verified)
  - Links to **Credential Model** (Verification is based on credentials)

- **Future Changes**:
  - Verification history remains immutable.

---

## 8️⃣ Encryption Key Model
- **Description**: Stores encryption keys for data security
- **Storage**: Local (OpenSSL)
- **Data Fields**:
  - `key_id (UUID)` - Unique key ID
  - `user_id (UUID)` - User owning the key
  - `public_key (String)` - Public key (used for verification)
  - `private_key (Encrypted)` - Private key (stored securely)
  - `created_at (Timestamp)`

- **How it is Obtained**:
  - Generated using OpenSSL upon user registration.

- **Relationships**:
  - Links to **DID Model** (Keys are used to sign transactions)

- **Future Changes**:
  - Keys can be rotated if compromised.

---

## Summary Table

| **Model**            | **Storage**               | **How It’s Obtained**                          | **Changes to Other Platforms?**         |
|----------------------|---------------------------|------------------------------------------------|-----------------------------------------|
| **User**             | PostgreSQL                | Entered by user                               | Links to DID on Indy Ledger            |
| **DID**              | Indy Ledger               | Auto-generated                                 | No changes                             |
| **Schema**           | Indy Ledger               | Created by system admin                       | Updates require new versions           |
| **Credential Definition** | Indy Ledger          | Created when a credential is issued           | Requires updates if schema changes     |
| **Credential**       | PostgreSQL + Indy Ledger  | Issued by an entity                           | Status updates in both DBs             |
| **Revocation Registry** | Indy Ledger            | When a credential is revoked                  | No changes after revocation            |
| **Verification Request** | PostgreSQL           | Created when verification is requested        | Status updates                         |
| **Encryption Keys**  | Local (OpenSSL)           | Auto-generated                                 | Can be rotated                         |

---

## 1️⃣ Types of Documents to Be Verified and Stored

### How These Credentials Are Captured:
1. **Manual Entry** – The user selects a credential type, and the system generates a form with relevant fields based on the schema.
2. **Document Upload** – Optical Character Recognition (OCR) or AI-based extraction tools analyze the document and extract the required data fields.
3. **Hybrid Approach** – Users upload a document, but they also get an editable form to verify or correct extracted details.

### Matching Credentials to Schema:
- When a user enters details manually, the input fields match the predefined schema stored in Hyperledger Indy.
- If a document is uploaded, only the required attributes are extracted and formatted correctly.
- The system validates the format and consistency of the credential before storing it in PostgreSQL and Hyperledger Indy Ledger.

---

## Sample Credentials

### National ID / Passport
- `credential_type`: "National ID" / "Passport"
- `holder_name`: Full name
- `date_of_birth`: YYYY-MM-DD
- `id_number`: Unique ID / Passport Number
- `gender`: Male / Female / Other
- `country_of_issue`: Country Name
- `expiration_date`: YYYY-MM-DD
- `issuing_authority`: Government Agency

### Driver’s License
- `credential_type`: "Driver’s License"
- `holder_name`: Full name
- `date_of_birth`: YYYY-MM-DD
- `license_number`: Unique License ID
- `issue_date`: YYYY-MM-DD
- `expiration_date`: YYYY-MM-DD
- `license_class`: Type of Vehicle Allowed
- `issuing_authority`: Government Transport Agency

### Educational Certificate
- `credential_type`: "Educational Certificate"
- `holder_name`: Full name
- `institution_name`: Name of School/University
- `degree`: Type of Qualification (e.g., BSc, MSc)
- `field_of_study`: Major/Discipline
- `date_of_graduation`: YYYY-MM-DD
- `certificate_id`: Unique Serial Number
- `grade`: Final Grade (Optional)
- `issuing_authority`: Name of Institution

### Employment Certificate
- `credential_type`: "Employment Certificate"
- `holder_name`: Full name
- `company_name`: Employer Name
- `job_title`: Position Held
- `employment_start_date`: YYYY-MM-DD
- `employment_end_date`: YYYY-MM-DD or "Present"
- `salary_range`: Optional (Currency & Amount)
- `supervisor_contact`: (Name & Email)
- `issuing_authority`: HR Department / Company Representative

### Other Types of Credentials
- **Professional License (Medical, Legal, Engineering, etc.)**
- **Property/Land Ownership Certificate**
- **Business Registration Certificate**

These details are captured, verified, and stored in the system as per the user’s consent and system permissions.


