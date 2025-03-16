import pytest
from data_ingestion.receive_verified_data import receive_data
from data_processing.clean_data import DataCleaner
from storage.postgres_models import User
from config.database import get_session

@pytest.mark.asyncio
async def test_data_pipeline():
    # Test data ingestion
    test_data = {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "dob": "1990-01-01"}
    ingested_data = await receive_data("https://api.example.com/users", "test_api_key")
    assert ingested_data == test_data

    # Test data cleaning
    cleaner = DataCleaner()
    cleaned_data = {
        "first_name": cleaner.clean_name(test_data["first_name"]),
        "last_name": cleaner.clean_name(test_data["last_name"]),
        "email": cleaner.clean_email(test_data["email"]),
        "dob": cleaner.clean_date(test_data["dob"])
    }
    assert cleaned_data["email"] == "john.doe@example.com"

    # Test data storage
    session = next(get_session())
    user = User(**cleaned_data)
    session.add(user)
    session.commit()
    assert user.user_id is not None