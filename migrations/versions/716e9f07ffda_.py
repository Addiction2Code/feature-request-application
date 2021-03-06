"""empty message

Revision ID: 716e9f07ffda
Revises: 
Create Date: 2018-06-20 14:08:09.738259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '716e9f07ffda'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feature_request', sa.Column('target_date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('feature_request', 'target_date')
    # ### end Alembic commands ###
