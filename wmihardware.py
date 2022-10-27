import platform
from getmac import get_mac_address as getmac
import socket
#import shutil
import psutil

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print (f"Architecture: {platform.architecture()}")
print(f"Platform processor:', {platform.processor()}")
print (f"Network name: {platform.node()}")
print (f"Operating System: {platform.platform()}")
print(f"Machine type: {platform.machine()}")
print(f"Python build no. and date: {platform.python_build()}")
print(f"Python compiler: {platform.python_compiler()}")
print(f"MAC add: {getmac()}")
print(f"Computer IP Address is:" + IPAddr)
#print(f"Partition D details:", shutil.disk_usage("D:\\"))
totalsize = psutil.disk_usage('D:').total / 2**30
print('Partition D, totalsize: ',totalsize, ' GB')
#MAC add as hex
#print (hex(uuid.getnode()))
