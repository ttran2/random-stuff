#!/usr/bin/python
import sys
from optparse import OptionParser
usage="Usage: %prog [OPTIONS] PATTERN [FILE]"
parser=OptionParser(usage=usage)
parser.add_option("-i","--ignore-case",action="store_true",dest="case",help="ignore case distinctions")
parser.add_option("-v","--invert-match",action="store_true",dest="invert",help="select non-matching lines")
#parser.add_option("-f","-file",dest="file",metavar="FILE",help="obtain PATTERN from FILE")
(opt,args)=parser.parse_args()
try:
    with open(arg[1],"r") as f:
        text = f.read().splitlines()
except:
    text=sys.stdin.read().splitlines()
#if sys.stdin.isatty():#keyboard input
#    with open(args[1],"r") as f:
#        text = f.read().splitlines()
#else:
#    text=sys.stdin.read().splitlines()
for line in text:
    if opt.case:
        s=args[0].lower()
        l=line.lower()
    else:
        s=args[0]
        l=line
    if bool(opt.invert) ^ bool(s in l):
        print line