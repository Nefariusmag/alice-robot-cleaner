import os
import miio

IP = os.getenv('IP', '')
TOKEN = os.getenv('TOKEN', '')

robot_cleaner = miio.vacuum.Vacuum(IP, TOKEN)
