#!/usr/bin/python3

import argparse
import json
import requests
from pathlib import Path


def get_input_args():
    parser = argparse.ArgumentParser(description=(
        'Prepare requests for FAIR assessment tool'
    ))
    parser.add_argument(
        '-ID',
        metavar='ID',
        type=str,
        help='Persistent Identifier'
    )
    parser.add_argument(
        '-R',
        metavar='PLUGIN',
        type=str,
        help='HTTP method'
    )
    parser.add_argument(
        '-B',
        metavar='OAI-PMH',
        type=str,
        help='OAI-PMH_ENDPOINT'
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
    headers = {'Content-Type':'application/json'}
    data = {
        "id": args.ID,
        "repo": args.R,
        "oai_base": args.B,
        "lang": "ES"
    }
    r = requests.post(url,data=json.dumps(data), headers=headers)
    return r.json()

print(main())
