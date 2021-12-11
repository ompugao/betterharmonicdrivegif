# better harmonic drive explanation gif

## Usage
```sh
$ pip3 install opencv-python matplotlib numpy
$ wget https://upload.wikimedia.org/wikipedia/commons/2/21/HarmonicDriveAni.gif
$ convert HarmonicDriveAni.gif frame.png
$ python main.py
$ ffmpeg -framerate 30 -i output/frame-%05d.png -vcodec libx264 -pix_fmt yuv420p -r 30 out.mp4
```
