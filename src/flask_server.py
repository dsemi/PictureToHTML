from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    return "Something"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)