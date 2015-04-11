#!/usr/bin/python

import yaml
import os

SRC_DIR = './src'

result = {}
for subsystem in os.listdir(SRC_DIR):
    data = yaml.load(open('{}/{}'.format(SRC_DIR, subsystem)))

    for function in  data:
        for signal in data[function]:
            ECUs = data[function][signal]
            if (signal not in result):
                result[signal] = {}
            if (subsystem not in result[signal]):
                result[signal][subsystem] = {}
            if (function not in result[signal][subsystem]):
                result[signal][subsystem][function] = {}
                result[signal][subsystem][function]['sender']   = []
                result[signal][subsystem][function]['receiver'] = []
            result[signal][subsystem][function]['sender'].append(ECUs[0])
            for receiver in ECUs[1:]:
                result[signal][subsystem][function]['receiver'].append(receiver)

with open ('{}/{}'.format('by-signal', 'generated.yaml'),'wb') as yaml_file :
     yaml.dump(result,yaml_file,default_flow_style=False)

