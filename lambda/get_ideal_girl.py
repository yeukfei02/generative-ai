import boto3
import json


def handler(event, context):
    print(f"event = {event}")

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "urls": []
        })
    }

    urls = get_presigned_url()
    if urls:
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "urls": urls
            })
        }

    print(f"response = {response}")
    return response


def get_presigned_url():
    urls = []

    try:
        client = boto3.client('s3')

        bucket = 'ideal-girl'

        response = client.list_objects(
            Bucket=bucket
        )
        print(f"response = {response}")

        if response:
            contents = response["Contents"]
            if contents:
                for item in contents:
                    key = item["Key"]

                    url = client.generate_presigned_url(
                        ClientMethod='get_object',
                        Params={
                            'Bucket': bucket,
                            'Key': key
                        },
                        ExpiresIn=86400
                    )
                    urls.append(url)
    except Exception as e:
        print(f"get_presigned_url error = {e}")

    return urls
