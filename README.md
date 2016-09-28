# ECS-Eraser
Script to delete buckets and everything inside the specified bucket. At present it is not possible to delete the folders inside buckets. That functionality will added soon.

# >This script is highly destructive. Please excercise extreme caution.

#Requirements
Python 3.x
boto3

#Installation Instructions
Download and install Python 3.x - https://www.python.org/downloads/
boto3 is AWS SDK for python. Following the installation instructions to install boto3 (Python should be installed first) - https://github.com/boto/boto3

#How to run?
After installing python and boto3, edit the script and include IP address of ECS, username and secret key of the object user.
Save and navigate to the location where you have placed the script in command prompt and run the following,

`# python ECS_Eraser.py`

Enter the name of the bucket when asked.
