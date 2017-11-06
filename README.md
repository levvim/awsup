# awsup
## uploader script for AWS S3 buckets

This is a simple script to facilitate the python based CLI uploader in bash for S3 buckets. It requires python/boto3 and is called via ordered arguments:

        python awsup.py \
                file_to_upload \
                file_destination

The aws access key and bucket/prefix have to be set up, which are at the beginning of the script.
