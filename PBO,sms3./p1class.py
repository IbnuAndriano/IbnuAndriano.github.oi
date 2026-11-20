class Sekolah:
    pass

class Siswa:
    pass

Kepala_sekolah = Sekolah()
Orang_tua = Siswa()

print(type(Kepala_sekolah))
print(type(Orang_tua))

Sir_Ibnu = Sekolah()
Abdul = Siswa()

print(type(Sir_Ibnu))
print(type(Abdul))

Kepala_sekolah = Sekolah()
Kepala_sekolah.umur = 26
Kepala_sekolah.nama = "Sir_Ibnu"

print(Kepala_sekolah.umur)
print(Kepala_sekolah.nama)

Orang_tua = Siswa()
Orang_tua.umur = 49
Orang_tua.nama = "Andriano"

print(Orang_tua.umur)
print(Orang_tua.nama)