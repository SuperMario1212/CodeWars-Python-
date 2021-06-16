# --> Instructions <--

# A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.
# He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
# His mother looks out of a window 1.5 meters from the ground.
# How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?

# Three conditions must be met for a valid experiment:
# 1. Float parameter "h" in meters must be greater than 0
# 2. Float parameter "bounce" must be greater than 0 and less than 1
# 3. Float parameter "window" must be less than h.
# *If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

# --> Instruction End <--

def bouncing_ball(h, bounce, window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        # if the ball dropped is higher than the window, then the mother
        # will see the ball at least one, even if the ball does not bounce back
        # to the window height, since the ball starts travel from the top 
        times = 1  
        while (h * bounce) > window:
            # each round the elevation of the ball changes
            # each round the mother will see the ball travels (1 for up and 1 for down)
            # (since the ball went up, it will definitely come down)
            # so 2 times 
            times += 2
            h = h * bounce
        return times
    
    else:
        return -1
