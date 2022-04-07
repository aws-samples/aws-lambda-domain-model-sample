import json
from i_recipient_input_port import IRecipientInputPort
from recipient_input_port import RecipientInputPort
from slot_output_port import SlotOutputPort
from recipient_output_port import RecipientOutputPort
from ddb_recipient_adapter import DDBRecipientAdapter
from ddb_slot_adapter import DDBSlotAdapter

'''
app_config: injector bind the target instances to param
'''
# get a RecipientInpurtPort instance
def get_recipient_input_port():
    return RecipientInputPort(
        RecipientOutputPort(DDBRecipientAdapter()), 
        SlotOutputPort(DDBSlotAdapter()))

def lambda_handler(event, context):
    '''
    API Gateway event adapter

    retrieve reservation request parameters
    ex. '{"recipient_id": "1", "slot_id":"1"}'
    '''
    body = json.loads(event['body'])
    recipient_id = body['recipient_id']
    slot_id = body['slot_id']

    # get an input port instance
    recipient_input_port = get_recipient_input_port()
    status = recipient_input_port.make_reservation(recipient_id, slot_id)
 
    return {
        "statusCode": status.status_code,
        "body": json.dumps({
            "message": status.message
        }),
    }

