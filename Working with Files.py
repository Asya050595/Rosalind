output = []

with open("/home/asik/rosalind_ini5.txt", 'r') as my_file:
    output = [line for i, line in enumerate(my_file.readlines()) if i % 2 != 0]

with open('/home/asik/output_file.txt', 'w') as out:
    out.write(''.join(i for i in output))
