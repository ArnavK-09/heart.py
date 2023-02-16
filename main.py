# imports
from tkinter import messagebox
import sys

# heart program
import heart

# ask prompt
start = messagebox.askyesno("Heart Program", "Should I start making heart in turtle or no?")

# start or exit
if start:
    # log
    print("Programme Started...\n")
    
    # start
    heart.main("This Heart Is For You! Enjoy!")
else:
    # log
    print("Exitting...")
    
    # exit
    sys.exit()
