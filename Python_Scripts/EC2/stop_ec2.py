import boto3

def stop_all_ec2_instances():
   
    ec2 = boto3.client('ec2')

    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]) # Get running instances

    instance_ids = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    if not instance_ids:
        print("No running EC2 instances found.")
        return

    ec2.stop_instances(InstanceIds=instance_ids) # Stop all running instances
    print("Stopping EC2 instances:", instance_ids)

if __name__ == "__main__":
    stop_all_ec2_instances()