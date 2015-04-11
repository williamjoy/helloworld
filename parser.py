#!/usr/bin/python

import yaml

data = yaml.load(open('subsystem1.yaml'))

result = {}
for function in  data:
    for signal in data[function]:
        ECUs = data[function][signal]
        if (signal not in result):
            result[signal] = {}
        if (function not in result[signal]):
            result[signal][function] = {}
            result[signal][function]['sender']   = []
            result[signal][function]['receiver'] = []
        result[signal][function]['sender'].append(ECUs[0])
        for receiver in ECUs[1:]:
            result[signal][function]['receiver'].append(receiver)

with open ('{}/{}'.format('by-signal', 'subsystem1.yaml'),'wb') as yaml_file :
     yaml.dump(result,yaml_file,default_flow_style=False)

