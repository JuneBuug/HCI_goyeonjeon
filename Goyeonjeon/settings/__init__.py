try:
    from django.contrib.messages import constants as messages
    MESSAGE_TAGS = {
        messages.ERROR: 'danger',
    }
except ImportError:
    pass