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
        print(outfile)
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
        
def startwebserver(port, image):    
    webServer = HTTPServer(('', port), httpserver(image))
    print("Server started http://%s:%s" % ('', str(port)))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

if __name__ == '__main__':
    for i in data["camera"]:
        # check for .png
        if ("output" in i["output"].lower() == False):
            i["output"] = i["output"] + ".png"

        new_thread = threading.Thread(target=startwebserver(i["port"], i["output"]))
        new_thread.daemon = True
        new_thread.start()
        #a.create_task(startwebserver(i["port"], i["output"]))   

    print(":tesrt")
    a = asyncio.get_event_loop()
    a.create_task(every(10, converttoimage)) # run every 10 seconds
    a.run_forever()
    print(":tefsrt")