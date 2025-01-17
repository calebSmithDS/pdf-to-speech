import os
import sys
import time
import tempfile
from flask import Flask, render_template, flash, request, redirect, url_for, send_file, after_this_request
from werkzeug.utils import secure_filename
from script import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')




@app.route('/success', methods = ['POST'])
def success():
    # the file does upload correctly 
    if request.method == 'POST':
        
        if 'file' not in request.files:
            return "no file"

        f = request.files['file']
        if f.filename == '':
            return 'No selected file'
        
    # this temp file method does produce cleaned text 
        with tempfile.NamedTemporaryFile(mode="wb", delete=False, suffix="pdf") as temp:
            temp.write(f.read())
            temp_path = temp.name
        
        processed_file = clean_text(temp_path)
    
    # text to mp3 convert
    file_name = f.filename.split('.')[0] + "-output.mp3"
    
    text_to_mp3(processed_file, file_name)
        
        
    DOWNLOAD_FOLDER = f"{os.getenv('USERPROFILE')}\\Downloads"

    
    response = send_file(file_name, as_attachment=True)

    @after_this_request
    def clean_files(response):
        try:
            print("entering clean up")
            if os.path.exists(file_name):
                os.remove(file_name)
                
            os.remove(temp)
            os.remove(temp_path)
        except Exception as e:
            # time.sleep(30)
            # os.remove(file_name)
            # os.remove(temp)
            # os.remove(temp_path)
            print(f"error removing files: {e}")
        return response
           
    return response
    
if __name__ == '__main__':
    app.run(debug=True)
