import logging
import traceback
from dronzaPanel.models import ActivityLog


class Data_Logger:
    @classmethod
    def log_error_message(cls, django_view, message, user_ip=None, user=None):
        error_message = str(message)
        logger = logging.getLogger()
        logger.error(traceback.format_exc())
        act_log = ActivityLog()
        act_log.django_view = django_view
        act_log.message = error_message
        act_log.stack_trace = traceback.format_exc()
        act_log.user_ip = user_ip
        act_log.user = user
        act_log.save()
        return error_message, act_log.id

    @classmethod
    def log_message(cls, user, msg, message_type, path=None, client_ip=None, project=None, flight=None):
        logger = logging.getLogger()
        logger.error(msg) if message_type == "error" else logger.debug(msg)
        act_log = ActivityLog()
        act_log.project = project
        act_log.flight = flight
        act_log.message = msg
        act_log.message_type = message_type
        act_log.request_path = path
        act_log.user_ip = client_ip
        act_log.user = user
        act_log.save()

    @classmethod
    def get_client_ip(cls, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
