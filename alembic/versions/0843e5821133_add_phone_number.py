"""add phone number

Revision ID: 0843e5821133
Revises: 8b2b206b49de
Create Date: 2021-12-12 18:54:03.376543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0843e5821133'
down_revision = '8b2b206b49de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
