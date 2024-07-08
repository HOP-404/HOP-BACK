import os,platform
os.system('git pull')
os.system("clear")
fbd=platform.architecture()[0]
if fbd=="32bit":
    __import__("swag32")
elif fbd=="64bit":
    __import__("hop64")
