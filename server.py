
from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('0.0.0.0', 5000)
    httpd = server_class(server_address, handler_class)
    print("Server running at http://0.0.0.0:5000/")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
