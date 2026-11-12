import os
from http.server import BaseHTTPRequestHandler, HTTPServer

TARGET = (
    "https://www.rodicconsultants.com/_next/image"
    "?url=https%3A%2F%2Fd1vah4ferpk10z.cloudfront.net%2F"
    "discover_rodic_img1_de53174aec.webp&w=2048&q=100"
)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)
        self.send_header("Location", TARGET)
        self.end_headers()

    def do_HEAD(self):
        self.do_GET()

    def log_message(self, format, *args):
        print(f"Redirected: {self.path}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print(f"Server running on port {port}")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
