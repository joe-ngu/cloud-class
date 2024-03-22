'''
A simple application to help you spit bars.
'''

import flask
from index import Index
from foods import Foods

app = flask.Flask(__name__)

app.add_url_rule('/',
        view_func=Index.as_view('index'),
        methods=['GET', 'POST']
)

app.add_url_rule('/foods',
        view_func=Foods.as_view('foods'),
        methods=['GET', 'POST']
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
