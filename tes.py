
list_cash_flow = [ 2500000, 5000000, -1000000, -2500000, 5000000, 10000000, -5000000, 7500000, 10000000, -1500000, 25000000, -2500000]
list_cash_flow.append(-1000000)


total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana
total_pengeluaran *= -1

sisa_kas = total_pemasukan - total_pengeluaran
total_kas_bulan_lalu = 50000000

print("Keadaan keuangan bulan ini")
print(f"Total pengeluaran = {total_pengeluaran}") 
print("Total pemasukkan =", total_pemasukan)

if sisa_kas > total_kas_bulan_lalu:
    print("Total sisa kas = " + str(sisa_kas) + " Surplus")
else:
    print("Total sisa kas = " + str(sisa_kas) + " Defisit")

