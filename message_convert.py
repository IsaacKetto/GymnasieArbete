#Convert string to bytes with bytes(str, enc, error)
message = "Oscar is the best"
message_encoded = bytes(message, 'UTF-8')
array_with_byte_message = []

#Printing the encoded message
print(message_encoded)

#Decoding the message
for bytes in message_encoded:
    array_with_byte_message.append(bytes)

print(array_with_byte_message)

#Convert bytes back to string
