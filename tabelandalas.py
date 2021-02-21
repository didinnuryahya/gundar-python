
pekerjaan = ['1', '2', '3', '4', '5']
waktu_proses_hari = [24, 18, 25, 21, 44]
batas_waktu_hari = [24, 18, 25, 21, 44]


titles = ['Pekerjaan', 'Waktu Proses (hari)', 'Batas Waktu (hari)']
data = [titles] + list(zip(pekerjaan, waktu_proses_hari, batas_waktu_hari))

for i, d in enumerate(data):
    line = '|'.join(str(x).ljust(19) for x in d)
    print(line)
    if i == 0:
        print('-' * len(line))
 print('-' * len(line))
