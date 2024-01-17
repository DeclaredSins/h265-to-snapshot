import asyncio
import ffmpeg
import json
import os
from httphandler import *
from http.server import HTTPServer
import threading

config = open("config.json")
data = json.load(config)

def converttoimage():
    if not os.path.exists(os.getcwd()+"/images"):
        os.makedirs(os.getcwd()+"/images")

    for i in data["camera"]:
        outfile = os.getcwd() + "/images" + '/' + i["output"]
        {
            ffmpeg
            .input(i["url"]) 
            # ss convert from frame 50, syntax = frame number / fps
            .output(outfile, vframes=1, ss=5)
            .run(overwrite_output=True)
        }

async def every(__seconds: float, func, *args):
    while True:
        func(*args)
        await asyncio.sleep(__seconds)
        
def startwebserver():    
    webServer = HTTPServer(('', 8080), httphandler)
    print("Server started http://%s:%s" % ('', "8080"))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

if __name__ == '__main__':
    threading.Thread(target=startwebserver).start()
    a = asyncio.get_event_loop()
    a.create_task(every(20, converttoimage)) # run every 20 seconds
    a.run_forever()
