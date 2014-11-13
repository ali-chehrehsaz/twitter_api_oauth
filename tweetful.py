import authorization

import json
import requests

from urls import *

import argparse
import sys


def make_parser():
	"""Constructs the command line parser"""
	description = "gets the API feature to access"

	parser = argparse.ArgumentParser(description=description)

	subparsers = parser.add_subparsers(dest="API_feature", help="Available features")

	#subparser for TIMELINE
	timeline_parser = subparsers.add_parser("TIMELINE", help="return JSON for user timeline")

	#subparser for FRIEND_ID
	friend_id_parser = subparsers.add_parser("FRIEND_ID", help="return JSON for user's friend ID")

	#subparser for FRIEND_LIST
	firend_list_parser = subparsers.add_parser("FRIEND_LIST", help="returns JSON for user's friend list")

	return parser


def main():
    """ Main function """

    parser = make_parser()
    arguments = parser.parse_args(sys.argv[1:])
    #convert parsed arguments from Namespace to dictionatry
    arguments = vars(arguments)
    api_feature = arguments.pop("API_feature")

    auth = authorization.authorize()

    if api_feature == "TIMELINE":
        response = requests.get(TIMELINE_URL, auth=auth)
        print json.dumps(response.json(), indent=4)

    if api_feature == "FRIEND_ID":
        response = requests.get(FRIEND_ID_URL, auth=auth)
        print json.dumps(response.json(), indent=4)

    if api_feature == "FRIEND_LIST":
    	response = requests.get(FRIEND_LIST_URL, auth=auth)
    	print json.dumps(response.json(), indent=4)


if __name__ == "__main__":
    main()