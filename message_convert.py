#Convert string to bytes with bytes(str, enc)
message = "10 words to hide in a really cool red picture 10 words to hide in a really cool red picture"
message_encoded = bytes(message, 'UTF-8')
array_with_byte_message = []

#Printing the encoded message
print(message_encoded)

#Decoding the message
for bytes in message_encoded:
    array_with_byte_message.append(bytes)

print(array_with_byte_message)

#Decoding message from image file
