#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


def usage():
    print("\n\t$ ./brew2sh Brewfile | sh\n")
    sys.exit(1)


def convert(line):
    if line[0] == "#" or len(line) == 1:
        return line.rstrip()
    else:
        return "brew %s || true" % line.rstrip()


if __name__ == '__main__':
    if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
        usage()

    with open(sys.argv[1]) as f:
        print("#!/bin/sh")
        for line in f:
            print(convert(line))
