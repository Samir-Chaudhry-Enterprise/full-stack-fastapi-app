"""trim_item_type_and_add_check_constraint

Revision ID: a1b2c3d4e5f6
Revises: 44b6a9196e68
Create Date: 2025-10-25 17:30:41.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = '44b6a9196e68'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("UPDATE item SET item_type = trim(item_type)")
    
    op.create_check_constraint(
        'ck_item_item_type_not_blank',
        'item',
        'char_length(trim(item_type)) > 0'
    )


def downgrade():
    op.drop_constraint('ck_item_item_type_not_blank', 'item', type_='check')
