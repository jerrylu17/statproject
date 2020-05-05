# PLAYID = play id obviously
# PLAYENDFIELDPOSITION = field position at the end of the play
# FIELDPOSITION = field position (use -1 * FP + 50 to calculate yard to goal)
# DOWN = down obviously
# GAINLOSS = gain or loss of play
# DISTANCE = distance to 1st down or goal line
# RUNPASS = R if run P if pass; X if flag presnap; null if special teams

# DRIVEENDEVENT = result of drive


'''
first thing we'll analyze is between the following plays: run, pass, kick (punt)
reward calculation based on DRIVEENDEVENT (only this for now)
'''
