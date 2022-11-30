#Convert string to bytes with bytes(str, enc, error)
message = "Test Message" #Message only in English. UTF-8 doesn't support "å,ä,ö"
message_encoded = bytes(message, 'UTF-8')
array_with_byte_message = []

#Decoding the message
for bytes in message_encoded:
    array_with_byte_message.append(bytes)

     