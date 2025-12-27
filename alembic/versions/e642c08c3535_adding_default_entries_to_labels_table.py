"""adding default entries to labels table

Revision ID: e642c08c3535
Revises: 
Create Date: 2025-12-27 22:58:18.740781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e642c08c3535'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
        -- 1. Insert default admin user
        INSERT INTO users (id, username, email, hashed_password, first_name, last_name, role, is_active)
        VALUES
            (1, 'admin', 'admin@admin.com', 'hashed_admin_password', 'Admin', 'User', 'admin', true)
        ON CONFLICT DO NOTHING;

        -- 2. Insert default expense labels (linked to admin user_id = 1)
        INSERT INTO labels (id, label_name, description, user_id)
        VALUES
            (1, 'Food', 'Meals, groceries, and dining out', 1),
            (2, 'Rent', 'Monthly house or apartment rent', 1),
            (3, 'Utilities', 'Electricity, water, gas, internet bills', 1),
            (4, 'Transport', 'Fuel, public transport, taxi, ride-sharing', 1),
            (5, 'Healthcare', 'Medical bills, pharmacy, insurance', 1),
            (6, 'Entertainment', 'Movies, subscriptions, hobbies', 1),
            (7, 'Travel', 'Trips, vacations, flights, hotels', 1),
            (8, 'Education', 'Courses, books, training, tuition', 1),
            (9, 'Shopping', 'Clothes, electronics, household items', 1),
            (10, 'Miscellaneous', 'Other uncategorized expenses', 1)
        ON CONFLICT DO NOTHING;

        -- 3. Insert default income labels (also tied to admin user_id = 1)
        INSERT INTO labels (id, label_name, description, user_id)
        VALUES
            (11, 'Salary', 'Monthly income from employer', 1),
            (12, 'Investments', 'Returns from stocks, bonds, or savings', 1),
            (13, 'Gifts', 'Monetary gifts received', 1),
            (14, 'Freelance', 'Income from freelance work or side gigs', 1),
            (15, 'Other Income', 'Any other sources of income', 1)
        ON CONFLICT DO NOTHING;
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        -- Remove seeded labels
        DELETE FROM labels WHERE id = 1;

        -- Remove seeded admin user
        DELETE FROM users WHERE id = 1;
    """)