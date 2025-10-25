import logging

from sqlmodel import Session, select

from app import crud
from app.core.db import engine, init_db
from app.models import Item, ItemCreate, User, UserCreate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_sample_data(session: Session) -> None:
    """Create sample users and items for development/demo purposes."""

    # Create sample users
    sample_users = [
        {
            "email": "john.doe@example.com",
            "password": "password123",
            "full_name": "John Doe",
            "is_superuser": False,
        },
        {
            "email": "jane.smith@example.com",
            "password": "password123",
            "full_name": "Jane Smith",
            "is_superuser": False,
        },
        {
            "email": "demo.user@example.com",
            "password": "password123",
            "full_name": "Demo User",
            "is_superuser": False,
        },
    ]

    created_users = []
    for user_data in sample_users:
        # Check if user already exists
        existing_user = session.exec(
            select(User).where(User.email == user_data["email"])
        ).first()

        if not existing_user:
            user_create = UserCreate(**user_data)
            user = crud.create_user(session=session, user_create=user_create)
            created_users.append(user)
            logger.info(f"Created sample user: {user.email}")
        else:
            created_users.append(existing_user)
            logger.info(f"Sample user already exists: {existing_user.email}")

    # Create sample items for the users
    sample_items = [
        {
            "title": "My First Project",
            "description": "A web application built with FastAPI",
            "item_type": "Work",
        },
        {
            "title": "Shopping List",
            "description": "Groceries and household items to buy",
            "item_type": "Chore",
        },
        {
            "title": "Book Recommendations",
            "description": "List of books to read this year",
            "item_type": "Personal",
        },
        {
            "title": "Draft Meeting Notes",
            "description": "Draft notes from yesterday's meeting",
            "item_type": "Chore",
        },
        {
            "title": "Travel Plans",
            "description": "Places to visit during summer vacation",
            "item_type": "Personal",
        },
        {
            "title": "Learning Goals",
            "description": "Skills and technologies to learn",
            "item_type": "Personal",
        },
        {
            "title": "Recipe Collection",
            "description": "Favorite recipes and cooking ideas",
            "item_type": "Chore",
        },
        {
            "title": "Client Call",
            "description": "Quick reminder about the client call",
            "item_type": "Work",
        },
        {
            "title": "Workout Routine",
            "description": "Daily exercise and fitness plan",
            "item_type": "Personal",
        },
        {
            "title": "Meeting Notes",
            "description": "Important points from team meetings",
            "item_type": "Work",
        },
        {
            "title": "Bug Fixes",
            "description": "List of bugs to fix in the application",
            "item_type": "Work Project",
        },
        {
            "title": "Feature Ideas",
            "description": "New features to implement",
            "item_type": "Work",
        },
        {
            "title": "Project Planning",
            "description": "Q4 planning",
            "item_type": "Work Project",
        },
        {
            "title": "Home Repairs",
            "description": "Fix the sink",
            "item_type": "Chore Tasks",
        },
    ]

    # Check if sample items already exist (to avoid duplicates on restart)
    sample_items_exist = False
    for user in created_users:
        existing_items = session.exec(
            select(Item).where(Item.owner_id == user.id).limit(1)
        ).first()
        if existing_items:
            sample_items_exist = True
            break

    if not sample_items_exist:
        # Distribute items among users
        for i, item_data in enumerate(sample_items):
            user = created_users[i % len(created_users)]  # Cycle through users

            item_create = ItemCreate(**item_data)
            item = crud.create_item(
                session=session, item_in=item_create, owner_id=user.id
            )
            logger.info(f"Created item '{item.title}' for user {user.email}")
    else:
        logger.info("Sample items already exist, skipping item creation")


def init() -> None:
    with Session(engine) as session:
        # Create the initial superuser
        init_db(session)

        # Create sample data for development
        create_sample_data(session)


def main() -> None:
    logger.info("Creating initial data")
    init()
    logger.info("Initial data created")


if __name__ == "__main__":
    main()
