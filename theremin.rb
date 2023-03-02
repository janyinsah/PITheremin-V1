# Welcome to Sonic Pi
live_loop :listen do
  set_sched_ahead_time! 0.1
  message = sync "/play_this"
end
