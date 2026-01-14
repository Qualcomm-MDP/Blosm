import flask

app = flask.Flask(__name__)
app.config.from_object('mdpweb.config')

import mdpweb.views.index

print(app.url_map)