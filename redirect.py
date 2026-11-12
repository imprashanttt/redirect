from http.server import BaseHTTPRequestHandler, HTTPServer

TARGET = (
    "https://www.rodicconsultants.com/_next/image"
    "?url=https%3A%2F%2Fd1vah4ferpk10z.cloudfront.net%2F"
    "discover_rodic_img1_de53174aec.webp&w=2048&q=100"
)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(301)  # 301 = permanent redirect
        self.send_header("Location", TARGET)
        self.end_headers()

    def log_message(self, format, *args):
        print(f"Redirected: {self.path}")

if __name__ == "__main__":
    print("Server running at http://127.0.0.1:5000")
    HTTPServer(("127.0.0.1", 5000), Handler).serve_forever()
