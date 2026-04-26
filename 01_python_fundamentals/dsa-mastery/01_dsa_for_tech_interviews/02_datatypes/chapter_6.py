chai_type = "Ginger Chai"
customer_name= "Arpreet"

print(f"Order for {customer_name}:{chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"first word is: {chai_description[0:8]}") # slicing the string to get the first word
print(f"last word is: {chai_description[11:15]}") # slicing the string to get the last word
# using negative indexing to get the last word
print(f"last word is: {chai_description[-4:]}") 

# using slicing to reverse the string
print(f"reversing the string using slicing: {chai_description[::-1]}") 

#encoding and decoding the string
label_text = "Chai spécialité"
encoded_label = label_text.encode("utf-8") # encoding the string to bytes
print(f"original label: {label_text}")
print(f"encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8") # decoding the bytes back to string
print(f"decoded label: {decoded_label}")
