# PI THEREMIN SONIC PI SCRIPT
# CREATED BY JOSIAH ANYINSAH-BONDZIE
# STUDENT ID: 8624637
#---------------------------------------------------------------
use_osc "127.0.0.1", 8000 # Detect local python mesasges on port 8000

pitch = 50
volume = 0.5
#---------------------------------------------------------------
# Listens for x, y values of left and right hand from python.
live_loop :listen_on_osc do
  use_real_time
  co_ordinate = sync "/osc/hand_location"
  l_hand_x = co_ordinate[0]
  l_hand_y = co_ordinate[1]
  r_hand_x = co_ordinate[2]
  r_hand_y = co_ordinate[3]
  #---------------------------------------------------------------
  # Sets the range of pitch between values 40 and 80 and then determines 0 as the minimum and 1 as the maximum.
  pitch_range = range(30..90)
  pitch = map(l_hand_y, 0, 1, pitch_range.min, pitch_range.max)
  
  # Same thing has pitch above but done for volume on the right hand instead.
  volume_range = range(0..1)
  volume = map(r_hand_y, 0.2, 1, volume_range.min, volume_range.max)
end
#---------------------------------------------------------------
# Updates the pitch and volume values based on hand positions received

live_loop :sine_wave do
  use_synth :subpulse
  play pitch, amp: volume
  sleep 0.1
end
