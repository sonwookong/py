from http.server import HTTPServer
httpd = HTTPServer(('localhost', 8000), HttpProcessor)
httpd.serve_forever()