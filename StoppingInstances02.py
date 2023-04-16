
#!/usr/bin/env python3.7

import boto3

#create 5 ec2 instances

ec2 = boto3.resource('ec2')

instance = (ec2.create_instances(
    ImageId='ami-06e46074ae430fba6',
    InstanceType='t2.micro',
    MaxCount=5,
    MinCount=5)
    )
print(instance)

ec2.Instance('i-034873fc863f7939d').stop()
ec2.Instance('i-098e1c326b9ef9ce4').stop()
ec2.Instance('i-02b2e792951c1e642').stop()
ec2.Instance('i-0639015bd4eda156e').stop()
ec2.Instance('i-07879481ed6d5cefc').stop()


