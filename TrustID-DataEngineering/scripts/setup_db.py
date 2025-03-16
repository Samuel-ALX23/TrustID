from sqlmodel import SQLModel, create_engine
from config.settings import settings
from storage import postgres_models

def initialize_db():
    engine = create_engine(settings.POSTGRES_URL)
    SQLModel.metadata.create_all(engine)
    print("Database tables created successfully.")

if __name__ == "__main__":
    initialize_db()