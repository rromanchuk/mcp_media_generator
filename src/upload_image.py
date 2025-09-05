import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import uuid
import os

def generate_unique_object_name():
    """Generate a unique object name using UUID and preserve the file extension.

    :return: Unique object name with the same file extension
    """

    # Generate a UUID
    unique_id = str(uuid.uuid4())
    # Combine UUID and extension
    unique_object_name = f"{unique_id}.png"

    return unique_object_name

def upload_file_to_s3(file_object):
    """Upload a file to an S3 bucket and return a pre-signed URL valid for 1 hour.

    :param file_object: File-like object to upload
    :return: Pre-signed URL string if successful, else None
    """
    aws_region = os.environ['AWS_REGION']
    aws_bucket = os.environ["S3_BUCKET"]

    object_name = generate_unique_object_name()

    # Create an S3 client
    s3_client = boto3.client('s3', region_name=aws_region)

    try:
        # Upload the file to S3
        s3_client.upload_fileobj(Fileobj=file_object, Bucket=aws_bucket, Key=object_name, ExtraArgs={'ContentType': 'image/png'})

        # Generate a pre-signed URL valid for 1 hour (3600 seconds)
        url = s3_client.generate_presigned_url('get_object',
                                               Params={'Bucket': aws_bucket,
                                                       'Key': object_name},
                                               ExpiresIn=3600)
        return url

    except FileNotFoundError:
        print(f"The file {file_object} was not found.")
        return None
    except ClientError as e:
        print(f"Client error: {e}")
        return None
