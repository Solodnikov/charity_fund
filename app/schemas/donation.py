from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt

from app.constants import MIN_LENGTH


class DonationBase(BaseModel):
    """Базовая схема пожертвований."""
    full_amount: PositiveInt = Field(title='Сумма пожертвования')
    comment: Optional[str] = Field(None, title='Комментарий к пожертвованию')


class DonationCreate(DonationBase):
    """Схема для создания пожертвования."""
    class Config:
        extra = Extra.forbid


class DonationDB(DonationBase):
    """Схема пожертвования для пользователя."""
    id: int = Field(title='Идентификатор пожертвования')
    create_date: datetime = Field(title='Дата внесения пожертвования')

    class Config:
        title = 'Схема пожертвования для получения'
        orm_mode = True


class DonationDBSuperUser(DonationDB):
    """Схема пожертвования из базы для суперпользователя."""
    user_id: Optional[int] = Field(None, title='Идентификатор пользователя')
    invested_amount: int = Field(
        MIN_LENGTH,
        title='Сумма пожертвования',
    )
    fully_invested: bool = Field(False, title='Внесена полная сумма')
    close_date: Optional[datetime] = Field(None, title='Дата внесения пожертвования')

    class Config:
        orm_mode = True
