import flask_routes as routes
from gevent.pywsgi import WSGIServer

def main():
    HTTP_SERVER = WSGIServer(('',5080), routes.app)
    HTTP_SERVER.serve_forever()

if __name__ == "__main__":
    main()