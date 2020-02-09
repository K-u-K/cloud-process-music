#!/bin/bash

if [ ! -f "$HOME/aws-sdk/aws-iam-authenticator" ]; then
  curl -o "$HOME/aws-sdk/aws-iam-authenticator" https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/linux/amd64/aws-iam-authenticator
  chmod +x "$HOME/aws-sdk/aws-iam-authenticator"
fi

# if [ ! -f "$HOME/aws-sdk/eksctl" ]; then
#     curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/latest_release/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C "$HOME/aws-sdk"
# fi

if [ ! -f "$HOME/aws-sdk/kubectl" ]; then
    curl -o "$HOME/aws-sdk/kubectl" https://amazon-eks.s3-us-west-2.amazonaws.com/1.14.6/2019-08-22/bin/darwin/amd64/kubectl
    chmod +x "$HOME/aws-sdk/kubectl"
fi
