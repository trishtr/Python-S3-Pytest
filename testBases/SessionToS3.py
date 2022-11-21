import boto3
from boto3.session import Session
from utilities.readProperties import getAccessKey, getRegionName, getSecretKey, getSessionToken


class createS3Session:

    """
    A session stores configuration state and allows to create clients and resources
    It contains: aws_access_key_id, aws_secret_access_key, aws_session_token
    and the region_name
    """
    access_key = getAccessKey()
    secret_key = getSecretKey()
    session_token = getSessionToken()
    region_name = getRegionName()

    def create_customized_session(self):
        customized_session = boto3.Session(aws_access_key_id= self.access_key,
                                   aws_secret_access_key= self.secret_key,
                                   aws_session_token = self.session_token,
                                   region_name= self.region_name)
        
        return customized_session


