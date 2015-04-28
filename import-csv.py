#!/usr/bin/python
import csv
import os
import yaml

parsed_data = {}
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
            parsed_data.setdefault(signal_long_name, {})
            parsed_data[signal_long_name].setdefault(subsystem, {})
            parsed_data[signal_long_name][subsystem].setdefault('Subscriber', [])
            parsed_data[signal_long_name][subsystem]['Short Name'] = row['Short Name']
            parsed_data[signal_long_name][subsystem]['Subscriber'] += row['Subscriber'].split('|')
            parsed_data[signal_long_name][subsystem]['Subscriber'] = list(set(parsed_data[signal_long_name][subsystem]['Subscriber']))
print '========================='
log_md.write('\n\nGenerated Data\n==========================\n\n```yaml\n{}```'.format( yaml.dump(parsed_data,default_flow_style=False)))
