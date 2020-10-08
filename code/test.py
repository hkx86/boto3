import boto3

s3 = boto3.resource('s3')

data = open('/Users/faat/Documents/Screenshot 2020-08-18 at 5.07.32 PM.png', 'rb')

s3.Bucket('sky88-nextcloud').put_object(Key='test.png', Body=data)
# for bucket in s3.buckets.all():
#     print(bucket.name)
