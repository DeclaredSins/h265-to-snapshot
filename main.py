import asyncio
import ffmpeg
import json
import os

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
        
if __name__ == '__main__':
    a = asyncio.get_event_loop()
    a.create_task(every(10, converttoimage)) # run every 10 seconds
    a.run_forever()