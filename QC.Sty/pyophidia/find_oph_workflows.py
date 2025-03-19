#!/usr/bin/env python
from pyophidia import Experiment
import json
import argparse
import urllib
import os
import ast


def find(pattern, path,):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if pattern in name:
                result.append(os.path.join(root, name))
    return result


def get_input_args():
    parser = argparse.ArgumentParser(description=("Find Ophidia workflows"))
    parser.add_argument(
        "--path", metavar="PATH", type=str, help="path to look for in the repository", default='.'
    )
    parser.add_argument(
        "--args_path", metavar="ARGS_PATH", type=str, help='path to json containing  dict formed by the list of args using filename as a key for each list Example {"filename":["1","historic"]} ',
    )
    return parser.parse_args()


def evaluate_workflow_path(candidates,arguments={"filename":["1","historic"]}):
    # Create the experiment that will validate
    ophexperiment = Experiment(
        name="validation", author="user", abstract="validation test"
    )
    # Create results lists and default values
    #args=[]
    #args.append('1')
    #args.append('historical')
    print(arguments)
    print(type(arguments))
    with open (arguments ,'r') as arg_file:
         arguments=json.load(arg_file)
    #arguments={str(arguments[0]):[arguments[1],arguments[2]]}
    passed = False
    passed_list = []
    failed_list = []
    reasons_list = []
    results = {
        "result": passed,
        "passed_list": passed_list,
        "failed_list": failed_list,
        "reasons_list": reasons_list,
    }
    # Validate all files
    for jsons in candidates:
        filename=os.path.basename(jsons)
        print(os.path.basename(jsons))
        try:
            print('test')
            print (arguments.keys())
            print (arguments)
            argument=arguments[filename]
            print(filename)
            print('conseguido')
        except:
            argument=['1','historic']
        try:
            
            res, msg = ophexperiment.validate(jsons,*argument)
            
        except:
            res = False
            msg = "Not readable workflow"
            
        if res:
            passed = True
            passed_list.append(jsons)
        else:
            failed_list.append(jsons)
            reasons_list.append(msg)

        results = {
            "result": passed,
            "passed_list": passed_list,
            "failed_list": failed_list,
            "reasons_list": reasons_list,
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
    # get input arguments
    args = get_input_args()

    is_url = urllib.parse.urlparse(args.path)
    # see if there is a need to download files
    if is_url.scheme == "https" or is_url.scheme == "http":

        candid = download(args.path)
    else:
        # find all the json files in path
        candid = find(".json", args.path)
    # evaluate  files
    print(args.args_path)
    res = evaluate_workflow_path(candid,args.args_path)
    return json.dumps(res)


print(main())
