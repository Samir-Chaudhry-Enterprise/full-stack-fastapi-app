from sqlmodel import Session, select

from app.initial_data import create_sample_data
from app.models import Item, User


def test_create_sample_data(db: Session) -> None:
    """Test that create_sample_data creates sample users and items."""
    create_sample_data(db)

    users = db.exec(select(User)).all()
    assert len(users) >= 3, "Should have at least 3 sample users"

    items = db.exec(select(Item)).all()
    assert len(items) >= 1, "Should have at least 1 sample item"

    sample_emails = [
        "john.doe@example.com",
        "jane.smith@example.com",
        "demo.user@example.com",
    ]
    user_emails = [user.email for user in users]
    for email in sample_emails:
        assert email in user_emails, f"Sample user {email} should exist"


def test_create_sample_data_idempotent(db: Session) -> None:
    """Test that create_sample_data can be called multiple times without errors."""
    create_sample_data(db)
    initial_user_count = len(db.exec(select(User)).all())
    initial_item_count = len(db.exec(select(Item)).all())

    create_sample_data(db)
    final_user_count = len(db.exec(select(User)).all())
    final_item_count = len(db.exec(select(Item)).all())

    assert (
        final_user_count == initial_user_count
    ), "Should not create duplicate users"
    assert (
        final_item_count == initial_item_count
    ), "Should not create duplicate items"
