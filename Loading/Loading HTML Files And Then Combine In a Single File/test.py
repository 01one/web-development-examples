from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

PORT = 8000
with HTTPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
