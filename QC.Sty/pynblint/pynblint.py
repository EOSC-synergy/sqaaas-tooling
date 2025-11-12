#!/usr/bin/env python
import json
import os
import sys

#parameters
max_warnings=3 #max number of warnings per file before failure


path=os.getcwd()
print(path,os.listdir())
with open('ls.txt','r') as file:
   base_file_list = file.read().splitlines()

actual_file_list= os.listdir()

final_file_list=list(set(actual_file_list)-set(base_file_list))


path=final_file_list[0]

#print (final_file_list)

#print('pynblint ' + path + ' -o report.json -S -q -y')

os.system('pynblint ' + path + ' -o report.json -S -q -y') 
with open('report.json','r') as file:
   data = json.load(file)
   

results={}
def evaluate_json_out(lints):
    
    passed = True
    warnings_counter = 0 
    passed_list = []
    failed_list = []
    passed_reasons_list = []
    failed_reasons_list = []
    
    for lint in lints:
       notebook_name = lint['notebook_metadata']['notebook_name']
       #print(lint.keys())
       #print(lint['notebook_metadata'])
       #print (len(lint['lints']))
       warnings_counter += len(lint['lints'])
       if len(lint['lints'])>max_warnings:
          #print(lint['lints'])
          failed_list.append(notebook_name)
          failed_reasons_list.append({notebook_name:lint['lints']})
       else:
          
          passed_list.append(notebook_name)
          passed_reasons_list.append({notebook_name:lint['lints']})
    
    if warnings_counter > len(lints)*max_warnings:
       passed = False   
    results = {
        "result": passed,
        "passed_list": passed_list,
        "failed_list": failed_list,
        "passed_reasons_list": passed_reasons_list,
        "failed_reasons_list": failed_reasons_list      }
    return(json.dumps(results))

res=evaluate_json_out(data['notebook_level_lints'])

print(res)


