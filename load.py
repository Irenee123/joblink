import time
import sys


def loading(seconds):
    for _ in range(seconds):
        sys.stdout.write('\033[1;31m.\033[0m')
        sys.stdout.flush()  # Flush the buffer to ensure it's printed immediately
        time.sleep(0.2)  # Wait for 0.2 second


def load():
    # Number of seconds for the loading effect
    num_seconds = 10
    print("\n\n\033[1m\033[31mWait This Takes Few Minutes To Load", end="")
    # Call the loading function
    loading(num_seconds)
    print("\033[1m\033[31m100%\033[0m",end="\n\n")
    time.sleep(0.2)


def home_load():
    # Number of seconds for the loading effect
    num_seconds = 20
    print("\n\n\033[1m\033[31mWait This Takes Few Minutes To Load", end="")
    # Call the loading function
    loading(num_seconds)
    print("\033[1m\033[31m100%\033[0m",end="\n\n")
    time.sleep(1.5)
