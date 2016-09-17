from http.server import HTTPServer, CGIHTTPRequestHandler

address = ('localhost', 8080)
server = HTTPServer(address, CGIHTTPRequestHandler)
print('serving at {0}:{1}'.format(address[0], address[1]))
server.serve_forever()