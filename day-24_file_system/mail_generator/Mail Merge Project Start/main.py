#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"

with open("./day-24_file_system\\mail_generator\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt", mode='r') as file:
    letter = file.read()
    

with open("./day-24_file_system\\mail_generator\\Mail Merge Project Start\\Input\\Names\\invited_names.txt", mode='r') as file:
    names = []
    for name in file.readlines():
        names.append(name.strip())
    

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
for name in names:
    # Create a copy of the letter list
    new_letter = letter.replace(PLACEHOLDER, name)
    with open(f"./day-24_file_system/mail_generator/Mail Merge Project Start/Input/ReadyToSend/letter_to_{name}.txt", mode='w') as file:
        file.write(new_letter)

#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp