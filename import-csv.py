#!/usr/bin/python
import csv
import os
import yaml

by_signal = {}
by_ecu = {}
input_dir = './input'
log_md=open("output.md", 'wb')

__SHORT_NAME__ = 'Short Name'
__LONG_NAME__  = 'Long Name'
__SUBSCRIBER__ = 'Subscriber'
__PUBLISHER__  = 'Publisher'
__SENDING__    = 'Sending'
__RECEIVERING__  = 'Receiving'

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
            subscribers = row[__SUBSCRIBER__].split('|')


            by_ecu.setdefault(row[__PUBLISHER__], {})
            by_ecu[row[__PUBLISHER__]].setdefault(__SENDING__, {})
            by_ecu[row[__PUBLISHER__]][__SENDING__].setdefault(signal_long_name, {})
            by_ecu[row[__PUBLISHER__]][__SENDING__][signal_long_name].setdefault(subsystem, [])
            by_ecu[row[__PUBLISHER__]][__SENDING__][signal_long_name][subsystem] += subscribers
            by_ecu[row[__PUBLISHER__]][__SENDING__][signal_long_name][subsystem] = list(set(by_ecu[row[__PUBLISHER__]][__SENDING__][signal_long_name][subsystem]))

            for subscriber in subscribers:
                by_ecu.setdefault(subscriber, {})
                by_ecu[subscriber].setdefault(__RECEIVERING__, {})
                by_ecu[subscriber][__RECEIVERING__].setdefault(signal_long_name, {})
                by_ecu[subscriber][__RECEIVERING__][signal_long_name].setdefault(subsystem,[])
                by_ecu[subscriber][__RECEIVERING__][signal_long_name][subsystem].append(row[__PUBLISHER__]) #no dedup here, expecting array length to be 1

            by_signal.setdefault(signal_long_name, {})
            by_signal[signal_long_name].setdefault(subsystem, {})
            by_signal[signal_long_name][subsystem].setdefault(__SUBSCRIBER__, [])
            by_signal[signal_long_name][subsystem][__SHORT_NAME__] = row[__SHORT_NAME__]
            by_signal[signal_long_name][subsystem][__PUBLISHER__] = row[__PUBLISHER__]
            by_signal[signal_long_name][subsystem][__SUBSCRIBER__] += subscribers
            by_signal[signal_long_name][subsystem][__SUBSCRIBER__] = list(set(by_signal[signal_long_name][subsystem]['Subscriber']))
    log_md.write("\n\n")
print '========================='
log_md.write('\nGenerated Data\n==========================\n\n```yaml\n')
log_md.write('{}```'.format( yaml.dump(by_ecu,default_flow_style=False)))
