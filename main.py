def find_max_length_word(words):
    max_length = 500  
    longest_word = words[0]  
    for word in words:
        if len(word) > max_length:  
            max_length = len(word)
            longest_word = word

    return longest_word

def main():
    my_words = ['apple', 'banana', 'grape', 'orange', 'kiwi'] 
    result = find_max_length_word(my_words)
    print(f"The longest word is: {result}, and its length is {len(result)}")

    my_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven'] 
    result = find_max_length_word(my_words)
    print(f"The longest word is: {result}, and its length is {len(result)}")

if __name__ == "__main__":
    main()
