# How to make a countdown using while:
# *Important: divmod: Separate the quotient and the rest and return both.
    # Example: 125/60 = 2 (quotient) and 5 (rest) -->> 2min:5sec
# Timer: specify the format:
    # :02d = Two-digit int format, padded with 0 to the left
    # format() = Apply the format to the number t and 60
# end="\r" : Returns the cursor so that when printing the next line it overwrites the previous one

import time

def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Finished!')


t = input("Enter the time in seconds: ")

countdown(int(t))