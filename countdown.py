#!/usr/bin/env python

import argparse
import sys
import time

ARGS = argparse.Namespace()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('time', type=float)
    parser.parse_args(namespace=ARGS)

def main():
    parse_args()
    end_time = time.time() + ARGS.time
    while True:
        now = time.time()
        if now > end_time:
            break
        sys.stdout.write('%8.1f\r' % (end_time - now))
        sys.stdout.flush()
        time.sleep(0.1)

if __name__ == '__main__':
    main()
