import os
import asyncio
import ffmpeg
import json

config = open("config.json")
data = json.load(config)

def converttoimage():
    for i in data["camera"]:
        {
            ffmpeg
            .input(i["url"]) 
            .output(i["name"]+".png", vframes=1, ss=5) # ss convert from frame 50, syntax = frame number / fps
            .run()
        }

        filelist=os.listdir()
        for files in filelist[:]: # filelist[:] makes a copy of filelist.
            if (files == i["output"]): # find the old one first
                os.remove(i["output"])
                #os.rename(i["name"]+".png", i["output"])

            if (files == i["name"]+".png"): # incase of creating new file
                os.rename(i["name"]+".png", i["output"]) 

async def every(__seconds: float, func, *args):
    while True:
        func(*args)
        await asyncio.sleep(__seconds)
        
if __name__ == '__main__':
    a = asyncio.get_event_loop()
    a.create_task(every(10, converttoimage)) # run every 10 seconds
    a.run_forever()