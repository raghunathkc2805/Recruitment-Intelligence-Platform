from .checks import HealthChecks

class HealthService:

    def __init__(self):

        self.checks = HealthChecks()

    def health(self):

        return {
            "status":"healthy"
        }

    def liveness(self):

        return {
            "status":"ALIVE"
        }

    def readiness(self):

        return {

            "status":"READY",

            "database":self.checks.database(),

            "redis":self.checks.redis(),

            "storage":self.checks.storage(),

            "queues":self.checks.queues(),

            "bujju":self.checks.ai_engine()

        }

