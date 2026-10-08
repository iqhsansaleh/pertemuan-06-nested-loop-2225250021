print("Tabel Perkalian dan Statistik")
n = int(input("n: "))

while n <= 0:
    n = int(input("n: "))

total_semua = 0
count_genap = 0

for i in range(1, n + 1):
    total_baris = 0
    
    for j in range(1, n + 1):
        hasil = i * j
        total_baris += hasil
        total_semua += hasil
        
        if hasil % 2 == 0:
            count_genap += 1
            
        print(f"{hasil}\t", end="")
        
    print(f"| Jumlah Baris: {total_baris}")

print(f"\nTotal semua: {total_semua}")
print(f"Banyak hasil genap: {count_genap}")