#!/usr/bin/env cims_python
import signal
import time
import sys
import os


def handle(sig, frame):
    print('get signal', sig)
    sys.exit(0)


if __name__ == "__main__":
    print(os.getpid())
    signal.signal(signal.SIGQUIT, handle)
    while True:
        time.sleep(1)
