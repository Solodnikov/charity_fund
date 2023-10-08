from sqlalchemy import Column, String, Text

from app.constants import MAX_LENGTH

from .base import InvestBaseModel


class CharityProject(InvestBaseModel):
    """Модель проектов для пожертвований."""
    name = Column(String(MAX_LENGTH), unique=True, nullable=False)
    description = Column(Text, nullable=False)
