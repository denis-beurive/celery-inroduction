# Make sure that the environment is configured. You should have "sourced" the file "setup-env.sh".
# Then run, from the project root directory:
#
#      python -m celery_introduction.run

import celery_introduction.tasks
from celery.app.task import Task


def execute() -> None:
    t1: Task = celery_introduction.tasks.add
    t2: Task = celery_introduction.tasks.subtract
    t1.delay(2, 3)
    t2.delay(2, 3)


if __name__ == "__main__":
    execute()
