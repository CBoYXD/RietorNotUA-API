"""add type, area, kwargs columns to Offers model

Revision ID: d7574ffb0cd5
Revises: 283b996b424a
Create Date: 2024-02-19 19:07:53.181628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "d7574ffb0cd5"
down_revision: Union[str, None] = "283b996b424a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("offers", sa.Column("type", sa.VARCHAR(length=20), nullable=False))
    op.add_column("offers", sa.Column("area", sa.Float(), nullable=False))
    op.add_column(
        "offers",
        sa.Column("kwargs", postgresql.JSON(astext_type=sa.Text()), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("offers", "kwargs")
    op.drop_column("offers", "area")
    op.drop_column("offers", "type")
    # ### end Alembic commands ###
