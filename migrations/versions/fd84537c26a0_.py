"""empty message

Revision ID: fd84537c26a0
Revises: b78663732c73
Create Date: 2024-02-12 03:30:06.611114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd84537c26a0'
down_revision = 'b78663732c73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_photo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo_path', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_photo', schema=None) as batch_op:
        batch_op.drop_column('photo_path')

    # ### end Alembic commands ###
