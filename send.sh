# rm *.jpg
rsync -zavh * pi@192.168.29.11:~/rpi-epaper-camera

# ssh pi@192.168.29.11 "cd rpi-epaper-camera;raspistill -o out.jpg -w 212 -h 104; sudo python displayOnEpaper.py"
ssh pi@192.168.29.11 "cd rpi-epaper-camera; sudo python displayOnEpaper.py"
# ssh pi@192.168.29.11 "cd rpi-epaper-camera;rm *.jpg; python camera.py"

rsync -zavh pi@192.168.29.11:~/rpi-epaper-camera/*.jpg .