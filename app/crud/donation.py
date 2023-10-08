from app.crud.base import CRUDBase
from app.models import Donation


class CRUDDonation(CRUDBase):
    """CRUD-класс для пожертвований."""
    pass


donation_crud = CRUDDonation(Donation)
