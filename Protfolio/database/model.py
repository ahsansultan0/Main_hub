from pathlib import Path
import sqlalchemy as db


# Project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database directory
DB_DIR = BASE_DIR / "database"

# Make sure database directory exists
DB_DIR.mkdir(exist_ok=True)

# Database file
DB_PATH = DB_DIR / "posts.db"

# SQLAlchemy engine
engine = db.create_engine(
    f"sqlite:///{DB_PATH}"
)

print("Engine created:", DB_PATH)


# Metadata
meta_obj = db.MetaData()


# Posts table
posts = db.Table(
    "posts",
    meta_obj,

    db.Column(
        "id",
        db.Integer,
        primary_key=True
    ),

    db.Column(
        "title",
        db.String,
        nullable=False
    ),

    db.Column(
        "content",
        db.String,
        nullable=False
    ),

    db.Column(
        "user_id",
        db.String(255),
        nullable=False
    )
)


# Create table if it doesn't exist
meta_obj.create_all(engine)