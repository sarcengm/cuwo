
""" King of the hill script by Sarcen """

# How frequent xp is given out and
# How frequent is check if players are within the radius
tick_frequency = 5.0

# How much gold is dropped on the ground every tick, defualt = 0
# Causes a bit of chatspam or clutter if nobody picks it up
copper_per_tick = 0

# How much xp everyone within the hill radius receives every tick
xp_per_tick = 2

# How much xp the king of the hill gets on top of xp_per_tick
king_xp_bonus = 10

# How often players get rewards
# players get points based on wether they are king or not, points are
# calculated from these durations, points are not reset when they are
# outside of the hill area
reward_frequency = 300
king_reward_frequency = 1