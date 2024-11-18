# Ini ke 1
my_dict = {}

my_dict = {'nama' : 'Hilmi', 'usia' : 20, 'kota' : 'Bandung'}

print(f"Nama saya adalah : {my_dict['nama']}")
print(f"umur saya : {my_dict['Usia']} ")

print(f"Kota kelahiran saya : {my_dict['Kota']}")
nama = my_dict['nama']
usia = my_dict['usia']
kota = my_dict['kota']

# print(f"nama saya {nama} umur saya {usia} tempat tinggal saya {kota}")
my_dict = {'nama' : 'Hilmi', 'usia' : 20, 'kota' : 'Bandung'}

## Cara menambahkan item baru 
my_dict['pekerjaan'] = 'Programmer'


## Memodifikasi Item yang ada 
my_dict['usia'] = 26


## Menghapus item dengan dell hilang key dan value nya 
del my_dict['kota']
my_dict

## Menggunakan pop untuk menghapus dan mendapatkan nilai yang hilang hanya key nya saja 
usia = my_dict.pop('kota')
print(usia)



# kedua

dict1 = {'a' : 1, 'b' : 2}
dict2 = {'a' : 3, 'b' : 4}
dict1.update(dict2)
dict1

# ketiga 
my_dict = {'nama' : 'Hilmi', 'usia' : 20, 'kota' : 'Bandung'}

for i in my_dict:
    print(i, my_dict[i])

# ke empat 
my_dict = {'nama' : 'Hilmi', 'usia' : 20, 'kota' : 'Bandung'}

for i in my_dict:
    print(i)

# ke lima 
my_dict = {'nama' : 'Hilmi', 'usia' : 20, 'kota' : 'Bandung'}

for i in my_dict.values():
    print(i)

# ke enam 

my_dict = {'nama' : 'diash', 'usia' : 25, 'kota' : 'Ujungberung'}
my_dict['nama'] = 'firdaus'
my_dict

# ke tujuh

for u, i in my_dict.items():
    print(u,i)

# ke delapan 

dictionary_banyak = { 
    'orang1' : {'nama' : 'Diash', 'usia' : 30, 'kota' : 'Bandung'}, 
    'orang2' : {'nama' : 'Hilmi', 'usia' : 20, 'kota' : 'Bandung'}
}
# print(dictionary_banyak['orang1'] ['nama'])

nama1 = dictionary_banyak['orang1'] ['nama']
usia1 = dictionary_banyak['orang1'] ['usia']
kota1 = dictionary_banyak['orang1'] ['kota']

nama2 = dictionary_banyak['orang2'] ['nama']
usia2 = dictionary_banyak['orang2'] ['usia']
kota2 = dictionary_banyak['orang2'] ['kota']


print(f"nama orang ke 1 adalah {nama1} & usianya adalah {usia1} Kota dia di {kota1}")
print(f"nama orang ke 2 adalah {nama2} & usia nya adalah {usia2} Kota dia di {kota2}")

# ke sembilan

dictionary_banyak = { 
    'orang1' : {'nama' : 'Diash', 'usia' : 30, 'kota' : 'Bandung'}, 
    'orang2' : {'nama' : 'Hilmi', 'usia' : 20, 'kota' : 'Bandung'}
}
for i, j in dictionary_banyak.items():
    print(f"\nID orang1 : {i}")
    print(f"nama:{j['nama']}")