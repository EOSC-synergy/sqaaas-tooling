#!/usr/bin/python3

import argparse
import json
import requests
from pathlib import Path


# HTTP methods
HTTP_METHODS = [
    'POST',
    'PUT',
    'GET'
]
# Follows GitHub supported markup languages
# -- https://github.com/github/markup/blob/master/README.md#markups
AVAILABLE_HEADERS = [
    'application/json'
]
# Ordered list of possible file locations
LOCATIONS = [
    '.',
    'docs',
    '.github'
]


def get_input_args():
    parser = argparse.ArgumentParser(description=(
        'Prepare requests for FAIR assessment tool'
    ))
    parser.add_argument(
        '-H',
        metavar='HEADER',
        type=str,
        choices=AVAILABLE_HEADERS,
        help='Header for the HTTP request'
    )
    parser.add_argument(
        '-X',
        metavar='METHOD',
        choices=HTTP_METHODS,
        type=str,
        help='HTTP method'
    )
    parser.add_argument(
        '-d',
        metavar='DATA',
        type=json.loads,
        help='Data to submit in HTTP request (dict: {id: item_id, repo: oai-pmh, oai_base: oai_endpoint, lang: ES})'
        )
    parser.add_argument(
        '--tool_endpoint',
        metavar='ENDPOINT',
        type=str,
        help='Enpoint to perform HTTP request. Example: http://localhost:9090/v1.0/rda/rda_all'
    )
    
    return parser.parse_args()


def main():
    args = get_input_args()
    url = args.tool_endpoint
    headers = {'Content-type': args.H}
    data = args.d
    if args.X == 'POST':
        r = requests.post(url,data=json.dumps(data), headers=headers)
    elif args.X == 'PUT':
        r = requests.put(url,data=json.dumps(data), headers=headers)
    else:
        r = requests.get(url,data=json.dumps(data), headers=headers)
    return json.dumps(r.text)

print(main())
