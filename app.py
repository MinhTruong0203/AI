from flask import Flask, request
from flask import render_template
import utils
import os
import imp

is_first = True

app = Flask(__name__)
app.secret_key = 'document_scanner_app'

@app.route('/',methods=['GET','POST'])
def scandoc():
    if request.method == 'POST':
        file = request.files['image_name']
        upload_image_path = utils.save_upload_image(file)
        print('Image saved in = ',upload_image_path)
        return render_template('scanner.html')            
    
    return render_template('scanner.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    global is_first
    import main
    if not is_first:
        imp.reload(main)
    is_first = False
    return render_template('result.html',results=main.display())

if __name__ == "__main__":
    app.run(debug=True)