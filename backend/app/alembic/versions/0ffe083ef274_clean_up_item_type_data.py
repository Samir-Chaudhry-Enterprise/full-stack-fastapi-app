"""clean_up_item_type_data

Revision ID: 0ffe083ef274
Revises: 44b6a9196e68
Create Date: 2025-10-26 06:03:51.150726

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '0ffe083ef274'
down_revision = '44b6a9196e68'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        UPDATE item 
        SET item_type = TRIM(item_type)
        WHERE item_type IS NOT NULL
    """)
    
    op.execute("""
        UPDATE item 
        SET item_type = SPLIT_PART(item_type, ' ', 1)
        WHERE item_type IS NOT NULL AND item_type LIKE '% %'
    """)
    
    op.execute("""
        UPDATE item 
        SET item_type = CASE 
            WHEN LOWER(item_type) LIKE 'work%' THEN 'Work'
            WHEN LOWER(item_type) LIKE 'chore%' THEN 'Chore'
            WHEN LOWER(item_type) LIKE 'personal%' THEN 'Personal'
            ELSE 'Personal'
        END
        WHERE item_type IS NOT NULL
    """)


def downgrade():
    pass
