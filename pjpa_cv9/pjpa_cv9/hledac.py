import argparse
import re

parser = argparse.ArgumentParser(description='Uloha pro devaty ukol.')
parser.add_argument('-f', '--filename', dest='file')
parser.add_argument('-s', '--search', dest='search', nargs='+')

args = parser.parse_args()

if args.search is not None:
    searches=args.search
    f=open(args.file)
    text=f.read()
    f.close()
    lines=text.splitlines()
    ar=[0]*lines.__len__()
    for s in searches:
        i=0
        for l in lines:
            reg=re.search(s, l)
            if (reg != None):
                ar[i]+=1
            i+=1
    i=0
    for x in ar:
        if (x==searches.__len__()):
            output=str(i+1)+":"+lines[i]
            print(output)
        i+=1
elif args.search is None and args.file is not None:
    f=open(args.file)
    text=f.read()
    f.close()
    lines=text.splitlines()
    i=1
    for l in lines:
        output=str(i)+":"+l
        print(output)
        i+=1
else:
    parser.print_help()
