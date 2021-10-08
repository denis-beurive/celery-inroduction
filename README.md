# Celery introduction

You may need to install or update `pipenv`. One way to do this is:

```bash
sudo apt install pipenv
pip install pipenv -U
```

> Please make sure to update `pipenv` (`pip install pipenv -U`). You need the last version.

```bash
git clone git@github.com:denis-beurive/celery-inroduction.git
cd celery-inroduction
```

Install the Python dependencies:

```bash
pipenv install
```

> We use REDIS over Rabbit-MQ since it is much lighter to install and configure.

Activate the shell:

```bash
pipenv shell
```

We assume that you already installed REDIS. Let REDIS_IP be the IP address used by REDIS to listen to messages.

Please edit the file [setup-env.sh](setup-env.sh), and set the value of `REDIS_IP`.

SEt the environment:

```bash
source setup-env.sh
```

Make sure that REDIS is started.

```bash
$ redis-cli -h $REDIS_IP PING
PONG
```

Then start workers for the tasks defined in the module `celery_introduction.tasks`:

```bash
$ celery -A celery_introduction.tasks worker --loglevel=INFO
...
[tasks]
  . celery_introduction.tasks.add
  . celery_introduction.tasks.subtract

[2021-10-08 11:48:25,050: INFO/MainProcess] Connected to redis://172.16.177.128:6379//
[2021-10-08 11:48:25,063: INFO/MainProcess] mingle: searching for neighbors
[2021-10-08 11:48:26,098: INFO/MainProcess] mingle: all alone
[2021-10-08 11:48:26,137: INFO/MainProcess] celery@labo ready.
```

OK, now we are ready to execute the tasks.

```bash
$ python -m celery_introduction.run
```

Please note that we can see LOG messages from `celery`:

```bash
[2021-10-08 11:52:17,680: INFO/MainProcess] Task celery_introduction.tasks.add[ed1792a2-463e-4f17-a095-ca382567ee98] received
[2021-10-08 11:52:17,681: INFO/ForkPoolWorker-1] Task celery_introduction.tasks.add[ed1792a2-463e-4f17-a095-ca382567ee98] succeeded in 0.0003252789992984617s: 5
[2021-10-08 11:52:17,690: INFO/MainProcess] Task celery_introduction.tasks.subtract[470b50bb-3dc8-42d7-af47-16aa8214b492] received
[2021-10-08 11:52:17,692: INFO/ForkPoolWorker-1] Task celery_introduction.tasks.subtract[470b50bb-3dc8-42d7-af47-16aa8214b492] succeeded in 0.00011070199980167672s: -1
```

> The 2 tasks have been executed.
