import pandas as p
import numpy as np
from run_full_drive import full_drive
# This function loops and repeatedly calls the function full_drive until someone scores.
# One of the main things this function does is keep track of which team has the ball.
def run_to_score(S1):
  team = 0 # start with team 0 (chosen so that we can work with modular arithmetic)
  k = 0 # again, if there is something crazy we want to kick out of the while loop.  in production time we
  # would prefer this to be a boolean and not a counter, but this will work for now.
  while k<101:
    result_drive = full_drive(S1) #team 0 runs their drive
    if result_drive['score'] != None:
      print("team", team, "scored!") #if they score, this function is done!
      break
    else:
      S1 = [10, 1, 100-result_drive['end_yard']]
      # S = list(A=10, B=1, C=100-result_drive$end_yard) #if they don't score, give the other team the ball
      # where the previous team left off.
      team = (team+1)%2 #this is modular arithmetic. Gives us a graceful way to switch between teams
      k = k+1 #play counter in case things get out of hand.


  #nothing is returned (yet!)
