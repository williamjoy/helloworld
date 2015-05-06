#!/usr/bin/python
import csv
import os
import yaml

parsed_data_by_sender = {}
parsed_data_by_subscriber = {}
input_dir = './input'
log_md=open("output.md", 'wb')

for subsystem in os.listdir(input_dir):
    if(not subsystem.endswith('.csv')):
        continue
    log_md.write("{}\n==========================\n".format(subsystem))
    with open("{}/{}".format(input_dir,subsystem), 'rb') as csvfile:
        subsystem = subsystem[:-4]
        reader = csv.DictReader(csvfile,skipinitialspace=True)
        print reader.fieldnames
        log_md.write("|{}|\n| ".format("|".join(reader.fieldnames)))
        for i in range(len(reader.fieldnames)):
            log_md.write("--- |")
        for row in reader:
            log_md.write("\n|")
            for i in range(len(reader.fieldnames)):
                log_md.write(row[reader.fieldnames[i]].replace('|','\\|'))
                log_md.write(" |")
            signal_long_name = row['Long Name']
            parsed_data_by_sender.setdefault(signal_long_name, {})
            parsed_data_by_sender[signal_long_name].setdefault(subsystem, {})
            parsed_data_by_sender[signal_long_name][subsystem].setdefault('Subscriber', [])
            parsed_data_by_sender[signal_long_name][subsystem]['Short Name'] = row['Short Name']
            parsed_data_by_sender[signal_long_name][subsystem]['Publisher'] = row['Publisher']
            subscribers = row['Subscriber'].split('|')
            parsed_data_by_sender[signal_long_name][subsystem]['Subscriber'] += subscribers
            parsed_data_by_sender[signal_long_name][subsystem]['Subscriber'] = list(set(parsed_data_by_sender[signal_long_name][subsystem]['Subscriber']))
    log_md.write("\n\n")
print '========================='
log_md.write('\nGenerated Data\n==========================\n\n```yaml\n{}```'.format( yaml.dump(parsed_data_by_sender,default_flow_style=False)))
