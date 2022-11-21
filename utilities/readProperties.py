import configparser

config = configparser.RawConfigParser()
config.read("configuration/config.ini")

def getAccessKey():
    access_key = config.get('aws_connection_key', 'access_key')
    return access_key

def getSecretKey():
    secret_key = config.get('aws_connection_key', 'secret_key')  
    return secret_key

def getSessionToken():
    session_token = config.get('aws_connection_key', 'session_token')
    return session_token   

def getRegionName():
    region_name = config.get('aws_connection_key', 'region_name')
    return region_name 

def getRawBucketName():
    raw_bucket = config.get('buckets_name','raw_bucket')
    return raw_bucket