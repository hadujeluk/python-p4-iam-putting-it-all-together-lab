"""empty message

Revision ID: 51e07146723d
Revises: fc8f48221459
Create Date: 2024-10-27 11:22:37.960575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51e07146723d'
down_revision = 'fc8f48221459'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('instructions',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('minutes_to_complete',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('bio',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('bio',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)

    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('minutes_to_complete',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('instructions',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
