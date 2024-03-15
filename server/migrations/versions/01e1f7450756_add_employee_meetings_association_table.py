"""add employee_meetings association table

Revision ID: 01e1f7450756
Revises: 71d4362e17c3
Create Date: 2024-03-15 13:15:09.367911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01e1f7450756'
down_revision = '71d4362e17c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees_meetings',
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('meetings.id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name=op.f('fk_employees_meetings_employee_id_employees')),
    sa.ForeignKeyConstraint(['meetings.id'], ['meetings.id'], name=op.f('fk_employees_meetings_meetings.id_meetings')),
    sa.PrimaryKeyConstraint('employee_id', 'meetings.id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees_meetings')
    # ### end Alembic commands ###
