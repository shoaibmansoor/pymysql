"""empty message

Revision ID: dcfafcc97d75
Revises: 
Create Date: 2021-08-18 01:56:05.967393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcfafcc97d75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=False),
    sa.Column('last_name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('last_name')
    )
    op.create_table('details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=150), nullable=False),
    sa.Column('country_origin', sa.String(length=150), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('age'),
    sa.UniqueConstraint('country_origin')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('details')
    op.drop_table('user')
    # ### end Alembic commands ###