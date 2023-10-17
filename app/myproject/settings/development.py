# pylint: skip-file

import os

from distutils.util import strtobool

from myproject.settings.base import *  # noqa: F403

DEBUG: bool = bool(strtobool(os.environ.get("DEBUG", default="True")))

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS.append("django_extensions")  # noqa: F405
