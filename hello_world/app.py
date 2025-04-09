import json
import boto3


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    """
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('dynamo-crud-table')

    response = table.get_item(
        Key={
            'ID': '1'
        }
    )

    current_count = response['Item']['vistor_count']
    current_count = str(int(current_count) + 1)

    table.update_item(
        Key={
            'ID': '1',
        },
        UpdateExpression="SET vistor_count = :val1",
        ExpressionAttributeValues={
            ':val1': current_count
        },
    )

    return {"statusCode": 200, 
            "headers": {
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': '*',
            },
            "body": current_count}
    # try:
    #     http_method = event.get('httpMethod')
    #     path = event.get('path')

    #     if http_method == 'GET' and path == '/hello':
    #         response = get_vistor()
    #     else:
    #         response = create_table()

    # except Exception as e:
    #     print('Error:', e)
    #     response = {"statusCode": 400, "body": json.dumps({
    #         "message": 'Error processing request',})
    #         }
   
    # return response


# def get_vistor():
#     # Get the service resource.
#     dynamodb = boto3.resource('dynamodb')

#     table = dynamodb.Table('visitors')

#     response = table.get_item(
#         Key={
#             'ID': '1'
#         }
#     )

#     current_count = response['Item']['vistor_count']
#     current_count = str(int(current_count) + 1)

#     table.update_item(
#         Key={
#             'ID': '1',
#             'vistor_count': current_count
#         }
#     )

#     return {"statusCode": 200, "body": json.dumps({
#             "message": current_count,})
#             }

# def create_table():
#     # Get the service resource.
#     dynamodb = boto3.resource('dynamodb')

#     table = dynamodb.create_table(
#         TableName='dynamo-crud-table',
#         KeySchema=[
#             {
#                 'AttributeName': 'ID',
#                 'KeyType': 'HASH'  # Partition key
#             },
#         ],
#         AttributeDefinitions=[
#             {
#                 'AttributeName': 'ID',
#                 'AttributeType': 'S'
#             },
#         ],
#     )
#     # Wait until the table exists.
#     table.wait_until_exists()

#     # Add an entry for the visitor count
#     table.put_item(
#         Item={
#             'ID': '1',
#             'vistor_count': 0
#         }
#     )
#     # Print out some data about the table.
#     print(table.item_count)

#     return {"statusCode": 200, "body": json.dumps({
#             "message": 'Table created, item added',})}