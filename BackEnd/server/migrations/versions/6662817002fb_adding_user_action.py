"""Adding user action.

Revision ID: 6662817002fb
Revises: 71663fc02fff
Create Date: 2024-08-13 14:51:10.310126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6662817002fb'
down_revision = '71663fc02fff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_content_actions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('content_id', sa.Integer(), nullable=False),
    sa.Column('content_type', sa.String(length=50), nullable=False),
    sa.Column('action', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_content_actions')
    # ### end Alembic commands ###
