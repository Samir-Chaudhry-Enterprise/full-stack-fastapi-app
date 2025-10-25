from sqlmodel import Session, select, func

from app.initial_data import create_sample_data
from app.models import Item, User


def test_create_sample_data(db: Session) -> None:
    """Test that create_sample_data creates users and items."""
    create_sample_data(db)
    
    users = db.exec(select(User)).all()
    assert len(users) >= 3
    
    items = db.exec(select(Item)).all()
    assert len(items) >= 14
    
    for item in items:
        assert item.item_type is not None
        assert len(item.item_type.strip()) > 0


def test_create_sample_data_idempotent(db: Session) -> None:
    """Test that create_sample_data can be called multiple times without duplicates."""
    create_sample_data(db)
    users_count_1 = db.exec(select(func.count()).select_from(User)).one()
    items_count_1 = db.exec(select(func.count()).select_from(Item)).one()
    
    create_sample_data(db)
    users_count_2 = db.exec(select(func.count()).select_from(User)).one()
    items_count_2 = db.exec(select(func.count()).select_from(Item)).one()
    
    assert users_count_1 == users_count_2
    assert items_count_1 == items_count_2
