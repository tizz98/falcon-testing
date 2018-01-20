import falcon

from chattr.common.http import get_object_or_404
from chattr.users.models import User
from chattr.users.serializers import UserSerializer


class UserListResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        users = UserSerializer(User.all(), many=True).data
        resp.media = {
            'users': users,
            'count': len(users),
        }

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        user = User.create(**req.media)
        resp.media = {'user': UserSerializer(user).data}


class UserDetailResource:
    def on_get(self, req: falcon.Request, resp: falcon.Response, user_id):
        user = get_object_or_404(User, id=user_id)
        resp.media = {'user': UserSerializer(user).data}
