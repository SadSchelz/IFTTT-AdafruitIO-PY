import os, time
from Adafruit_IO import Client

broker_addr = "io.adafruit.com"  ## This is the broker for Adafruit
broker_port = 1883              ## The port that Adafruit use 
username = ""                    ## Your Adafruit account username
user_key = ""                   ## Your Adafruit user key
pc_mac = ""                     ## MAC for the pc you want to wake

aio = Client(username, user_key)
digital = aio.feeds("turnon")           ## Feed for toggler

while 1:
    data = aio.receive(digital.key)
    if int(data.value) == 1:
        aio.send_data(digital.key, 0)               ## Here we set it back off cause it will stay on :(
        os.system(f"wakeonlan {pc_mac}")            ## Here recreate a sys command for WoL
        break
    time.sleep(0.01)