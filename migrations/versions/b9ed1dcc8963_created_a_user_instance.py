"""Created a user instance

Revision ID: b9ed1dcc8963
Revises: 1cfafa435356
Create Date: 2023-09-07 14:04:23.228651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9ed1dcc8963'
down_revision: Union[str, None] = '1cfafa435356'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
