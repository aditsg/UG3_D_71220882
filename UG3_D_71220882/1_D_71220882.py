curah = float(input('Masukan nilai curah hujan :'))

hujan = ('Curah hujan lebat' if  curah >= 51 and curah <= 100 else('curah hujan ringan' if curah >= 0.5 and curah <= 20 else ('curah hujan sedang' if curah >= 21 and curah <= 50 else('curah hujan lebat' if curah >= 100 else('cuaca terang/berawan' if curah == '0' else(print('salah input')))))))
print(hujan)