def get_new_sentence(random_sentence, vowels):
    new_sentence = ""
    for word in random_sentence:
        new_word = ""
        word_length = len(word)
        for i in range(word_length):
            if word[i].lower() in vowels:
                new_word = word[i:] + new_word
                break
            else:
                new_word += word[i]
        new_sentence += new_word + " "
    return (new_sentence)
def main():
    random_sentence = input().split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_sentence = get_new_sentence(random_sentence, vowels)
    print(new_sentence)
main()
