# Function which generates tone for the Pi Theremin.
import time
from psonic import *
from client import *

#---------------------------------------------------
# 'post' sends the script message to the Sonic PI interface.

post = connect_to_client()

#---------------------------------------------------
#test python-sonic api by sending a note the DAW server interface.
while True:
    n = play(60)
    post.send_message('/trigger/tone', n)
    sleep(0.5)














        

