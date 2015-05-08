#!/usr/bin/python
import csv
import os
import yaml

from graphviz import Digraph
import zlib

dot = Digraph('Signals',format='svg')
dot.graph_attr['rankdir'] = 'LR'
dot.graph_attr['title'] = 'ECU Signals'
dot.node_attr['shape'] = 'box'
dot.node_attr['style'] = 'filled'

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

def hash_color(data):
    return '#' + hex(zlib.adler32(data) % 0xffffff)[2:]

all_ecus = set()

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

            signal_long_name  = row[__LONG_NAME__]
            signal_short_name = row[__SHORT_NAME__]
            publisher   = row[__PUBLISHER__]
            subscribers = row[__SUBSCRIBER__].split('|')
            if(publisher not in all_ecus):
                all_ecus.add(publisher)
                dot.node(publisher,publisher, color=hash_color(publisher))


            by_ecu.setdefault(publisher, {})
            by_ecu[publisher].setdefault(__SENDING__, {})
            by_ecu[publisher][__SENDING__].setdefault(signal_long_name, {})
            by_ecu[publisher][__SENDING__][signal_long_name].setdefault(subsystem, [])
            by_ecu[publisher][__SENDING__][signal_long_name][subsystem] += subscribers
            by_ecu[publisher][__SENDING__][signal_long_name][subsystem] = list(set(by_ecu[publisher][__SENDING__][signal_long_name][subsystem]))

            for subscriber in subscribers:
                if(subscriber not in all_ecus):
                    all_ecus.add(subscriber)
                    dot.node(subscriber,subscriber, color=hash_color(subscriber))
                dot.edge(publisher,subscriber,label="{}::{}".format(subsystem,signal_short_name), color=hash_color(signal_short_name))
                by_ecu.setdefault(subscriber, {})
                by_ecu[subscriber].setdefault(__RECEIVERING__, {})
                by_ecu[subscriber][__RECEIVERING__].setdefault(signal_long_name, {})
                by_ecu[subscriber][__RECEIVERING__][signal_long_name].setdefault(subsystem,[])
                by_ecu[subscriber][__RECEIVERING__][signal_long_name][subsystem].append(publisher) #no dedup here, expecting array length to be 1

            by_signal.setdefault(signal_long_name, {})
            by_signal[signal_long_name].setdefault(subsystem, {})
            by_signal[signal_long_name][subsystem].setdefault(__SUBSCRIBER__, [])
            by_signal[signal_long_name][subsystem][__SHORT_NAME__] = signal_short_name
            by_signal[signal_long_name][subsystem][__PUBLISHER__] = publisher
            by_signal[signal_long_name][subsystem][__SUBSCRIBER__] += subscribers
            by_signal[signal_long_name][subsystem][__SUBSCRIBER__] = list(set(by_signal[signal_long_name][subsystem]['Subscriber']))
    log_md.write("\n\n")
print '========================='
log_md.write('\nGenerated Data\n==========================\n\n```yaml\n')
log_md.write('{}```'.format( yaml.dump(by_ecu,default_flow_style=False)))

log_md.write('\nGenerated Graphviz Source\n==========================\n\n```dot\n')
log_md.write(dot.source)
log_md.write('\n```')
dot.render('graph.dot')
