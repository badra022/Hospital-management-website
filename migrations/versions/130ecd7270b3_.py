"""empty message

Revision ID: 130ecd7270b3
Revises: 
Create Date: 2021-01-12 04:08:15.559985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '130ecd7270b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctor', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('date', sa.Time(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('forms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('script', sa.Text(), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('job', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('d_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['users.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('p_accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.ForeignKeyConstraint(['email'], ['users.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_p_accounts_phone'), 'p_accounts', ['phone'], unique=True)
    op.create_table('scans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('p_id', sa.Integer(), nullable=True),
    sa.Column('file_url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['p_id'], ['p_accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('scans')
    op.drop_index(op.f('ix_p_accounts_phone'), table_name='p_accounts')
    op.drop_table('p_accounts')
    op.drop_table('d_accounts')
    op.drop_table('users')
    op.drop_table('forms')
    op.drop_table('appointment')
    # ### end Alembic commands ###
