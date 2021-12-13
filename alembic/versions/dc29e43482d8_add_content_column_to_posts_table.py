"""add content column to posts table

Revision ID: dc29e43482d8
Revises: ba68286bd75b
Create Date: 2021-12-12 17:49:18.847014

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc29e43482d8'
down_revision = 'ba68286bd75b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
