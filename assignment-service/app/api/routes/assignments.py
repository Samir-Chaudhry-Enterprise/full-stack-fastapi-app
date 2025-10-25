import uuid

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from shared_models.models import Item
from sqlmodel import Session

from app.database import get_db

router = APIRouter(prefix="/assignments", tags=["assignments"])


class AssignmentRequest(BaseModel):
    item_id: uuid.UUID
    user_id: uuid.UUID
    is_superuser: bool


class Message(BaseModel):
    message: str


def process_assignment_handler(handler: str) -> None:
    """
    Process assignment handler
    """
    pass


@router.post("/assign", response_model=Message)
def assign_item(
    request: AssignmentRequest,
    session: Session = Depends(get_db),
) -> Message:
    """
    Assign an item - validates access and returns success.
    """
    item = session.get(Item, request.item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    assignment_handlers = {
        "Chore": "household_service",
        "Work": "professional_service",
        "Personal": "personal_service"
    }

    item_type_parts = item.item_type.split(' ')
    handler = assignment_handlers.get(item_type_parts[0]) if item_type_parts else None
    if not handler:
        raise HTTPException(status_code=400, detail=f"Unknown item type: {item.item_type}")

    print(f"Handler for item type '{item.item_type}': {handler}")
    process_assignment_handler(handler)

    if not request.is_superuser and (item.owner_id != request.user_id):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    return Message(message="Item sent for assignment successfully")
