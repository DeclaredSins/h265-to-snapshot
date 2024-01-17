# h265-to-snapshot
As the name implies, this project aims to convert h265 rtsp stream to snapshot. It was not created for converting video to snapshot but instead a rtsp stream. It converts video to snapshot and display on the web so you can easily use it with your camera.

## Using with Scrypted
Scrypted does not support converting prebuffer video to snapshot with h265. All you will get is a gray snapshot but the video will work as expected when you enable transcode. 
To use h265-to-snapshot with Scrypted, simply edit the config to get the stream from Scrypted and points it to your snapshot url. This will make h265 camera works with snapshot.

## How to install
**Make sure to edit config before you start!**
```
sudo apt update
sudo apt install git ffmpeg python3-pip
git clone https://github.com/DeclaredSins/h265-to-snapshot.git
cd h265-to-snapshot
pip install requirements.txt
python3 main.py
