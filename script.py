from urllib.request import Request, urlopen
import json,os


def get_jsonparsed_data(url):
    query = Request(url)
    query.add_header('Accept', 'application/json')
    data = urlopen(query).read()
    return json.loads(data)


outputfile = os.environ.get('OUTPUT_FILE')
metadatabaseurl = os.environ.get('CONFIG_BASEURL')
metadatakeys = os.environ.get('CONFIG_KEYS').split(',')
finaljson = { }
for key in metadatakeys:
  url = metadatabaseurl + key
  data = get_jsonparsed_data(url)
  finaljson.update({key : data})

with open(outputfile, 'w+') as handle:
  json.dump(finaljson, handle)
