import os
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

from chattr.users.models import User

connection.setup(
    hosts=[os.getenv('CASSANDRA_HOST', '127.0.0.1')],
    default_keyspace=os.getenv('CASSANDRA_KEYSPACE', "cqlengine"),
    protocol_version=3,
)

# Sync tables - probably a better way to handle this
sync_table(User)
