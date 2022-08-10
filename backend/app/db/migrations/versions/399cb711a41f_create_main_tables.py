"""create_main_tables
Revision ID: 399cb711a41f
Revises: 4bb3c45721ea
Create Date: 2022-08-06 22:59:56.754890
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic
revision = "399cb711a41f"
down_revision = None
branch_labels = None
depends_on = None


def create_items_table() -> None:
    op.create_table(
        "items",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("ingredients", sa.Text, nullable=True),
        sa.Column("item_type", sa.Text, nullable=False),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )


def upgrade() -> None:
    create_items_table()


def downgrade() -> None:
    op.drop_table("items")
