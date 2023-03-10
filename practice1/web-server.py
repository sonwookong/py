from http.server import HTTPServer, CGIHTTPRequestHandler


httpd = HTTPServer(('localhost', 8000), CGIHTTPRequestHandler)
httpd.serve_forever()