from http.server import BaseHTTPRequestHandler
from re import search
import os

class httphandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/images'

        try:
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            path = self.path

            # check for .png
            if search(".png", path) == None:
                path = path + ".png"

            f = open(os.getcwd() + '/images' + path, 'rb')
            self.wfile.write(f.read())
            f.close()
            print("Accessed from " + self.client_address + " to " + path)
        except:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')
