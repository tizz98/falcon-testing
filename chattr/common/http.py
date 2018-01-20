import typing

from cassandra.cqlengine.models import Model

from chattr.common import errors


def get_object_or_404(model: typing.Type[Model], *args, **kwargs):
    try:
        return model.get(*args, **kwargs)
    except model.DoesNotExist:
        raise errors.HTTPNotFound(description='Requested object not found.')
