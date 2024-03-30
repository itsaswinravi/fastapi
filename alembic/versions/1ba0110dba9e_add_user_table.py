"""add user table

Revision ID: 1ba0110dba9e
Revises: de058c8211c2
Create Date: 2024-03-29 16:36:50.380345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ba0110dba9e'
down_revision: Union[str, None] = 'de058c8211c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
