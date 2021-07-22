rsync -zavh * pi@192.168.29.11:~/epaperPoC

ssh pi@192.168.29.11 "cd epaperPoC;raspistill -o out.jpg -w 212 -h 104; sudo python displayOnEpaper.py"