with open('dataset_3363_4.txt', 'r', encoding='utf-8') as file:
    data_school = {}
    for line in file:
        data_school[tuple(line.strip().split(';',maxsplit=1))[0]]=line.strip().split(';',maxsplit=1)[1].split(';')
    for i in data_school.values():
        for j in i:
            i[i.index(j)] = int(j)
    with open('result.txt', 'w') as res:
        some_lst = []
        # count = len()
        for i in data_school.values():
            res.write(f'{sum(i)/len(i)}'+'\n')
            some_lst.append(i)
        for i in range(len(some_lst)):
            for j in range(len(some_lst[i])):
                print(some_lst[i][j],end=' ')
            print()