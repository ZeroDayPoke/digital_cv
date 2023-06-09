"""init

Revision ID: 471a1bee5c65
Revises: 
Create Date: 2023-07-12 15:48:21.047067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '471a1bee5c65'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('content_file', sa.String(length=500), nullable=True),
    sa.Column('id', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('projects',
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('role', sa.String(length=120), nullable=True),
    sa.Column('repo_link', sa.String(length=500), nullable=True),
    sa.Column('live_link', sa.String(length=500), nullable=True),
    sa.Column('id', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('id', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('skills',
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('id', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('verification_token', sa.String(length=40), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.Column('token_generated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.String(length=60), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_users_username'), ['username'], unique=True)

    op.create_table('blog_skills',
    sa.Column('blog_id', sa.String(length=60), nullable=False),
    sa.Column('skill_id', sa.String(length=60), nullable=False),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ),
    sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
    sa.PrimaryKeyConstraint('blog_id', 'skill_id')
    )
    op.create_table('project_skills',
    sa.Column('project_id', sa.String(length=60), nullable=False),
    sa.Column('skill_id', sa.String(length=60), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
    sa.PrimaryKeyConstraint('project_id', 'skill_id')
    )
    op.create_table('user_roles',
    sa.Column('user_id', sa.String(length=60), nullable=True),
    sa.Column('role_id', sa.String(length=60), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_roles')
    op.drop_table('project_skills')
    op.drop_table('blog_skills')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_username'))
        batch_op.drop_index(batch_op.f('ix_users_email'))

    op.drop_table('users')
    op.drop_table('skills')
    op.drop_table('roles')
    op.drop_table('projects')
    op.drop_table('blogs')
    # ### end Alembic commands ###
