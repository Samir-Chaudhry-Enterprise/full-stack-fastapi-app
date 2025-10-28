"""clean_item_type_values

Revision ID: 20251025223506
Revises: 44b6a9196e68
Create Date: 2025-10-25 22:35:06.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20251025223506'
down_revision = '44b6a9196e68'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("""
        UPDATE item 
        SET item_type = CASE 
            WHEN TRIM(SPLIT_PART(item_type, ' ', 1)) IN ('Work', 'Chore', 'Personal') 
            THEN TRIM(SPLIT_PART(item_type, ' ', 1))
            ELSE 'Personal'
        END
        WHERE item_type != TRIM(SPLIT_PART(item_type, ' ', 1))
           OR item_type NOT IN ('Work', 'Chore', 'Personal')
    """)


def downgrade():
    pass
