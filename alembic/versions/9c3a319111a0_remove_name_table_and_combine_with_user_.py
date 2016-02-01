"""Remove name table and combine with user table

Revision ID: 9c3a319111a0
Revises: df54f2fa989e
Create Date: 2016-01-16 20:49:02.093916

"""

# revision identifiers, used by Alembic.
revision = '9c3a319111a0'
down_revision = 'df54f2fa989e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('name')
    op.add_column('user', sa.Column('first_name', sa.String(length=512), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=512), nullable=True))
    op.add_column('user', sa.Column('nickname', sa.String(length=512), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'nickname')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.create_table('name',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('user_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('first_name', mysql.VARCHAR(length=512), nullable=True),
    sa.Column('last_name', mysql.VARCHAR(length=512), nullable=True),
    sa.Column('nickname', mysql.VARCHAR(length=512), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], name=u'name_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    ### end Alembic commands ###
