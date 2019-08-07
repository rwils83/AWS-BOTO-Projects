import boto3, requests, json, os

# client = boto3.client('sts')
#
# response = client.assume_role(
#     RoleArn = '',
#     RoleSessionName='',
#     PolicyArns=[
#         {
#             'arn':'string'
#         }
#     ],
#     Policy='',
#     ExternalId='',
#     SerialNumber='',
#     TokenCode=''
# )
# s3 = boto3.client('s3')
#
# response2 = s3.list_buckets()
#
# print('Existing buckets:')
# for bucket in response2['Bucket']:
#     print(f' {bucket["Name"]}')
test = os.getenv('AWSKEY')
print(test)
test2 = os.getenv('AWSSECRET')
print(test2)
print(os.getenv('path'))