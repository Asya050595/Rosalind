AA = int(input())
Aa = int(input())
aa = int(input())

total = AA + Aa + aa

probabily = (4 * (AA * (AA - 1) + 2 * AA * Aa + 2 * AA * aa + Aa * aa) + 3 * Aa * (Aa - 1)) / (4 * total * (total-1))

print(probabily)
