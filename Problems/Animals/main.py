file = open('animals.txt', 'r', encoding='utf-8')

results = [line.rstrip("\n") + ' ' for line in file.readlines()]

new_file = open('animals_new.txt', 'w', encoding='utf-8')

for i in results:
    new_file.write(i)

file.close()
new_file.close()