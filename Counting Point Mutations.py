def point_mutations_sum(text1, text2):
    count = 0
    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] != text2[j] and i == j:
                count += 1
    return count


text1 = input()
text2 = input()
print(point_mutations_sum(text1, text2))
