"""add last few columns to posts table

Revision ID: 3fa7543b9804
Revises: 9c58a32edd22
Create Date: 2024-03-29 16:43:49.657155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fa7543b9804'
down_revision: Union[str, None] = '9c58a32edd22'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
