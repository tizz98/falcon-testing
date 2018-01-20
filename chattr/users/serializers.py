import serpy


class UserSerializer(serpy.Serializer):
    id = serpy.StrField()
    first_name = serpy.StrField()
    last_name = serpy.StrField()
    email = serpy.StrField()
