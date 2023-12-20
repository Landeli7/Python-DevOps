import os
import psutil

print("CPU usage: ", str(psutil.cpu_percent()) + "%")
print("Memory usage: ", str(psutil.disk_usage('/').percent) + "%")

os.system("df -h")
