import os
from google.cloud import storage
from st_secrets import load_secrets

load_secrets()

def download_blobs(bucket_name, prefix='', local_directory=''):
    # Ensure the local directory exists or create it if it doesn't
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    client = storage.Client.from_service_account_json('service_account_key.json')
    bucket = client.get_bucket(bucket_name)

    blobs = bucket.list_blobs(prefix=prefix)

    for blob in blobs:
        if blob.name.endswith('/'):  # Check if it's a "folder" (blob with a trailing '/')
            pass
        else:
            local_filename = f"{local_directory}/{blob.name.split('/')[-1]}"  # Extract the file name
            blob.download_to_filename(local_filename)
            print(f"Downloaded {blob.name} to {local_filename}")
    return 0


# download_blobs(
#     'sodipe-models', 
#     prefix='gpt2/', 
#     local_directory='assets/gpt2/'
# )
