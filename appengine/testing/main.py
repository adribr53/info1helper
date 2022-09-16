from flask import Flask, request
import uuid
import zipfile
import os
import test
from google.cloud import storage

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['zip'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# TODO : take updates from github for test

@app.route('/submissions', methods=['POST', 'GET'])
def submissions():	
    # TODO delete dir after response
    if request.form.get('_method')=='POST':
        if 'file' in request.files:
            file = request.files['file']
            if allowed_file(file.filename):
                name, _ = file.filename.rsplit('.zip')
                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall('/tmp/dir')
                    res = ""
                    for filename in os.listdir('/tmp/dir/'+name):
                        tmp = test.test('/tmp/dir/'+name+'/'+filename)
                        res = res + filename + ","+str(tmp) + "\n"
                        # write res to bucket
                        # consider firestore or cloud sql instead
                    storage_client = storage.Client()
                    bucket_name =  'dashboard11111'  
                    bucket = storage_client.bucket(bucket_name)
                    blob = bucket.blob(str(uuid.uuid1()))
                    output = res
                    blob.upload_from_string(data=output, content_type="text/plain")
                return 'good'
            else:
                return 'where zip'

if __name__ == '__main__':
    # add mission number, ability to upload a test suite, etc
    app.run(host='127.0.0.1', port=8001, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
