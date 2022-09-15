from flask import Flask, request
import uuid
from google.cloud import storage

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['zip'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/submissions', methods=['POST', 'GET'])
def submissions():	
    if request.form.get('_method')=='POST':
        if 'file' in request.files:
            file = request.files['file']
            if allowed_file(file.filename):
                storage_client = storage.Client()

                bucket_name =  'quantum-ether-362110.appspot.com'  #os.environ.get()
                bucket = storage_client.bucket(bucket_name)
                blob = bucket.blob(str(uuid.uuid1()))
                blob.upload_from_string(data=file.read(), content_type="text/plain")
                # unzip, then launch tests (add option to add your own tests), finally put results in one dashboard, to be processed later on
                # unzip
                # iterate over files, push each to working queue ?
                # then containerized app pop from the queue, do the job, push to dashboard
                return 'good'
            else:
                return 'where zip'

if __name__ == '__main__':
    # add mission number, ability to upload a test suite, etc
    app.run(host='127.0.0.1', port=8001, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
