import boto3
import boto3.s3.transfer
from boto3.s3.transfer import S3Transfer
import sys

BUCKET='bucket_here'
PREFIX='prefix_here/'
AWS_ACCESS_KEY_ID = 'access_key_here',
AWS_SECRET_ACCESS_KEY = '/secret_access_key_here',

localFile=sys.argv[1]
remoteFilePath=sys.argv[2]

def uploadFile(filepath):
	transfer = S3Transfer(client)
	# Upload /tmp/myfile to s3://bucket/key and print upload progress.
	transfer.upload_file(filepath, BUCKET, PREFIX)
	return()

def uploadObject(filePath, S3name):
	try:
		with open(filePath, 'rb') as f:
			client.upload_fileobj(f,BUCKET,PREFIX + '{S3name}'.format(S3name=S3name))
			print('Uploading file:' , filePath)
			print('File alias for the S3 will be: ', S3name)
	except FileNotFoundError:
			print("No file or directory was found on your machine to upload.")
	return()

if __name__ == "__main__":

	client = boto3.client(
		's3','us-east-1',
		aws_access_key_id = AWS_ACCESS_KEY_ID,
		aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
	)

	bucket = BUCKET
	prefix = PREFIX

	exit = False

        uploadObject(localFile, remoteFilePath)
