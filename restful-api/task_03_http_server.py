from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):
    """
    Subclass BaseHTTPRequestHandler
    """

    def do_GET(self):
        """
        Method to handle GET requests
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode())

        elif self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            json_data = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(json_data)
            self.wfile.write(json_string.encode('utf-8'))  # Encode string to bytes
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), MyHandler)
    print("Web server started at localhost:8000")
    server.serve_forever()
