passwords = input().split()

passwords.sort(key=len)

for i in passwords:
    print(i, len(i))
