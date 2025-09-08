from pyophidia import Experiment
import json
import argparse
import urllib
import os
import ast
import pyophidia

#function to find files
def find(
    pattern,
    path,
):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if pattern in name:
                result.append(os.path.join(root, name))
    return result


def get_input_args():
    parser = argparse.ArgumentParser(description=("Find Ophidia workflows"))
    parser.add_argument(
        "--path",
        metavar="PATH",
        type=str,
        help="path to look for in the repository",
        default=".",
    )
    parser.add_argument(
        "--args_path",
        metavar="ARGS_PATH",
        type=str,
        help='path to json containing  dict formed by the list of args using filename as a key for each list Example {"filename":["1","historic"]} ',
    )
    return parser.parse_args()

#function to evaluate list of paths to workflow files
def evaluate_workflow_path(candidates, arguments={"filename": ["1", "historic"]}):
    # Create the experiment that will validate
    ophexperiment = Experiment(
        name="validation", author="user", abstract="validation test"
    )


    if arguments != {"filename": ["1", "historic"]}:
        with open(arguments, "r") as arg_file:
            arguments = json.load(arg_file)
    # Create results lists and default values
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
    for workflow in candidates:
        res=False
        msg=''
          
        filename = os.path.basename(workflow)
        extension = os.path.splitext(filename)[1]
        direc= os.path.dirname(workflow)
        
        #exclude 
        if 'lib' in direc or 'utils'in direc :
            continue
        
        try:

            argument = arguments[filename]

        except:
            argument = ["1", "historic"]
        if extension == '.cwl':
          
          
          
           
          if not (os.path.islink(direc+'/tasks')):
            os.system('ln -s /home/palomo/PyOphidia/pyophidia/utils/tasks '+direc)  
          try:
              work=ophexperiment.load_cwl(workflow,"--nthreads 1 --lon_file lon_file.nc --container wind --lat_range 0:70 --space_range 0:70|100:320 --number_of_files 1 --query_on_files *_201*.nc --output_variable1 msl --output_variable2 vo_850")
              
              res=work.check(display=False)
              
          except:
            
            res=False
            msg="Error while evaluating"
               
              
          
          
          if not res and msg=='':
            
            msg=('.cwl file  did not pass the structure test')
        else:
            
            #if not (os.path.islink(direc+'/tasks')):
                #os.system('ln -s /home/palomo/PyOphidia/pyophidia/utils/tasks '+direc)
          
            try:

              res, msg = ophexperiment.validate(workflow, *argument)
              
            except:
              res = False
              msg = "Not readable workflow"
       
        if res:
            passed = True
            passed_list.append(workflow)
        else:
            failed_list.append(workflow)
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
        candid_json = find(".json", args.path)
        candid_cwl= find(".cwl", args.path)
        candid = candid_json + candid_cwl
        
    # evaluate  files
    if args.args_path:
        res = evaluate_workflow_path(candid, args.args_path)
    else:
            
        res = evaluate_workflow_path(
            candid,
        )
         
    return json.dumps(res)


print(main())
