"""Initial migration

Revision ID: 142b7c115488
Revises: 
Create Date: 2025-03-14 00:18:08.813248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '142b7c115488'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('listing',
    sa.Column('ListingID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ListingOwner', sa.Integer(), nullable=False),
    sa.Column('ListingName', sa.String(length=255), nullable=False),
    sa.Column('ListingCategory', sa.String(length=255), nullable=False),
    sa.Column('ListingPrice', sa.Float(), nullable=False),
    sa.Column('ListingItem', sa.Float(), nullable=False),
    sa.Column('ListingDesc', sa.String(length=500), nullable=True),
    sa.Column('isActive', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('ListingID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('listing')
    # ### end Alembic commands ###
