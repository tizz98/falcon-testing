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
