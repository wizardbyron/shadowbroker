#!/usr/bin/env python
import requests
import boto3
import dateutil.parser

def get_latest_amazon_image_id(region):
    client = boto3.client('ec2', region_name = region)
    images = client.describe_images(ExecutableUsers=['all'],Filters=[{'Name': 'name','Values': ['amzn2-ami-hvm-*']}],Owners=['amazon'])
    return sorted(images['Images'], key=lambda x:dateutil.parser.isoparse(x['CreationDate']))[-1]['ImageId']

def get_fastest_aws_region():
    client = boto3.client('ec2')
    regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    elapsedlist = []
    try:
        for region in regions:
            url = 'https://ec2.{}.amazonaws.com/'.format(region)
            elapsed = requests.get(url).elapsed.microseconds
            elapsedlist.append((region, elapsed))
    except Exception:
        pass
    return sorted(elapsedlist, key=lambda x:x[1])[0][0]

if __name__ == "__main__":
    region = get_fastest_aws_region()
    ami_id =  get_latest_amazon_image_id(region)
    print("%s:%s"%(region,ami_id))