import uuid

from cassandra.cqlengine import columns, connection
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model


class User(Model):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    first_name = columns.Text()
    last_name = columns.Text()
    email = columns.Text()
