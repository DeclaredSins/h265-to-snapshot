import os
import asyncio
import ffmpeg
import json

config = open("config.json")
data = json.load(config)

def converttoimage():
    filelist=os.listdir()
    for files in filelist[:]: # filelist[:] makes a copy of filelist.
        for i in data["camera"]:
            if (files == i["name"]+".png"): # find the old one first
                os.remove(i["output"])
                os.rename(i["name"]+".png", i["output"])

    for i in data["camera"]:
        {
            ffmpeg
            .input(i["url"]) 
            .output(i["name"]+".png", vframes=1, ss=5) # ss convert from frame 50, syntax = frame number / fps
            .run()
        }

async def every(__seconds: float, func, *args):
    while True:
        func(*args)
        await asyncio.sleep(__seconds)
        
if __name__ == '__main__':
    a = asyncio.get_event_loop()
    a.create_task(every(10, converttoimage)) # run every 10 seconds
    a.run_forever()