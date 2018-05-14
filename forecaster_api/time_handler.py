import datetime
from dateutil import parser

class TimeHandler(object):
    MAX_TIMESTAMP_AGE = 1

    def current_timestamp(self):
        return str(datetime.datetime.now())

    def parse_timestamp(self, timestamp):
        return parser.parse(timestamp)

    def stale_timestamp(self, timestamp):
        return (datetime.datetime.now() - parse_timestamp(timestamp)).seconds // 3600 >= MAX_TIMESTAMP_AGE
