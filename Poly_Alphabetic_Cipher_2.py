import string

letters = string.ascii_uppercase
plane_text = input("Enter a text you want to enc: ").upper()
num_keys = input("Enter an number of keys: ")

block_size = int(num_keys)
new_text = ""
for indx in range(0,len(plane_text),block_size) :
    letter = plane_text[indx]
    for key_num in range(block_size):
        if indx+key_num >= len(plane_text): break
        shift_size = letters.index(plane_text[indx+key_num]) + (key_num+1)*2 +1
        if shift_size >= len(letters): shift_size = shift_size - len(letters)
        letter_new_indx = letters[shift_size]
        new_text = new_text + letter_new_indx

print("New text: ",new_text)
print("Plain text: ",plane_text.lower())
