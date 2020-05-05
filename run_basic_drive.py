from run_to_score import run_to_score
from run_full_drive import full_drive

#  states = (A, B, C)

#  Probability breakdown:
#  P(A_{t+1}, B_{t+1}, C_{t+1} | A_t, B_t, C_t)
#          = P(A_{t+1} | C_{t+1}, C_t, A_t)
#              P(B_{t+1} | C_{t+1}, C_t, B_t)
#              P(C_{t+1} | A_t, B_t, C_t)

# A is YTG, B is Downs, C is LOS- ranges from 0 to 100 (so your own 25 would be 75.  0 would be a touchdown)

# Assume that YG comes from the same simple distribution- this is one of the major changes you would want to make!



A=10 # yards til 1st down
B=1 # down counter
C=75 # yards til goal
 #starting state- better: simulate a kickoff, but this will do for now

#now we run our main function.  This function isn't necessarily the one you will use to simulate a game
#eventually, because it's not necessarily the best "unit" to loop over, but it's something for now!
#in the very least, you can use it to work out things like punts, and different kinds of scoring opportunities.

run_to_score([A, B, C])

#to simulate more, you only need to run the function again.  S does not change, so you don't need to
#re run the line that defines S.
