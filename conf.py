import os
import miio

IP = os.getenv('IP', '')
TOKEN = os.getenv('TOKEN', '')
whitelist = os.getenv('TRUE_ID', "")

robot_cleaner = miio.Vacuum(IP, TOKEN)

