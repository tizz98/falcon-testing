import json

import falcon
import msgpack


class MsgPackMixin:
    def to_json(self):
        err = super().to_json()
        return msgpack.dumps(json.loads(err))


class HTTPNotFound(MsgPackMixin, falcon.HTTPNotFound):
    pass
