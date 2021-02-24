import itertools

for n in range(1, 4):
    my_iter = itertools.combinations(flower_names, n)
    for i in my_iter:
        print(i)