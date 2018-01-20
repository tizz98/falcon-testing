from wsgiref import simple_server

import falcon
from falcon import media

from chattr.users import resources as user_resources


handlers = media.Handlers({
    'application/msgpack': media.MessagePackHandler(),
})

app = falcon.API(media_type='application/msgpack')
app.req_options.media_handlers = handlers
app.resp_options.media_handlers = handlers

app.add_route('/users/', user_resources.UserListResource())
app.add_route('/users/{user_id}/', user_resources.UserDetailResource())


if __name__ == '__main__':
    addr, port = '127.0.0.1', 8000
    print('Starting server on http://{}:{}'.format(addr, port))

    httpd = simple_server.make_server(addr, port, app)
    httpd.serve_forever()
