from testBases.SessionToS3 import createS3Session
from utilities.readProperties import getRawBucketName


class Test_Connection_001:

    raw_bucket_name = getRawBucketName()
    list_bucket_name = []

    def test_S3_contains_raw_hl7_bucket(self):

        self.s3connector = createS3Session()
        self.s3_session = self.s3connector.create_customized_session()
        s3_resources_object = self.s3_session.resource('s3')
        
        
        for bucket in s3_resources_object.buckets.all():
            print(bucket.name)
            self.list_bucket_name.append(bucket.name)

        #print(self.list_bucket_name)    
            
        assert self.raw_bucket_name in self.list_bucket_name

            





    
