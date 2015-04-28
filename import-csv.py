#!/usr/bin/python
import csv
import os
import yaml

parsed_data = {}
input_dir = './input'
for subsystem in os.listdir(input_dir):
    if(not subsystem.endswith('.csv')):
        continue
    with open("{}/{}".format(input_dir,subsystem), 'rb') as csvfile:
        subsystem = subsystem[:-4]
        reader = csv.DictReader(csvfile,skipinitialspace=True)
        print reader.fieldnames
        for row in reader:
            signal_long_name = row['Long Name']
            parsed_data.setdefault(signal_long_name, {})
            parsed_data[signal_long_name].setdefault(subsystem, {})
            parsed_data[signal_long_name][subsystem].setdefault('Subscriber', [])
            parsed_data[signal_long_name][subsystem]['Short Name'] = row['Short Name']
            parsed_data[signal_long_name][subsystem]['Subscriber'] += row['Subscriber'].split('|')
            parsed_data[signal_long_name][subsystem]['Subscriber'] = list(set(parsed_data[signal_long_name][subsystem]['Subscriber']))
    print subsystem
print '========================='
print yaml.dump(parsed_data,default_flow_style=False)
