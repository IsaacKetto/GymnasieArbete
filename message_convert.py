#Convert string to bytes with bytes(str, enc, error)
message = "hej kuksugare"
message_encoded = bytes(message, 'UTF-8')
array_with_byte_message = []

#Printing the encoded message
print(message_encoded)

#Decoding the message
for bytes in message_encoded:
    array_with_byte_message.append(bytes)

     