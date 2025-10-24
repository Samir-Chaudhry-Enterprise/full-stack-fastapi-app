"""trim_whitespace_from_item_type

Revision ID: 53b4ceec2c65
Revises: 44b6a9196e68
Create Date: 2025-10-24 19:42:21.106447

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '53b4ceec2c65'
down_revision = '44b6a9196e68'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("UPDATE item SET item_type = TRIM(item_type)")


def downgrade():
    pass
