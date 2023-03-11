"""Deleting numbers

Revision ID: 035c7a19ae67
Revises: 8bfff52e52c4
Create Date: 2023-02-10 15:57:38.644531

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "035c7a19ae67"
down_revision = "8bfff52e52c4"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table("divisors")
    op.drop_table("numbers")


def downgrade() -> None:
    op.create_table(
        "numbers",
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("square", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("number"),
    )
    op.create_table(
        "divisors",
        sa.Column("divisor", sa.Integer(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["number"],
            ["numbers.number"],
        ),
        sa.PrimaryKeyConstraint("divisor", "number"),
    )
