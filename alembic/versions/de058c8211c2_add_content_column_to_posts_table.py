"""add content column to posts table

Revision ID: de058c8211c2
Revises: 1ed5e28c83ab
Create Date: 2024-03-29 16:27:54.999947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de058c8211c2'
down_revision: Union[str, None] = '1ed5e28c83ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')  # type: ignore[arg-type]  # noqa: F821, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E231, E501, E
    pass
