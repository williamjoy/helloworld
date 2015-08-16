import sys
import requests
dot_string = open(sys.argv[1], 'r').read()
print dot_string
url='https://chart.googleapis.com/chart'
req = requests.Request('GET',url,params = {'cht':'gv:dot','chl':dot_string})
r = req.prepare()
print r.url



