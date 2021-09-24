# Default Executor

To check the airflow configuration (default)
docker exec -it {containerId} /bin/bash

```bash
grep executor airflow.cfg 
```

```bash
# The executor class that airflow should use. Choices include
# full import path to the class when using a custom executor.
executor = SequentialExecutor
# start with the elements of the list (e.g: "scheduler,executor,dagrun")
[celery_kubernetes_executor]
celery_app_name = airflow.executors.celery_executor
# The number of seconds to wait before timing out ``send_task_to_executor`` or
```

```bash
grep sql_alchemy_conn airflow.cfg 
```


```bash
sql_alchemy_conn = sqlite:////usr/local/airflow/airflow.db
# sql_alchemy_connect_args =
```

```bash
 grep smtp airflow.cfg 
 ```

# smtp server here
```bash
smtp_host = localhost
smtp_starttls = True
smtp_ssl = False
# Example: smtp_user = airflow
# smtp_user =
# Example: smtp_password = airflow
# smtp_password =
smtp_port = 25
smtp_mail_from = airflow@example.com
smtp_timeout = 30
smtp_retry_limit = 5
```