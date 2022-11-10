import boto3
s3_client=boto3.client('s3',region_name='us-east-1')
def buildBucket():
    bucketName=input('Enter a name of bucket:')
    s3_client.create_bucket(Bucket=bucketName)


def listBuckets():
    response=s3_client.list_buckets()
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'{bucket["Name"]}')

buildBucket()
listBuckets()