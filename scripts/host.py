import http.server
import socketserver
import os

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
os.chdir("../docs")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()