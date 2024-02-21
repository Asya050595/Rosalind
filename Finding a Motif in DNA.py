def finding_a_motif_in_DNA(s, t):
    list_num = [i for i in range(len(s)) if s.startswith(t, i)]
    list_num_2 = [i + 1 for i in list_num]
    return str(list_num_2)[1:-1]

s = input()
t = input()
print(finding_a_motif_in_DNA(s,t))

