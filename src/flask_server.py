import os
from flask import Flask, request
from werkzeug.utils import secure_filename

from html_structure.converter import convert

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            f_name_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(f_name_path)
            # Call thing here
            html = convert(f_name_path)
            return html
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)