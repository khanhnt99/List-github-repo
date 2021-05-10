import argparse

parser = argparse.ArgumentParser(description='Process some interger.')
parser.add_argument('intergers', metavar='N', type=int, nargs='+', 
                    help='an interger for accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',const=sum, default=min, help='sum the interger')
args = parser.parse_args()
print(args.accumulate(args.intergers))