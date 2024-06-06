from twilio.rest import Client
from datetime import datetime

# Twilio credentials
account_sid = 'AC00ce379ae06d3704998f4f5e7728b472'  # Replace with your Twilio account SID
auth_token = 'f4d64dbb130f2e6fae457f31d314a1d9'  # Replace with your Twilio Auth Token
twilio_phone_number = '+12183667851'  # Replace with your Twilio phone number
destination_phone_number = '+918792554085'  # Replace with the recipient's phone number

# Generate slot number and get current datetime
slot_number = '99699'  # Replace this with the actual slot number
current_time = datetime.now().strftime('%H:%M:%S')
current_date = datetime.now().strftime('%Y-%m-%d')

# Prepare message body
message_body = f"Your slot number {slot_number} has been booked on {current_time} and {current_date}."

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Send the message
message = client.messages.create(
    body=message_body,
    from_=twilio_phone_number,
    to=destination_phone_number
)

# Output message SID for verification
print(f"Message Successfully Sent With SID: {message.sid}")
