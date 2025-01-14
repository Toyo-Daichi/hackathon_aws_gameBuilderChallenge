#!/bin/bash

export AWS_PROFILE=
export AWS_REGION=

AWS_ACCOUNT_ID=`aws sts get-caller-identity --query Account --output text`
image=
repo=

ecr_uri=${AWS_ACCOUNT_ID}.dkr.ecr.ap-northeast-1.amazonaws.com/${repo}

# ECR login
aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ecr_uri}

docker image tag ${image}:latest ${ecr_uri}:latest
docker image push ${ecr_uri}:latest

echo "Normal END"
exit
