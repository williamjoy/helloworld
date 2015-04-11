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

csv_file_all = open('by-signal/generated.csv', 'wb')
csv_file_group_by_sender = open('by-signal/group_by_sender.csv', 'wb')
csv_file_all.write('Signal, Sub System, Function, Sender, Receiver\n')

group_by_sender= {}
for signal in result:
    if (signal not in group_by_sender):
        group_by_sender[signal] = {}
        group_by_sender[signal]['sender']   = set([])
        group_by_sender[signal]['receiver'] = set([])
    for subsystem in result[signal]:
        for function in result[signal][subsystem]:
            sender   = result[signal][subsystem][function]['sender']
            receiver = result[signal][subsystem][function]['receiver']
            group_by_sender[signal]['sender']   |= set(sender)
            group_by_sender[signal]['receiver'] |= set(receiver)

            line = ','.join([signal, subsystem, function, '|'.join(sender), '|'.join(receiver)])
            line += '\n'
            csv_file_all.write(line)

csv_file_group_by_sender.write('Signal, Sender, Receiver\n')
for signal in group_by_sender:
    csv_file_group_by_sender.write( '{},{},{}\n'.format( signal,
                             '|'.join(list(group_by_sender[signal]['sender'])),
                             '|'.join(list(group_by_sender[signal]['receiver'])) ))
