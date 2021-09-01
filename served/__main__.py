from pulumi import StackReference, export
from pulumi_aws import s3

bucket1 = StackReference("bucket1")
bucket2 = StackReference("bucket2")

combines_tags = {
    "bucket1": bucket1.get_output("bucket_name"),
    "bucket2": bucket2.get_output("bucket_name"),
    "Managed By": "Pulumi",
}

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket',
    acl="private",
    tags=combines_tags,
)

# Export the name of the bucket
export('bucket_name', bucket.id)