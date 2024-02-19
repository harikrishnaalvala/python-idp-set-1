def swap_competition(word):
    word_one = word[0]
    word_two = word[1]
    word_one_swap = sorted(word_one)
    word_two_swap = sorted(word_two)
    if word_one_swap == word_two_swap:
        return "YES"
    else:
        return "NO"
n = int(input())
output = ""
for i in range(n):
    word = input().lower()
    word = word.split()
    result = swap_competition(word)
    output += result + " "
print(output)
    
