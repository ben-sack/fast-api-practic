"""create_main_tables
Revision ID: 4bb3c45721ea
Revises: 
Create Date: 2022-08-06 21:51:36.629070
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic
revision = "4bb3c45721ea"
down_revision = None
branch_labels = None
depends_on = None


def create_items_table() -> None:
    op.create_table(
        "items",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("ingredients", sa.Text, nullable=True),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )


def upgrade() -> None:
    create_items_table()


def downgrade() -> None:
    op.drop_table("items")
