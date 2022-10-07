#Convert string to bytes with bytes(str, enc, error)
message = "Oscar är bäst"
message_encoded = bytes(message, 'UTF-8')

#Printing the encoded message
print(message_encoded)

#Decoding the message
for bytes in message_encoded:
    print(bytes, end = ' ')