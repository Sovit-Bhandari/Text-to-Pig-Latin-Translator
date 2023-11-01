'''Name = Sovit Bhandari
U-number= U83561265
Brief discription = The following code works as a translator to convert the text within the file into piglatin'''

def convert_to_pig_latin(contents):
    # Split the contents into words and convert to lowercase
    words = contents.split()
    
    # Iterate over each word and convert it to Pig Latin
    pig_latin_words = []
    for word in words:
        # Handle punctuation at the end of the word
        punctuation = ''
        while word and not word[-1].isalpha():
            punctuation = word[-1] + punctuation
            word = word[:-1]
        
        # Convert the word to Pig Latin
        if word:
            pig_latin_word = word[1:] + word[0] + 'ay' + punctuation
        else:
            # Handle single-letter words
            pig_latin_word = 'ay' + punctuation
        
        pig_latin_words.append(pig_latin_word)
    
    # Reconstruct the contents using spaces as separators
    pig_latin_contents = ' '.join(pig_latin_words)
    return pig_latin_contents

def main():
    # Prompt the user for the name of a text file
    input_file_name = input("Please enter the name of a text file: ")
    
    # Read the contents of the file
    with open(f'{input_file_name}.txt', 'r') as file:
        contents = file.read()
    
    # Convert the contents to Pig Latin
    pig_latin_contents = convert_to_pig_latin(contents.lower())  # Convert to lowercase as per the prompt
    
    # Prompt the user for the name of the output text file
    output_file_name = input("Please enter the name of the output text file: ")
    
    # Write the converted contents to the output file
    with open(output_file_name, 'w') as file:
        file.write(pig_latin_contents)

if __name__ == "__main__":
    main()