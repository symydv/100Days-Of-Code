import pandas

data = pandas.read_csv("day_26/nato_phonetic_alphabet.csv")

dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(dict)

def generate_phenoetic():
    word = input("Enter a word : ").upper()

    try:
        output_list = [dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phenoetic()
    else:
        print(output_list)

generate_phenoetic()

