#!/usr/bin/python3

import argparse
import json
import requests
import sys


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
        default='http://localhost:9090/v1.0/rda/rda_all',
        help=(
            'Enpoint to perform HTTP request. Example: '
            'http://localhost:9090/v1.0/rda/rda_all'
        )
    )

    return parser.parse_args()


def is_api_up(url):
    s = requests.Session()
    retries = requests.adapters.Retry(
        total=5,
        backoff_factor=0.4,
        status_forcelist=[ 500, 502, 503, 504 ]
    )
    s.mount('http://', requests.adapters.HTTPAdapter(max_retries=retries))

    response = None
    try:
        response = s.get(url)
    except requests.exceptions.ConnectionError:
        pass

    return response


def main():
    args = get_input_args()
    url = args.tool_endpoint

    healthcheck_url = 'http://localhost:9090/v1.0/rda'
    if not is_api_up(healthcheck_url):
        print(
            'Maximum retries reached when attempting to connect '
            'to FAIR_EVA API: %s' % healthcheck_url
        )
        sys.exit(-1)

    headers = {'Content-Type': 'application/json'}
    data = {
        "id": args.ID,
        "repo": args.R,
        "oai_base": args.B,
        "lang": "ES"
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return json.dumps(r.json())


print(main())
