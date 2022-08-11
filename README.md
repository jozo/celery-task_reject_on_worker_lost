# celery-task_reject_on_worker_lost

## Steps to reproduce the error:

1. Start redis
```
docker-compose up redis
```

2. Start celery
```
docker-compose up celery
```

3. Add a task
```
docker-compose up app
```

4. Kill celery - e.g. press 2x `Ctrl+C`

5. Start again celery and check if it starts processing the killed task (it does not)
