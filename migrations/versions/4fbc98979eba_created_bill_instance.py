"""Created bill instance

Revision ID: 4fbc98979eba
Revises: b9ed1dcc8963
Create Date: 2023-09-07 18:51:22.748873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4fbc98979eba'
down_revision: Union[str, None] = 'b9ed1dcc8963'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
