from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.constants import DEFAULT_INVESTED_AMOUNT
from app.crud.charity_project import charity_project_crud
from app.models import CharityProject


async def check_charity_project_exists(
        charity_project_id: int,
        session: AsyncSession,
) -> CharityProject:
    """
    Проверка существования объекта проекта по id.
    """
    charity_project = await charity_project_crud.get(charity_project_id, session)
    if charity_project is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Проект не найден!'
        )
    return charity_project


async def check_name_duplicate(
        project_name: str,
        session: AsyncSession,
) -> None:
    """
    Проверка дубликата имени проекта.
    """
    project_id = await charity_project_crud.get_name_by_id(
        project_name, session)
    if project_id:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Проект с таким именем уже существует!',
        )


async def check_project_open(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    """Проверка открыт ли проект."""
    charity_project = await charity_project_crud.get(project_id, session)
    if charity_project.close_date:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Закрытый проект нельзя редактировать!',
        )
    return charity_project


async def check_invested_amount(
        project_id: int,
        session: AsyncSession,
) -> CharityProject:
    """Проверка есть ли средства в проекте."""
    charity_project = await charity_project_crud.get(project_id, session)
    if charity_project.invested_amount > DEFAULT_INVESTED_AMOUNT:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='В проект были внесены средства, не подлежит удалению!',
        )
    return charity_project


async def check_investing_funds(
        project_id: int,
        obj_in_full_amount,
        session: AsyncSession,
) -> CharityProject:
    """Проверка необходимой суммы."""
    charity_project = await charity_project_crud.get(project_id, session)
    if obj_in_full_amount < charity_project.invested_amount:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Требуемая сумма проекта не может быть меньше вложенной!',
        )
    return charity_project
