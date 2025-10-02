#!/bin/bash
 set -x
 aws s3 ls
 aws ec2 describe-instances --query "Reservations[].Instances[].InstanceId" --output text

 aws iam list-users
