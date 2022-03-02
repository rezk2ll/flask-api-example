from flask import Flask, Blueprint

app = Flask(__name__)

from clean_module import clean_blueprint

app.register_blueprint(clean_blueprint)

@app.route('/')
def main():
  return 'use a GET /clean/<text> or POST /clean'

@app.route('/rania')
def rania():
  return "Hello"

app.run(host='0.0.0.0')
