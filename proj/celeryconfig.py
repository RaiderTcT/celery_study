from __future__ import absolute_import

# Broker settings.
# broker_url = 'amqp://ulysses:62300313@localhost:5672/ubuntu'

# List of modules to import when the Celery worker starts.
imports = ('proj.tasks',)

# Using the database to store task state and results.
result_backend = 'redis://localhost:6379/0'

# 将任务分配到不同的队列
# task_routes = {'tasks.add': 'low-priority',}

# 限制任务执行的效率： 每分钟10个这类任务
#　task_annotations = {'tasks.add': {'rate_limit': '10/s'}}

# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# timezone = 'Europe/Oslo'
# enable_utc = True
