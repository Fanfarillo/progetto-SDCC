#bin/bash

AMI=ami-05fa00d4c63e32376
sg=sg-06560604d4de772d5

aws ec2 run-instances --image-id ${AMI} --count 1 \
--instance-type t2.micro \
--security-group-ids ${sg} \
--key-name SDCC-keys-1 --associate-public-ip-address \
--tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=SDCC}]"
