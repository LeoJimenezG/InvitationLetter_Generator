KEYWORD = "[name]"
# Open the file with the names on it
with open(file="../input/names/names_list.txt", mode="r") as names:
    # Save the names as a list
    names_list = names.readlines()

# Open the file with the letter text
with open(file="../input/letter/starting_letter.txt", mode="r") as letter:
    # Save the text as a list
    letter_text = letter.readlines()

# Use all names to write the letters
for person in names_list:
    # Create a new list to avoid modifying the original one
    new_letter = []
    for text_line in letter_text:
        new_letter.append(text_line)
    # Delete any blank space in the name
    person_name = person.strip()
    # Replace the first line with the person name
    new_letter[0] = new_letter[0].replace(KEYWORD, person_name)
    # Create a new file with the name of each person
    with open(file=f"ready_letters/invitation_letter_{person_name}.txt", mode="a") as invitation:
        # Write each line of the new letter
        for line in new_letter:
            invitation.write(line)
