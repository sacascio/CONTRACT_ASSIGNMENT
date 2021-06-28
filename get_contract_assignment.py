#!/usr/bin/env python3
import json
import logging
import sys
import os
import argparse


class ACI:
	# __init__ is the constructor
	def __init__(self,fn):

		self.filename = fn
		logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

		if not os.path.isfile(self.filename):
			logging.error(" File %s not found" % filename)
			sys.exit(9)

		# Build headers for the CSV
		f = open("contract_assignment.csv", "a")
		f.write("EPG,NAME,TYPE" + "\n")
		f.close()

	def load_file(self):
		with open(self.filename) as json_file:
			data = json.load(json_file)

		return data

	def print_contract_data(self,data):
		for d in data['polUni']['children']:
			for keys in d.keys():
				if keys == 'fvTenant':
					tenant = d[keys]['attributes']['name']
					


	def build_virtual_device_6a(self,short_tenant,vrf,vmmd):
		f = open("PBR_CSV/6a.csv", "a")
		f.write("TNT_SWP_" + short_tenant + "," + "SVD_" + short_tenant + "_PFW_" + vrf + "," + vmmd + "\n")
		f.close()


def read_arguments():
	parser = argparse.ArgumentParser(sys.argv[0] + " -f <ACI JSON File>")
	parser.add_argument("-f", "--input-file", dest="filename" , help="JSON From Backup File", required=True)
	args = parser.parse_args()
	return args

def main():
	args = read_arguments()
	data = ACI(args.filename)
	json_data = data.load_file()

	data.print_contract_data(json_data)
if __name__ == '__main__':
	main()