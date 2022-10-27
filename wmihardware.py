import platform


print (f"Architecture: {platform.architecture()}")
print(f"Platform processor:', {platform.processor()}")
print (f"Network name: {platform.node()}")
print (f"Operating System: {platform.platform()}")
print(f"Machine type: {platform.machine()}")
print(f"Python build no. and date: {platform.python_build()}")
print(f"Python compiler:', {platform.python_compiler()}")
