import texttable as tt
tab = tt.Texttable()
headings = ['Pekerjaan', 'Waktu Proses (hari)', 'Batas Waktu (hari)']
tab.header(headings)
pekerjaan = ['1', '2', '3', '4', '5']
waktu_proses_hari = [24, 18, 25, 21, 44]
batas_waktu_hari = [24, 18, 25, 21, 44]

for row in zip(pekerjaan,waktu_proses_hari,batas_waktu_hari):
    tab.add_row(row)

s = tab.draw()
print (s)