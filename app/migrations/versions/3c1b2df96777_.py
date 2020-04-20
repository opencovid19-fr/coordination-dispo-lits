"""empty message

Revision ID: 3c1b2df96777
Revises: 1f326b63fbdd
Create Date: 2020-04-20 15:27:00.870792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c1b2df96777'
down_revision = '1f326b63fbdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orga_region',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('code', sa.String(length=2), nullable=False),
    sa.Column('tncc', sa.String(length=20), nullable=False),
    sa.Column('libelle', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.add_column('orga_address', sa.Column('insee_code', sa.String(length=10), nullable=True))
    op.add_column('orga_organization', sa.Column('reg_code', sa.String(), nullable=True))
    op.create_foreign_key(None, 'orga_organization', 'orga_region', ['reg_code'], ['code'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orga_organization', type_='foreignkey')
    op.drop_column('orga_organization', 'reg_code')
    op.drop_column('orga_address', 'insee_code')
    op.drop_table('orga_region')
    # ### end Alembic commands ###
