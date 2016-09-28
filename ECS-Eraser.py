#Om
#Script to delete buckets and everything inside the specified bucket. At present it is not possible to delete the folders inside buckets. That functionality will added soon.
#ECS is Elastic Cloud Storage from DELL EMC. 
from boto3.session import Session, Config

print('***This program will delete the specified bucket and its contents owned by an object user***\n\n \
URL of the ECS Node IP or the loadbalancer is hardcoded in the script. Edit the script to change "ecs_url" with \n the IP address that you have set for ECS. \
Likewise change "ecs_obj_user" and "ecs_secret_key" with the ECS object user \n and the respective secret key.\n\n')

#Connection information
ecs_url = 'https://x.x.x.x:9021' # IP address of ECS
ecs_obj_user = 'Enter objtect user here' # ECS object user
ecs_secret_key = 'Enter secret key here' # Secret key belonging object user

#The url we use is secure i.e via 9021 and the SSL certificate provided by ECS is not verified,
#so we will capture the InsecureRequestWarning with a logging module.
import logging
logging.captureWarnings(True)

addressing_style = 'path' #ECS recommends using path style
signature_version = 's3'

#Establishing connection to ECS
session = Session(aws_access_key_id=ecs_obj_user, aws_secret_access_key=ecs_secret_key)
s3 = session.resource('s3', endpoint_url=ecs_url, verify=False,   
                      config=Config(signature_version='s3', s3={'addressing_style': 'path'}))

#Getting bucket name from user and saving it in b1
b1 = str(input('Enter the name of bucket which needs to be deleted: '))

print('\n')

#Partially working need to add a way to delete folders inside folders and its contents
for b1 in s3.buckets.all():
    for key in b1.objects.all():
        print('Deleting key', key)
        key.delete()
print('\n')
print('Bucket', b1, 'is deleted')
b1.delete()
print('\n')