# h265-to-snapshot
As the name implies, this project aims to convert h265 RTSP stream to snapshot. It was not created for converting video to snapshot but instead a RTSP stream. It converts video to snapshot and display on the web so you can easily use it with your camera.

## Using with Scrypted
Scrypted does not support converting prebuffer video to snapshot with h265, all you will get is a gray snapshot but the video will work as expected when you enable transcoding. 
To use h265-to-snapshot with Scrypted, simply edit the config to get the stream from Scrypted and points it to your snapshot url. This will make h265 camera works with snapshot.

## How to install
**Make sure to edit config before you start!**
```
sudo apt update
sudo apt install git ffmpeg python3-pip
git clone https://github.com/DeclaredSins/h265-to-snapshot.git
cd h265-to-snapshot
pip install -r requirements.txt --break-system-packages
python3 main.py
```
The web server is now reachable via http://yourip:8080/example.png -- change example.png to whatever output you set in your config.
