#!/usr/bin/python
import csv
import os
import yaml

parsed_data_by_signal = {}
parsed_data_by_publisher = {}
parsed_data_by_subscriber = {}
input_dir = './input'
log_md=open("output.md", 'wb')

__SHORT_NAME__ = 'Short Name'
__LONG_NAME__  = 'Long Name'
__SUBSCRIBER__ = 'Subscriber'
__PUBLISHER__  = 'Publisher'

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
                cell = row[reader.fieldnames[i]]
                if (cell):
                    cell = '\\|'.join([ '`{}`'.format(i) for i in cell.split('|') ])
                log_md.write(cell)
                log_md.write(" |")
            signal_long_name = row[__LONG_NAME__]
            parsed_data_by_signal.setdefault(signal_long_name, {})
            parsed_data_by_publisher.setdefault(row[__SHORT_NAME__], {})
            parsed_data_by_signal[signal_long_name].setdefault(subsystem, {})
            parsed_data_by_signal[signal_long_name][subsystem].setdefault(__SUBSCRIBER__, [])
            parsed_data_by_signal[signal_long_name][subsystem][__SHORT_NAME__] = row[__SHORT_NAME__]
            parsed_data_by_signal[signal_long_name][subsystem][__PUBLISHER__] = row[__PUBLISHER__]
            subscribers = row[__SUBSCRIBER__].split('|')
            parsed_data_by_signal[signal_long_name][subsystem][__SUBSCRIBER__] += subscribers
            parsed_data_by_signal[signal_long_name][subsystem][__SUBSCRIBER__] = list(set(parsed_data_by_signal[signal_long_name][subsystem]['Subscriber']))
    log_md.write("\n\n")
print '========================='
log_md.write('\nGenerated Data\n==========================\n\n```yaml\n')
log_md.write('{}```'.format( yaml.dump(parsed_data_by_signal,default_flow_style=False)))
