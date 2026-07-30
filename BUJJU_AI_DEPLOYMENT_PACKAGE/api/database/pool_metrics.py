from sqlalchemy import event


class PoolMetrics:

    def __init__(self):

        self.checked_out = 0
        self.checked_in = 0
        self.connects = 0

    def register(self, engine):

        @event.listens_for(engine, "connect")
        def connect(dbapi_connection, connection_record):
            self.connects += 1

        @event.listens_for(engine, "checkout")
        def checkout(dbapi_connection, connection_record, connection_proxy):
            self.checked_out += 1

        @event.listens_for(engine, "checkin")
        def checkin(dbapi_connection, connection_record):
            self.checked_in += 1

    def report(self):

        return {

            "connections_created": self.connects,

            "checked_out": self.checked_out,

            "checked_in": self.checked_in,

            "active_connections":
                self.checked_out - self.checked_in,

        }


pool_metrics = PoolMetrics()
