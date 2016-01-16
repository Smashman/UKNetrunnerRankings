"""Add pack cycle number

Revision ID: f91bacbf0876
Revises: 5d6356614f75
Create Date: 2016-01-11 23:38:37.282830

"""

# revision identifiers, used by Alembic.
revision = 'f91bacbf0876'
down_revision = '5d6356614f75'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pack', sa.Column('cycle_id', sa.Integer(), nullable=True))
    op.add_column('pack', sa.Column('num_in_cycle', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pack', 'cycle', ['cycle_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('pack_ibfk_1', 'pack', type_='foreignkey')
    op.drop_column('pack', 'num_in_cycle')
    op.drop_column('pack', 'cycle_id')
    ### end Alembic commands ###
