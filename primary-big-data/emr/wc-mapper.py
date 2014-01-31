#!/usr/bin/python
import sys
import re

def main(argv):
        print argv
        pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
        print sys
        for line in sys.stdin:
            for word in  pattern.findall(line):
                    print  word.lower() + "\t" + "1"


if __name__ == "__main__":
        print sys.argv
        main(sys.argv)
