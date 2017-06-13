
import json


def get_json_data():
    with file('geo_json_data.json') as f:
        return f.read()

data = json.loads(get_json_data())

result = []


for feature in data['features']:
    geometry = feature['geometry']
    if geometry['type'] == 'Point':
        properties = feature['properties']

        result.append({
            'loc': geometry['coordinates'],
            'data': {k.replace(' ', ''): v for k, v in properties.iteritems()}
        })

with open('ariel_data.json', 'w') as arik:
    arik.writelines(json.dumps(result))

