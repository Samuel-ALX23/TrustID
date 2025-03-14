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

To add icons and colors to the README, you can use Markdown with emojis and inline HTML for styling. Here's an updated version of your project structure with icons and some color highlights:

```markdown
# TrustID Data Engineering

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


