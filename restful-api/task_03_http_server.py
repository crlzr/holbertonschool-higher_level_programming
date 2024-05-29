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
        if self.path == "/data":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            json_data = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(json_data)
            self.wfile.write(json_string)
        else:
            self.send_response(404)
            self.end_headers()
