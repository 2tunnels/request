#!/usr/bin/env python

import logging
import sys

from aiohttp.log import access_logger
from aiohttp.web import run_app

from requestd import create_application

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('%(levelname)s %(asctime)s %(module)s %(message)s'))

access_logger.setLevel(logging.INFO)
access_logger.addHandler(handler)

run_app(create_application())
