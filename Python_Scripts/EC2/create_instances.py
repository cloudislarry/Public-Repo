import boto3

ec2 = boto3.resource ('ec2')

instance = ec2.create_instances( # Arguments
    ImageId = 'ami-06ca3ca175f37dd66',
    MinCount = 3,
    MaxCount = 4, 
    InstanceType = 't2.micro',
    KeyName= 'LUIT',
    TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': 'Name','Value': 'Dev'},
                {'Key': 'Env','Value': 'Dev'}]
                          },
                      ],
                      )
print(instance)