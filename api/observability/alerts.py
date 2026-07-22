from datetime import datetime
from uuid import uuid4

from api.models.alert_models import Alert
from api.observability.notification_manager import notification_manager

class AlertManager:

    def __init__(self):
        self.active = []

    def raise_alert(
        self,
        name,
        severity,
        source,
        message,
        metadata=None
    ):

        alert = Alert(
            id=str(uuid4()),
            name=name,
            severity=severity,
            status="ACTIVE",
            source=source,
            message=message,
            created_at=datetime.utcnow(),
            metadata=metadata or {}
        )

        self.active.append(alert)

        notification_manager.notify(alert)

        return alert

    def list_alerts(self):
        return self.active

alert_manager = AlertManager()
