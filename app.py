from wsgiref import simple_server

from chattr.api import app


if __name__ == '__main__':
    addr, port = '127.0.0.1', 8000
    print('Starting server on http://{}:{}'.format(addr, port))

    httpd = simple_server.make_server(addr, port, app)
    httpd.serve_forever()
