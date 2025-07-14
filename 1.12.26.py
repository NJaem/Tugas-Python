def jumlah_rekursif(n):
    if n == 1:
        return 1
    return n + jumlah_rekursif(n - 1)
print(jumlah_rekursif(10))