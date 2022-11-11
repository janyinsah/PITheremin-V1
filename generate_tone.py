# Function which generates tone for the Pi Theremin.
from psonic import *
from client import *

#---------------------------------------------------
# 'post' sends the script message to the Sonic PI interface.

post = connect_to_client()

#---------------------------------------------------
#test python-sonic api by sending a note the DAW server interface.
notes  = play(70)
post.send_message("/osc/generate_tone", notes)














        

