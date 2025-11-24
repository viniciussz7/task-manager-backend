"""add user model and relationship

Revision ID: 9048e3cce04f
Revises: 43f0c5468461
Create Date: 2025-11-24 09:55:22.311339

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9048e3cce04f'
down_revision: Union[str, Sequence[str], None] = '43f0c5468461'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    
    with op.batch_alter_table('tasks') as batch_op:
        batch_op.add_column(sa.Column('owner_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            "fk_tasks_owner",
            "users",
            ["owner_id"],
            ["id"]
        )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # Remover FK e coluna em batch mode
    with op.batch_alter_table('tasks') as batch_op:
        batch_op.drop_constraint("fk_tasks_owner", type_="foreignkey")
        batch_op.drop_column('owner_id')

    # Remover tabela users
    op.drop_table('users')
    # ### end Alembic commands ###
