import argparse, os
from lib.Zippshare import Zippyshare

parser = argparse.ArgumentParser(description='Zippshare downloader.')
parser.add_argument('-l', '--list', help="File containing a list of zipshare urls", required=True)
parser.add_argument('-o', '--output', help="The downloaded folder",default="./output")

if __name__ == '__main__':
	args = parser.parse_args()
	zipPy = Zippyshare()
	with open(args.list, 'r') as f:
		urls = f.read().splitlines()
		zipPy.download(*urls, output=args.output)
		print("The Downloaded Folder: {}".format(os.path.realpath(args.output)))
	