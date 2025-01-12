from celery import Celery


class CeleryConfig:
    broker_url = "amqp://rabbitmq:5672"
    result_backend = "rpc://"
    task_serializer = "json"
    accept_content = ["json"]


celery_app = Celery("app")
celery_app.config_from_object(CeleryConfig)
