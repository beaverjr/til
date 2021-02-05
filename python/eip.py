import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
try:
    filters = [
    {'Name': 'network-interface-id', 'Values': ['eni-xxxxxxxxxx']}
    ]
    addresses = ec2.describe_addresses(Filters=filters)
    address_list = addresses["Addresses"]
    address = address_list[0] if len(address_list) else ''
    old_allocationid = address["AllocationId"]
    print(old_allocationid)
    allocation = ec2.allocate_address(Domain='vpc')
    associate = ec2.associate_address(AllocationId=allocation['AllocationId'],NetworkInterfaceId='eni-xxxxxxxxxxxx')
    print(associate)
    release = ec2.release_address(AllocationId=old_allocationid)
    print('Address released')
except ClientError as e:
    print(e)