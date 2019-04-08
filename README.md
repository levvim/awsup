# awsup
## uploader script for AWS S3 buckets

This is a simple script to facilitate the python based CLI uploader in bash for S3 buckets using the `boto3` library. It provides utility since it can potentially be faster for transfers compared to the AWS CLI interface. It requires python3 and the boto3 library to be installed and is called via ordered arguments:

        python awsup.py \
                file_to_upload \
                file_destination

The aws access key and bucket/prefix have to be set up, which are at the beginning of the script.
