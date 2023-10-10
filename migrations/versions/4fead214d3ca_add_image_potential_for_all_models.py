"""add image potential for all models

Revision ID: 4fead214d3ca
Revises: 
Create Date: 2023-10-10 13:10:40.848908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fead214d3ca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_filename', sa.String(length=128), nullable=True))

    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_filename', sa.String(length=128), nullable=True))

    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_filename', sa.String(length=128), nullable=True))

    with op.batch_alter_table('tutorials', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_filename', sa.String(length=128), nullable=True))

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_filename', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('image_filename')

    with op.batch_alter_table('tutorials', schema=None) as batch_op:
        batch_op.drop_column('image_filename')

    with op.batch_alter_table('roles', schema=None) as batch_op:
        batch_op.drop_column('image_filename')

    with op.batch_alter_table('projects', schema=None) as batch_op:
        batch_op.drop_column('image_filename')

    with op.batch_alter_table('blogs', schema=None) as batch_op:
        batch_op.drop_column('image_filename')

    # ### end Alembic commands ###