"""Schema alignment

Revision ID: 449874d5dea4
Revises: 65cb880e2ac7
Create Date: 2026-07-21
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "449874d5dea4"
down_revision: Union[str, Sequence[str], None] = "65cb880e2ac7"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Align production schema with SQLAlchemy models."""

    op.execute("""
    DO $$
    BEGIN
        IF EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_schema='public'
              AND table_name='candidate_profiles'
        ) THEN
            DROP TABLE candidate_profiles;
        END IF;
    END $$;
    """)

    op.alter_column(
        "resumes",
        "resume_hash",
        existing_type=sa.String(length=64),
        nullable=False,
    )

    op.alter_column(
        "users",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
    )

    op.alter_column(
        "users",
        "updated_at",
        existing_type=sa.DateTime(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
    )

    op.drop_index("ix_users_username", table_name="users")

    op.create_unique_constraint(
        "uq_users_username",
        "users",
        ["username"],
    )


def downgrade() -> None:
    """Rollback schema alignment."""

    op.drop_constraint(
        "uq_users_username",
        "users",
        type_="unique",
    )

    op.create_index(
        "ix_users_username",
        "users",
        ["username"],
        unique=True,
    )

    op.alter_column(
        "users",
        "updated_at",
        existing_type=sa.DateTime(timezone=True),
        type_=sa.DateTime(),
        existing_nullable=False,
    )

    op.alter_column(
        "users",
        "created_at",
        existing_type=sa.DateTime(timezone=True),
        type_=sa.DateTime(),
        existing_nullable=False,
    )

    op.alter_column(
        "resumes",
        "resume_hash",
        existing_type=sa.String(length=64),
        nullable=True,
    )

    op.create_table(
        "candidate_profiles",
        sa.Column("id", sa.String(length=36), nullable=False),
        sa.Column("candidate_id", sa.String(length=36), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_candidate_profiles_candidate_id",
        "candidate_profiles",
        ["candidate_id"],
        unique=False,
    )
