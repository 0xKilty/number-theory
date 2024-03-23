import http.server
import socketserver
import shutil
import subprocess
import os
import sys


if len(sys.argv) != 1:
    if sys.argv[1] == "-deploy":
        subprocess.run(["python", "generate_html.py"])
        shutil.rmtree('../docs')
        shutil.copytree('../build/number-theory', '../docs')
else:
    os.chdir("../build")
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving at http://localhost:" + str(PORT) + "/number-theory")
        httpd.serve_forever()
