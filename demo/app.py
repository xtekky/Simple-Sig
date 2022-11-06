from secrets         import token_hex
from flask           import (Flask, render_template, send_file, request)
import requests, curlify

app = Flask(__name__, template_folder='assets/html')

app.config['SECRET_KEY'] = token_hex(64)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


class website:
    def __init__(self) -> None:
        self.routes = {
            '/': {
                'function': self._index,
                'methods': ['GET', 'POST']
            },
            '/assets/<folder>/<file>': {
                'function': self._assets,
                'methods': ['GET', 'POST']           
            },
            '/test': {
                'function': self._test,
                'methods': ['POST']
            }
        }

        self.config = {
            'host': '0.0.0.0',
            'port': 5000,
            'debug': True
        }

    def _test(self):
        data = request.data
        sig1 = request.headers['x-kspx-00']
        sig2 = request.headers['x-tx-00']
        
        r = requests.post('https://sig.xtekky.repl.co/verify', json = {
            'x-kspx-00': sig1,
            'x-tx-00': sig2,
            'data': data.decode('utf-8') # also works with querystring or whatever u used in index.js
        })
        
        if r.json()['is_valid'] == True:
            return {
                'status': 'success'
            }

        else:
            return {
                'status': 'error',
                'message': 'invalid sig'
            }

    def _index(self):
        return render_template('index.html')
        
    def _assets(self, folder: str, file: str):
        try:
            return send_file(f"assets/{folder}/{file}", as_attachment=False)
        except:
            return "File not found", 404

if __name__ == '__main__':
    website = website()
    
    for route in website.routes:
        app.add_url_rule(
            route,
            view_func=website.routes[route]['function'],
            methods=website.routes[route]['methods']
        )

    app.run(**website.config)