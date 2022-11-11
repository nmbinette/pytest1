import logging
import boto3
from botocore.exceptions import ClientError


def to_the_cloud(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    TEST_BUCKET = "comp630-m1-f21-proftim"

    # Upload the file
    s3_client = boto3.Session(profile_name='nmb1056').client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(f'Upload Response: {response}')
    except ClientError as e:
        logging.error(e)
        return False
    
    return True
