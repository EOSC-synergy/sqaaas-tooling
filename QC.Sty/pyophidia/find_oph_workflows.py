from PyOphidia import client
import os
import json
import argparse


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


def evaluate_workflow(candidates):
    ophclient = client.Client(
        username="oph-user", password="oph-passwd", local_mode=True
    )
    passed = 0
    passed_list = []
    failed_list = []
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


def main():

    args = get_input_args()
    candid = find(".json", args.path)
    res = evaluate_workflow(candid)
    return json.dumps(res)


print(main())
