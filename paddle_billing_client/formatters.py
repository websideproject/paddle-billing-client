import datetime
import json

from apiclient import JsonRequestFormatter
from apiclient.utils.typing import OptionalJsonType, OptionalStr


class CustomJsonRequestFormatter(JsonRequestFormatter):
    """Format the outgoing data as json."""

    content_type = "application/json"

    @staticmethod
    def default(o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat() + "Z"

    @classmethod
    def format(cls, data: OptionalJsonType) -> OptionalStr:
        if data:
            return json.dumps(data, default=cls.default)
