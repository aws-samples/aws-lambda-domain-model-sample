'''
main.py

This code is only used for local testing. 
First, you need to deploy a DynamoDB table to your AWS account. 
For details, see readme.md how to deploy your DynamoDB table and to load initial data. 
Then you can use this code to run and test on local environment.

$ python main.py

'''
from ddb_recipient_adapter import DDBRecipientAdapter
from ddb_slot_adapter import DDBSlotAdapter
from i_recipient_input_port import IRecipientInputPort
from recipient_input_port import RecipientInputPort
from slot_output_port import SlotOutputPort
from recipient_output_port import RecipientOutputPort


def get_recipient_input_port():
    return RecipientInputPort(
        RecipientOutputPort(DDBRecipientAdapter()), 
        SlotOutputPort(DDBSlotAdapter()))

def main():
    recipient_input_port = get_recipient_input_port()
    status = recipient_input_port.make_reservation("1", "1")
    print(f"status_code: {status.status_code}, message: {status.message}")

if __name__ == "__main__":
    main()
