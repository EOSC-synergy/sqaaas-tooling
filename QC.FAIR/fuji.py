#!/usr/bin/python3

import argparse
import json
import requests


def get_input_args():
    parser = argparse.ArgumentParser(description=(
        'Prepare requests for FAIR assessment tool'
    ))
    parser.add_argument(
        '-OID',
        metavar='object_identifier',
        type=str,
        help='Object Persistent Identifier. I.e.: DOI, Handle, LandingPage '
             'URL, etc.',
        required=True
    )
    parser.add_argument(
        '--tool_endpoint',
        metavar='tool_endpoint',
        type=str,
        help='Tool endpoint to perform HTTP request. Example: '
             'http://localhost:1071/fuji/api/v1/evaluate',
        required=True
    )
    parser.add_argument(
        '-T',
        metavar='metadata_service_type',
        choices=['oai_pmh', 'sparql', 'ogc_csw'],
        type=str,
        help='Type of the Metadata service. One of: "oai_pmh", "sparql" or '
             '"ogc_csw".'
    )
    parser.add_argument(
        '-E',
        metavar='metadata_service_endpoint',
        type=str,
        help='Metadata service endpoint URL.'
    )
    return parser.parse_args()


def main():
    args = get_input_args()
    url = args.tool_endpoint
    headers = {'Content-Type': 'application/json'}
    data = {
        "object_identifier": args.OID,
        "metadata_service_endpoint": args.E,
        "metadata_service_type": args.T,
        "test_debug": True,
        "use_datacite": True
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return json.dumps(r.text)


print(main())
