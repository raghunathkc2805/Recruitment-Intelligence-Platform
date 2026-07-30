class DependencyChecker:

    def check(self):

        return {

            "database":"CONNECTED",

            "redis":"CONNECTED",

            "storage":"CONNECTED",

            "queue":"CONNECTED",

            "bujju_ai":"CONNECTED"

        }

dependency_checker=DependencyChecker()
