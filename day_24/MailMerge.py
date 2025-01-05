
with open("/code/python/Input/people/invited_names.txt") as names:
    name_list = names.readlines() 

with open("/code/python/Input/Letters/starting_letter.txt") as strt_letter:
    letter_content = strt_letter.read()
    for name in name_list:
        stripped_name = name.strip()  #to remove the extra line
        x = letter_content.replace("[name]", stripped_name)
        with open(f"/code/python/Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as letter:
            letter.write(x)


