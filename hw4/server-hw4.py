# Sooji Kim
# CS5700 Fall25
# HW 4
# 14 September 2025

# Server for serving an html and json file to clients

from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import mimetypes

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve HTML or JSON content based on the requested resource
        if mimetypes.guess_type(self.path)[0] == "text/html":
            try:
                '''
                Insert your code here.    
                '''
                resource = self.path.lstrip("/")
                with open(resource, "rb") as f:
                    body = f.read()
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.send_header("Content-length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except FileNotFoundError:
                '''Insert your code here'''
                self.send_error(404, f"File Not Found: {self.path.lstrip('/')}")
        elif mimetypes.guess_type(self.path)[0] == "application/json":
            try:
                '''
                Insert your code here.    
                '''
                resource = self.path.lstrip("/")
                with open(resource, "rb") as f:
                    body = json.load(f)
                body = json.dumps(body).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.send_header("Content-length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
            except FileNotFoundError:
                '''Insert your code here'''
                self.send_error(404, f"File Not Found: {self.path.lstrip('/')}")
        else:
            # Handle unsupported content type
            '''
            Insert your code here.    
            '''
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found - Unsupported Content Type")
            '''
            Insert your code here.    
            '''

# Server setup
port = 8070
server_address = ('', port)
httpd = HTTPServer(server_address, MyHandler)

print(f"Serving on port {port}")
httpd.serve_forever()