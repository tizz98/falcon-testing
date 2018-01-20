import msgpack
import requests


def unpackb(data, **kwargs):
    kwargs.setdefault('encoding', 'utf-8')
    return msgpack.unpackb(data, **kwargs)


r = requests.post(
    'http://127.0.0.1:8000/users/',
    data=msgpack.dumps(dict(first_name='John', last_name='Doe', email='j@d.co')),
    headers={'Content-Type': 'application/msgpack'},
)
user_id = unpackb(r.content)['user']['id']

r = requests.get(
    'http://127.0.0.1:8000/users/',
    headers={'Content-Type': 'application/msgpack'},
)
print(unpackb(r.content))

r = requests.get(
    'http://127.0.0.1:8000/users/5a8d5e6e-fe2c-11e7-b73b-3c15c2eb7774/',
    headers={'Content-Type': 'application/msgpack'},
)
print(unpackb(r.content))

r = requests.get(
    'http://127.0.0.1:8000/users/{}/'.format(user_id),
    headers={'Content-Type': 'application/msgpack'},
)
print(unpackb(r.content))
