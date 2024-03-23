import http.server
import socketserver
import os

PORT = 8004

Handler = http.server.SimpleHTTPRequestHandler
os.chdir("../build")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at http://localhost:" + str(PORT))
    httpd.serve_forever()
