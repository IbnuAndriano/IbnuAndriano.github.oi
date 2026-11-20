class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nama, nim): 
        self.nama = nama
        self.nim = nim



mhs = Mahasiswa("Ibnu Andriano", "14022500088")
print(mhs.nama)
print(mhs.nim)