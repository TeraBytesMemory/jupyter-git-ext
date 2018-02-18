from notebook.base.handlers import APIHandler as IPyAPIHandler
from notebook.base.handlers import HTTPError
import json


class APIHandler(IPyAPIHandler):
    def finish(self, chunk=None):
        if type(chunk) == dict:
            chunk = json.dumps(chunk)
        return super().finish(chunk)
