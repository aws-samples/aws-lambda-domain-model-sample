import os
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
from i_slot_adapter import ISlotAdapter
from slot import Slot

table_name = os.getenv("TABLE_NAME", "VACCINATION_RESERVATION")
pk_prefix = "slot#"

'''
implement of Slot adapter for Amazon DynamoDB
'''
class DDBSlotAdapter(ISlotAdapter):
    def __init__(self):
        ddb = boto3.resource('dynamodb')
        self.__table = ddb.Table(table_name)

    def load(self, slot_id:str) -> Slot:
        try:
            response = self.__table.get_item(
                Key={'pk': pk_prefix + slot_id})
            if 'Item' in response:
                item = response['Item']
                reservation_date = item['reservation_date']
                location = item['location']
                slot = Slot(
                    slot_id, 
                    datetime.strptime(reservation_date, '%Y-%m-%d %H:%M:%S'), 
                    location)

                return slot
            return None

        except ClientError as e:
            print(e.response['Error']['Message'])
            return None
