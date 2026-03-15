import os
from datetime import datetime
from azure.storage.blob import BlobServiceClient

conn = os.getenv("BLOB_CONNECTION")

def store_log(log):

    blob_service = BlobServiceClient.from_connection_string(conn)

    container = blob_service.get_container_client("cicd-logs")

    name = f"log-{datetime.utcnow().timestamp()}.txt"

    container.upload_blob(name, log, overwrite=True)