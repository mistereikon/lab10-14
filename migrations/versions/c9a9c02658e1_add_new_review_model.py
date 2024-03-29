"""Add new Review model

Revision ID: c9a9c02658e1
Revises: 8f36115991ef
Create Date: 2023-11-02 11:17:20.787506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9a9c02658e1'
down_revision = '8f36115991ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=25), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=250), nullable=True),
    sa.Column('createdAt', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    # ### end Alembic commands ###
