#!/usr/bin/env python
from pyophidia import client
import json
import argparse
import urllib
import os

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if pattern in name:
                result.append(os.path.join(root, name))
    return result


def get_input_args():
    parser = argparse.ArgumentParser(description=("Find Ophidia workflows"))
    parser.add_argument(
        "--path", metavar="PATH", type=str, help="path to look for in the repository"
    )
    return parser.parse_args()


def evaluate_workflow_path(candidates):
    ophclient = client.Client(
        username="oph-user", password="oph-passwd", local_mode=True
    )
    passed = False
    passed_list = []
    failed_list = []
    results = {
        "result": passed,
        "passed_list": passed_list,
        "failed_list": failed_list,
    }
    for jsons in candidates:
        f = open(str(jsons), "r")
        
        data = json.load(f)
        res, msg = ophclient.wisvalid(data)

        if res:
            passed = True
            passed_list.append(jsons)
        else:
            failed_list.append(jsons)

        results = {
            "result": passed,
            "passed_list": passed_list,
            "failed_list": failed_list,
        }
    return results


def download(url):

    response = urllib.request.urlopen(url)
    text = str(response.read())
    try:

        data = json.loads(text)
    except:
        # This is because its neccesary when downloading from github raw
        exp = bytes(text, "utf-8").decode("unicode_escape")

        data = json.loads(exp[2:-1])

    with open("downloaded_workflow.json", "w") as dwork:
        json.dump(data, dwork)
    pathfile = ["downloaded_workflow.json"]
    return pathfile


def main():

    args = get_input_args()
    is_url = urllib.parse.urlparse(args.path)

    if is_url.scheme == "https" or is_url.scheme == "http":

        candid = download(args.path)
    else:
        candid = find(".json", args.path)

    res = evaluate_workflow_path(candid)
    return json.dumps(res)


print(main())
