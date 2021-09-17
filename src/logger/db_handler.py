import logging
from time import gmtime, strftime
import inspect


MEASUREMENT = "logs"
# DB_NAME = 'analyzer'
# PORT = 8086
# HOST = 'localhost'
# SERVER_URL = "http://localhost:8086"
# APP = 'analyzer'
# TOKEN = "my-token"
# ORG = "behnama"
# BUCKET = "behnama"


class LogDBHandler(logging.Handler):

    def __init__(self, write_api, config):
        logging.Handler.__init__(self)
        self.write_api = write_api
        self.config = config

    def save_log(self, record):
        # ToDO: add line number of call
        # if record.exc_info:  # for exceptions
        #     print("Exception %s", record.exc_info)
        data = [
           {
               'measurement': MEASUREMENT,
               'time': strftime("%Y-%m-%dT%H:%M:%SZ", gmtime()),
               "tags": {
                   'app': self.config.influx_app,
                   'scope': record.name,
                   'level': record.levelname
               },
               'fields': {
                   'message': record.getMessage(),
                   'caller': inspect.stack()[7].function
               }
           }
        ]
        self.write_api.write(self.config.influx_bucket, self.config.influx_org, data)

    def emit(self, record):
        # self.save_log(record)
        pass



