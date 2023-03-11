# PI THEREMIN SONIC PI SCRIPT
# CREATED BY JOSIAH ANYINSAH-BONDZIE
# STUDENT ID: 8624637
#---------------------------------------------------------------
use_osc "127.0.0.1", 8000

define :continuous_sine_wave do
  pitch = args[0]
  amp = args[1]
  use_synth :sine 
  play pitch, amp: volume
end


live_loop :listen_on_osc do
  sync "/osc/synth"
  args = sync "/osc/snyth"
end
