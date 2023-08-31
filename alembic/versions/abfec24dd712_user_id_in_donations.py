"""user.id in donations

Revision ID: abfec24dd712
Revises: d68090c94d67
Create Date: 2023-07-31 22:39:37.219674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abfec24dd712'
down_revision = 'd68090c94d67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donations', schema=None) as batch_op:
        batch_op.create_foreign_key('fk_donations_user_id_users', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donations', schema=None) as batch_op:
        batch_op.drop_constraint('fk_donations_user_id_users', type_='foreignkey')

    # ### end Alembic commands ###
