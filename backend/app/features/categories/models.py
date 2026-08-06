from datetime import datetime, timezone
from  sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped
from typing import Optional
from app.extensions.database import db

class Category(db.Model):
    __table__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)