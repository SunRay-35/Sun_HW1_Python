# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Данная программы выводит таблицу истинности для утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
print()
truth_table = [['X'.ljust(27)],['Y'.ljust(27)],['Z'.ljust(27)],['¬X'.ljust(27)],['¬Y'.ljust(27)],['¬Z'.ljust(27)],['X ⋁ Y'.ljust(27)],['X ⋁ Y ⋁ Z'.ljust(27)],['¬X ⋀ ¬Y'.ljust(27)],['¬(X ⋁ Y ⋁ Z)'.ljust(27)],['¬X ⋀ ¬Y ⋀ ¬Z'.ljust(27)],['¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z']]
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
                truth_table[0].append(x)
                truth_table[1].append(y)
                truth_table[2].append(z)
                truth_table[3].append(int(not x))
                truth_table[4].append(int(not y))
                truth_table[5].append(int(not z))
                temp1 = int(x or y)
                truth_table[6].append(temp1)
                temp1 = int(temp1 or z)
                truth_table[7].append(temp1)
                temp1 = int(not temp1)
                truth_table[9].append(temp1)
                temp2 = int(not x and not y)
                truth_table[8].append(temp2)
                temp2 = int(temp2 and not z)
                truth_table[10].append(temp2)
                temp1 = int(temp1 == temp2)
                truth_table[11].append(int(temp1))
for i in range(0, len(truth_table)):
    for j in range(0, len(truth_table[i])):
        print(truth_table[i][j], end='\t')