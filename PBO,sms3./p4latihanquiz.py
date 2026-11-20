import time
import random

def jeda():
    time.sleep(random.uniform(0.8, 1.8))

def ngobrol():
    print("=" * 55)
    print("   CHAT: IBNU & ANDRIANO")
    print("=" * 55)
    print()

    percakapan = [
        ("Ibnu",      "no, tadi lu masuk kelas Statistika ga?"),
        ("Andriano",  "masuk lah, tapi telat 15 menit wkwk"),
        ("Ibnu",      "lah telat lagi, padahal dosennya galak banget itu"),
        ("Andriano",  "iya tau, untung ga ketauan. lu gimana, masuk?"),
        ("Ibnu",      "masuk dong, cuma bingung sama materi uji hipotesis"),
        ("Andriano",  "sama, gua juga ga ngerti. tadi lu nyatet ga?"),
        ("Ibnu",      "nyatet sih, tapi tulisan gua kayak ceker ayam"),
        ("Andriano",  "wkwk, nanti minjem ya, gua foto aja"),
        ("Ibnu",      "boleh, tapi jangan lupa traktir indomaret"),
        ("Andriano",  "halah, dasar lu. oke deh, nanti gua traktir"),
        ("Ibnu",      "btw besok jadwalnya apa aja? gua lupa cek"),
        ("Andriano",  "pagi Basis Data, terus siang ada Pemrograman Web"),
        ("Ibnu",      "oh iya, tugas Basis Data udah lu kerjain?"),
        ("Andriano",  "belum, masih ngasal. lu?"),
        ("Ibnu",      "belum juga, bingung di bagian normalisasi"),
        ("Andriano",  "sama, 3NF sama BCNF bikin pusing"),
        ("Ibnu",      "nanti malem kerja bareng aja di kos gua?"),
        ("Andriano",  "boleh tuh, gua bawa laptop. jam 7 ya"),
        ("Ibnu",      "oke, sekalian gua mesen kopi"),
        ("Andriano",  "sip, jangan lupa bahan buat tugasnya"),
        ("Ibnu",      "udah gua siapin. ya udah deh, gua mau ke perpus dulu"),
        ("Andriano",  "oke, hati-hati. nanti gua chat lagi kalau udah di kos"),
        ("Ibnu",      "siap no, dadah"),
        ("Andriano",  "dadah"),
    ]

    for pengirim, pesan in percakapan:
        if pengirim == "Ibnu":
            print(f"Ibnu      : {pesan}")
        else:
            print(f"Andriano  : {pesan}")
        jeda()

    print()
    print("=" * 55)
    print("   [Percakapan selesai]")
    print("=" * 55)

if __name__ == "__main__":
    ngobrol()