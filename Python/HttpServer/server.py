from http.server import HTTPServer, SimpleHTTPRequestHandler

address = ('localhost', 8080)
server = HTTPServer(address, SimpleHTTPRequestHandler)
print('serving at {0}:{1}'.format(address[0], address[1]))
server.serve_forever()