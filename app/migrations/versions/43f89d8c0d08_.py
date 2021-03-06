"""empty message

Revision ID: 43f89d8c0d08
Revises: 2821ed848df9
Create Date: 2020-04-22 13:11:22.769654

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '43f89d8c0d08'
down_revision = '2821ed848df9'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orga_region', 'libelle',
                    existing_type=sa.VARCHAR(length=20),
                    type_=sa.String(length=30),
                    existing_nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('orga_region', 'libelle',
                    existing_type=sa.String(length=30),
                    type_=sa.VARCHAR(length=20),
                    existing_nullable=False)
    ### end Alembic commands ###
