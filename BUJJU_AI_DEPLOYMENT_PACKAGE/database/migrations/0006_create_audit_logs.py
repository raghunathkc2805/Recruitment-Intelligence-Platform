"""
Sprint 6
Enterprise Audit Logging Migration
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID

revision = "0006_create_audit_logs"
down_revision = "0005"
branch_labels = None
depends_on = None

def upgrade():

    op.create_table(
        "audit_logs",

        sa.Column("id", UUID(as_uuid=True), primary_key=True),

        sa.Column("tenant_id", UUID(as_uuid=True), nullable=True),
        sa.Column("organization_id", UUID(as_uuid=True), nullable=True),

        sa.Column("user_id", UUID(as_uuid=True), nullable=True),

        sa.Column("username", sa.String(255)),
        sa.Column("email", sa.String(255)),

        sa.Column("role_name", sa.String(150)),

        sa.Column("session_id", sa.String(255)),
        sa.Column("request_id", sa.String(255)),
        sa.Column("correlation_id", sa.String(255)),
        sa.Column("trace_id", sa.String(255)),

        sa.Column("action", sa.String(120), nullable=False),
        sa.Column("event_type", sa.String(120), nullable=False),

        sa.Column("resource_type", sa.String(150)),
        sa.Column("resource_id", sa.String(255)),
        sa.Column("resource_name", sa.String(255)),

        sa.Column("module", sa.String(150)),
        sa.Column("endpoint", sa.String(500)),
        sa.Column("http_method", sa.String(20)),

        sa.Column("status", sa.String(50), nullable=False),
        sa.Column("status_code", sa.Integer()),

        sa.Column("message", sa.Text()),
        sa.Column("reason", sa.Text()),

        sa.Column("before_data", JSONB),
        sa.Column("after_data", JSONB),
        sa.Column("metadata", JSONB),

        sa.Column("client_ip", sa.String(64)),
        sa.Column("forwarded_ip", sa.String(64)),
        sa.Column("user_agent", sa.Text()),

        sa.Column("device", sa.String(255)),
        sa.Column("browser", sa.String(255)),
        sa.Column("platform", sa.String(255)),

        sa.Column("country", sa.String(150)),
        sa.Column("city", sa.String(150)),

        sa.Column("latitude", sa.Float()),
        sa.Column("longitude", sa.Float()),

        sa.Column("request_body", JSONB),
        sa.Column("query_params", JSONB),
        sa.Column("headers", JSONB),

        sa.Column("response_time_ms", sa.Float()),

        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False
        )
    )

    indexes = [
        "created_at",
        "user_id",
        "action",
        "event_type",
        "resource_type",
        "resource_id",
        "session_id",
        "request_id",
        "correlation_id",
        "status"
    ]

    for idx in indexes:
        op.create_index(
            f"ix_audit_logs_{idx}",
            "audit_logs",
            [idx]
        )

def downgrade():

    indexes = [
        "status",
        "correlation_id",
        "request_id",
        "session_id",
        "resource_id",
        "resource_type",
        "event_type",
        "action",
        "user_id",
        "created_at"
    ]

    for idx in indexes:
        op.drop_index(
            f"ix_audit_logs_{idx}",
            table_name="audit_logs"
        )

    op.drop_table("audit_logs")
