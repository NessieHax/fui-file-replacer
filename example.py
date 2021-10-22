#!/usr/bin/python3

from uGecko.uGecko import uGecko
from fuiHeader import fuiHeader
from fuiFileReplacer import replaceFuiFile
import sys


def main():
    with open(sys.argv[1],"rb") as fui: data = fui.read()
    gecko = uGecko(sys.argv[2])
    gecko.connect()
    replaceFuiFile(gecko, data)
    gecko.disconnect()

if __name__ == "__main__" and len(sys.argv)>2:
    main()