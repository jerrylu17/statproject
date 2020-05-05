#this function runs a full drive

import numpy as np
import pandas as p

#full drive function takes in a starting state and simulates a full drive that either: ends in a "touchdown"
# worth 7 points, or ends in a loss of possession on downs.

def full_drive(S1):

  is_not_done = True
  k = 0 #this allows us to gracefully kick out of a bad while loop. Not needed in production
  #but in case you miscode something while running a while loop, it's always good to not have to kill the kernel.

  drive_result = {'score':None, 'end_yard':0}
  # drive_result = list(score = NA, end_yard = NA) #we don't really need to declare this here, I'm just being inefficient
  # drive_results [score, end_yard]

  #this is the meat of the drive.  Basically, we either score or run out of downs.  NOthing else.
  while is_not_done:

    y = int(np.random.normal(loc=3, scale=1))
    # y = floor(rnorm(1, mean=3, sd=1)) #how many yards do you gain.  This is a silly way to sample yards.  Should
    #definitely be replaced with a smarter sampling function, and one that is
    #estimated from the data!

    #print current state
    print_status(S1, y)

    # A = yards remaining in down
    # B = down counter
    # C = yards remaining to goal
    B_new = S1[1] + 1
    C_new = S1[2] - y
    A_new = S1[0] - y
    if(A_new <= 0):
        B_new = 1
        A_new = 10
    else:
        B_new = S1[1] + 1
    if C_new <= 0: # c_new == 0 means reach goal (score)
        is_not_done = False
        drive_result['score'] = 7
        break
    elif B_new >= 5: #bnew==turnoveronddowns
        is_not_done = False
        drive_result['end_yard'] = C_new
        turnover_on_downs_print_status(C_new)
        break
    else:
        k = k+1
        S1[0] = A_new
        S1[1] = B_new
        S1[2] = C_new
        print(S1)
    if k > 100:
        is_not_done = False
        drive_result['end_yard'] = C_new
        break

  return drive_result #return drive result which is (score, end_yard).  One of those will always be NA.


#helper function that prints current state in pretty way
def print_status(S1, y):
    if S1[2] > 50:
        print("YTG: ", S1[0], " Down: ", S1[1], " LOS: own ", 100-S1[2], " Yards gained: ", y) #the states are not saved!
    elif S1[2] == 50:
        print("YTG: ", S1[0], " Down: ", S1[1], " LOS: ", S1[2], " Yards gained: ", y)
    elif S1[2] < 50 and S1[2] > 20:
        print("YTG: ", S1[0], " Down: ", S1[1], " LOS: opponent's ", S1[2], " Yards gained: ", y)
    else:
        print("RED ZONE ALERT!!! YTG: ", S1[0], " Down: ", S1[1], " LOS: opponent's ", S1[2], " Yards gained: ", y)

def turnover_on_downs_print_status(y):
  #y is in terms of your team's last possession.  So to get it in terms of your opponents position
  #we need to take 100-y
  x = 100 - y
  s1 = "Sorry, you have lost possession on downs.  Your opponent gets the ball on "
  s2 = "their own " + str(100-x)
  s3 = " yard line."
  if x == 50:
      s2 = "the 50"
  elif x < 50:
      s2 = "your " + str(x)
  return s1 + s2 + s3
