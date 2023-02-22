nama = input("masukan nama lengkap andan :")
prodi = input("masukan prodi anda :")
nilai_ = input("masukan nilai (dalam huruf) yang anda dapat :").lower()

try :
    if nilai_ == 'a' : 
     print("Nilai anda adalah 4.0, tbl tbl serem bngt loh")
    elif nilai_ == 'a-' :
        print("Nilai anda 3.75, kamu keren")
    elif nilai_== 'b+' :
        print("nilai anda adalah 3.25")
    elif nilai_== 'b' :
        print("nilai anda adalah 3.0")
    elif nilai_ == 'b-' :
        print("nilai anda adalah 2.75, kurang semangat belajar nihh")
    elif nilai_ == 'c+' :
        print("nilai anda adalah 2.25, wokowkokwo sips")
    elif nilai_== 'c' :
        print("nilai anda adalah 2.0, hahahhah dapet c")
    elif nilai_== 'd' :
        print("nilai anda adalah 1.0, apakah sudah ada pikiran untuk pindah jurusan?")
    elif nilai_== 'e' :
        print("nilai anda adalah 0, niat kuliah ga sih??")
except :
    print("input nilai anda tidak valid")