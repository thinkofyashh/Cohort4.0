import argparse


parser=argparse.ArgumentParser()

parser.add_argument("--name",default="Raju")
parser.add_argument("--city",default="Delhi")

args=parser.parse_args()

print(args.name)
print(args.city)


