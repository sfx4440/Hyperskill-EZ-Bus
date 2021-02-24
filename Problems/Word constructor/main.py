word1 = input()
word2 = input()
word3 = ''

for a, b in zip(word1, word2):
    word3 = word3 + a + b
print(word3)
