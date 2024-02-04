"""empty message

Revision ID: 6bef9842379e
Revises: 434ce2a67802
Create Date: 2024-01-31 22:33:32.862726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bef9842379e'
down_revision = '434ce2a67802'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite_park', schema=None) as batch_op:
        batch_op.alter_column('park_id',
               existing_type=sa.INTEGER(),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorite_park', schema=None) as batch_op:
        batch_op.alter_column('park_id',
               existing_type=sa.String(length=100),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###
