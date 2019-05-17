import os
import miio

IP = os.getenv('IP', '192.168.1.14')
TOKEN = os.getenv('TOKEN', '')


status = miio.vacuum.VacuumStatus.battery
print(status)
# def home(IP, TOKEN):
#     os.system(f"mirobo --ip {IP} --token {TOKEN} home")
#
#
# def pause(IP, TOKEN):
#     os.system(f"mirobo --ip {IP} --token {TOKEN} pause")
#
#
# def start(IP, TOKEN):
#     os.system(f"mirobo --ip {IP} --token {TOKEN} start")
#
#
# def stop(IP, TOKEN):
#     os.system(f"mirobo --ip {IP} --token {TOKEN} stop")


