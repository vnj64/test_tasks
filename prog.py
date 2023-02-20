# 1. Напишите systemd файл запуска сервиса /etc/systemd/system/myservice.service запускающий python программу /home/my/prog.py

import time
from datetime import datetime

while True:
    with open("timestamp.txt", "a") as f:
        f.write("Текущая временная метка: " + str(datetime.now()))
        f.close()
    time.sleep(10)
