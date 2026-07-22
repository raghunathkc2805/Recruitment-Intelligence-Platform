class NotificationManager:

    def notify(self, alert):

        # Future integrations:
        # Email
        # Slack
        # Microsoft Teams
        # SMS
        # PagerDuty
        # Webhooks

        print(f"[ALERT] {alert.name}")

notification_manager = NotificationManager()
