plat_no = input("Masukan plat nomor : ").split(' ')


try :   
    x = int(plat_no[1])
    if x >= 0 and x <= 3000 :
        print("Plat nomor tersebut diperuntukan untuk mobil")
    elif x >= 3001 and x <= 4000 :
        print("Plat nomor tersebut diperuntukan untuk motor")
    elif x >= 4001 and x <= 5000 :
        print("Plat nomor tersebut diperuntukan untuk angkutan umum")        
except : 
    print("Plat nomor tidak terindikasi, harus terdapat nomor kendaraan setelah kode daerah")