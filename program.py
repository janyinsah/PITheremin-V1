#This module aims to generate a tone a different method, by sending messages through
#OSC Messages to Sonic Pi.
                #Created by Josiah Anyinsah-Bondzie
#---------------------------------------------------------
import time
from psonic import *
from client import *
from threading import Thread
import handtrack
#---------------------------------------------------------
#'post' sends the script message to the Sonic PI interface.
post = connect_to_client('127.0.0.1', 4560)
#---------------------------------------------------------


