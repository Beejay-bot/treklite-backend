"""add start address to trip table

Revision ID: cdc9e6519e2c
Revises: f55951b7ffdf
Create Date: 2019-09-27 16:14:49.671605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdc9e6519e2c'
down_revision = 'f55951b7ffdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trips', sa.Column('start_address', sa.String(), nullable=False))
    op.add_column('trips', sa.Column('start_latitude', sa.Numeric(precision=9, scale=6), nullable=False))
    op.add_column('trips', sa.Column('start_longitude', sa.Numeric(precision=9, scale=6), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('trips', 'start_longitude')
    op.drop_column('trips', 'start_latitude')
    op.drop_column('trips', 'start_address')
    # ### end Alembic commands ###
