from logging import exception
import os
import boto3
from botocore.exceptions import ClientError
from datetime import datetime
from i_recipient_adapter import IRecipientAdapter
from recipient import Recipient
from slot import Slot

table_name = os.getenv("TABLE_NAME", "VACCINATION_RESERVATION")
pk_prefix = "recipient#"

'''
implement of Recipient adapter for Amazon DynamoDB
'''
class DDBRecipientAdapter(IRecipientAdapter):
    def __init__(self):
        ddb = boto3.resource('dynamodb')
        self.__table = ddb.Table(table_name)

    def load(self, recipient_id:str) -> Recipient:
        try:
            response = self.__table.get_item(
                Key={'pk': pk_prefix + recipient_id})
            if 'Item' in response:
                item = response['Item']
                email = item['email']
                first_name = item['first_name']
                last_name = item['last_name']
                age = item['age']
                recipient = Recipient(recipient_id, email, first_name, last_name, age)
                print("in the ddb_recipient_adapter")
                print(recipient)

                if 'slots' in item:
                    slots = item['slots']
                    for slot in slots:
                        print(slot)

                        slot_id = slot['slot_id']
                        reservation_date = slot['reservation_date']
                        location = slot['location']
                        recipient.add_reserve_slot(Slot(
                            slot_id, 
                            datetime.strptime(reservation_date, '%Y-%m-%d %H:%M:%S'), 
                            location))

                return recipient
                
            print("Item not found!")
            return None

        except ClientError as e:
            print(e.response['Error']['Message'])
            return None
        except Exception as e:
            print(e)
            return None

    def save(self, recipient:Recipient) -> bool:
        try:
            item = {
                "pk": pk_prefix + recipient.recipient_id,
                "email": recipient.email,
                "first_name": recipient.first_name,
                "last_name": recipient.last_name,
                "age": recipient.age,
                "slots": []
            }
            
            slots = recipient.slots
            for slot in slots:
                slot_item = {
                    "slot_id": slot.slot_id,
                    "reservation_date": slot.reservation_date.strftime('%Y-%m-%d %H:%M:%S'),
                    "location": slot.location
                }
                item['slots'].append(slot_item)

            self.__table.put_item(Item=item)
            return True

        except ClientError as e:
            print(e.response['Error']['Message'])
            return False
