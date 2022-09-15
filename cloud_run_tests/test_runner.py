"""
IO :
pass a zip to unzip, containing codes to run against a suite of tests
"""
import zipfile
import os
import test_example
import uuid
from google.cloud import storage

# iterate over files, run tests for each file, publish results in result list ? (async)
def main(zipname):
    name, _ = zipname.rsplit('.zip')
    print("name", name)
    with zipfile.ZipFile(zipname, 'r') as zip_ref:
        zip_ref.extractall('./dir') # extract to cloud storage ? 
        for filename in os.listdir('./dir/'+name):
            print(filename)
            res = test_example.test('./dir/'+name+'/'+filename)
            # write res to bucket
            # consider firestore or cloud sql instead
            storage_client = storage.Client()
            bucket_name =  'dashboard11111'  
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(str(uuid.uuid1()))
            output = name+' '+str(res)
            blob.upload_from_string(data=output, content_type="text/plain")
                
if __name__=='__main__':
    main("test.zip")