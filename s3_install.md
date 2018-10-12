# Remote installation and configuration of aws cli for s3 uploading

First we would like to install aws cli inside a virtual environment. Install miniconda3 and follow the prompts:

        cd $HOME
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
        chmod u+x Miniconda3-latest-Linux-x86_64.sh
        ./Miniconda3-latest-Linux-x86_64.sh

Navigate to miniconda and install aws

        $HOME/miniconda3/bin/pip install pip install --upgrade pip awscli s3cmd

Configure keys (we use `region:us-east-1 and output:none`)

        $HOME/miniconda3/bin/aws configure

We can then upload to s3 using a `s3 cp` command.

        $HOME/miniconda3/bin/aws s3 cp test.txt "s3://bucket/Collab_TEST/test.txt"

