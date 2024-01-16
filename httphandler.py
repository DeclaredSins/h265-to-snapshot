from http.server import BaseHTTPRequestHandler
from main import data
import os

class httphandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/images'

        try:
            self.send_response(200)
            self.send_header("Content-type", "image/png")
            self.end_headers()
            for i in data["camera"]:
                # check for .png
                if ("output" in i["output"].lower() == False):
                    i["output"] = i["output"] + ".png"
                    f = open(os.getcwd() + '/images' + '/' + i["output"], 'rb')
                    self.wfile.write(f.read())
                    f.close()
        except:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')
