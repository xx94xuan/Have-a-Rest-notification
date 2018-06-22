#!/usr/bin/env python

import os
import threading 

title = "Have a Rest Now"
text = ":) Time to stand up and have a walk now ~"
#time_range = 60.0 * 60.0 * 2 # 2 hours
time_range = 10.0 #10 seconds for test

def let_sleep():
    threading.Timer(time_range, let_sleep).start()
    display_command = "display notification \"%s\" with title \"%s\" sound name \"Frog.aif\""%(text, title)
    os.system("osascript -e \'%s\'"%display_command)

def main():
    let_sleep()

main()
