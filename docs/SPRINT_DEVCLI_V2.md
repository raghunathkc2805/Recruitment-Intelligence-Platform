================================================================================
SPRINT : Developer CLI v2.0
================================================================================

GOAL
----
Replace the monolithic dev.py with a modular command framework.

TARGET
------
tools/
¦
+-- dev.py
+-- core/
¦   +-- command_loader.py
¦   +-- registry.py
¦   +-- config.py
¦   +-- logger.py
¦
+-- commands/
¦   +-- doctor.py
¦   +-- build.py
¦   +-- backup.py
¦   +-- stats.py
¦   +-- test.py
¦   +-- validate.py
¦   +-- sync.py
¦   +-- release.py
¦   +-- ...
¦
+-- templates/

TASKS
-----
1. Dynamic command discovery
2. Automatic command registration
3. Plugin architecture
4. Common logger
5. Configuration loader
6. Remove all if/elif command dispatching
7. One class per command
8. Future command auto-loading

SUCCESS CRITERIA
----------------
python tools/dev.py doctor
python tools/dev.py stats
python tools/dev.py test
python tools/dev.py build
python tools/dev.py backup

must execute without modifying dev.py again.

================================================================================
