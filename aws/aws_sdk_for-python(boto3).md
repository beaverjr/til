## 20210203
ドキュメント：https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

- describe_addresses
ENIで絞る

```
import boto3

ec2 = boto3.client('ec2')
filters = [
    {'Name': 'network-interface-id', 'Values': ['eni-xxxxxxxxxx','eni-xxxxxxxxxxx']}
]
response = ec2.describe_addresses(Filters=filters)
print(response)
```