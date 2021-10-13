from flask import Flask, request

import json

def read_json(path):
    with open(path, 'r') as f:
        data = json.load(f).get('api_list', [])

    return data

def api_return():
    rt = str(request.url_rule)
    return json_dc.get(rt, {'message': 'Somethine Wrong!'})

app = Flask(__name__)

data = read_json('api.json')

json_dc = {}

for d in data:
    rt = d.get('route')
    data = d.get('data')
    method = d.get('method')

    json_dc[rt] = data

    app.add_url_rule(rt, methods=method, view_func=api_return)

if __name__ == '__main__':
    # app.run('0.0.0.0', )
    app.run('127.0.0.1', debug=True)