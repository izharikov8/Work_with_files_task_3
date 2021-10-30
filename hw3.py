import os

path = os.getcwd()

files = os.listdir(path)
data = {}
for file in files:
    if(file.endswith('.txt')):
        with open(file, encoding='utf-8') as f:
            lines = f.read()
            with open(file, encoding='utf-8') as f:
                file_name = f.name
                count = sum(1 for line in f)
            data[file_name] = (count, lines)
            sorted_dict = {}
            sorted_keys = sorted(data, key=data.get)
            for w in sorted_keys:
                sorted_dict[w] = data[w]


for i in sorted_dict.items():
    with open('4.txt', 'a', encoding='utf-8') as new_file:
        new_file.write(f'{str(i[0])}\n')
        new_file.write(f'{str(i[1][0])}\n')
        new_file.write(f'{str(i[1][1])}\n')









