# SPDX-License-Identifier: AGPL-3.0
# Migration: Add Beneficiary Acknowledgment Columns
import os
from sqlalchemy import create_url, text
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("DATABASE_URL not found in .env")
    exit(1)

# Handle postgresql:// vs postgres:// for SQLAlchemy
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)

def migrate():
    with engine.connect() as conn:
        print("Adding is_acknowledged and acknowledgment_token to users table...")
        try:
            conn.execute(text("ALTER TABLE users ADD COLUMN is_acknowledged BOOLEAN DEFAULT FALSE"))
            conn.commit()
            print("Added is_acknowledged")
        except Exception as e:
            print(f"Skipping is_acknowledged: {e}")

        try:
            conn.execute(text("ALTER TABLE users ADD COLUMN acknowledgment_token VARCHAR"))
            conn.commit()
            print("Added acknowledgment_token")
        except Exception as e:
            print(f"Skipping acknowledgment_token: {e}")
            
        print("Migration complete.")

if __name__ == "__main__":
    migrate()
