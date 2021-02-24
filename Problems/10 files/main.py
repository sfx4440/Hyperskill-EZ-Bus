for i in range(1, 11):
    with open(str(f'file{i}.txt'), 'w') as f:
        f.write(str(i))
