import http.server
import socketserver
import os

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            return self.list_directory(path)
        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(404, "File not found")
            return None
        try:
            self.send_response(200)
            self.send_header("Content-type", self.guess_type(path))
            self.send_header("Cache-Control", "no-store, must-revalidate")
            self.send_header("Pragma", "no-cache")
            self.send_header("Expires", "0")
            self.end_headers()
            return f
        except:
            f.close()
            raise

PORT = 8001

Handler = NoCacheHTTPRequestHandler
os.chdir("../docs")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at http://localhost:" + str(PORT))
    httpd.serve_forever()