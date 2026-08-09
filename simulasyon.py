import numpy as np
import matplotlib.pyplot as plt

# 1) Rastgele bit dizisi üret
np.random.seed(42)
bit_sayisi = 20
bitler = np.random.randint(0, 2, bit_sayisi)
print("Gönderilen bitler:", bitler)

# 2) Bitleri ikişerli gruplara ayır
if bit_sayisi % 2 != 0:
    bitler = np.append(bitler, 0)
bit_ciftleri = bitler.reshape(-1, 2)
print("İkili gruplar:\n", bit_ciftleri)

# 3) Her ikili grubu bir faza (noktaya) çevir
def bitleri_faza_cevir(cift):
    b1, b2 = cift
    if b1 == 0 and b2 == 0:
        return 0
    elif b1 == 0 and b2 == 1:
        return np.pi / 2
    elif b1 == 1 and b2 == 1:
        return np.pi
    else:
        return 3 * np.pi / 2

fazlar = np.array([bitleri_faza_cevir(cift) for cift in bit_ciftleri])
print("Fazlar (radyan):", fazlar)





# 4) Her faz için gerçek bir dalga oluştur ve yan yana diz
ornekleme_hizi = 100  # her sembol için kaç örnek nokta kullanacağız
frekans = 5  # taşıyıcı dalga frekansı

tum_sinyal = []
for faz in fazlar:
    t = np.linspace(0, 1, ornekleme_hizi)
    dalga = np.cos(2 * np.pi * frekans * t + faz)
    tum_sinyal.extend(dalga)

tum_sinyal = np.array(tum_sinyal)

# 5) Sinyali çiz
plt.figure(figsize=(12, 4))
plt.plot(tum_sinyal)
plt.title('QPSK Modüle Edilmiş Sinyal')
plt.xlabel('Örnek Numarası')
plt.ylabel('Genlik')
plt.grid(alpha=0.3)
plt.show()




# 6) Sinyale gürültü ekle (gerçek dünya kanalını simüle ediyoruz)
gurultu_seviyesi = 20
gurultu = gurultu_seviyesi * np.random.normal(0, 1, len(tum_sinyal))
gurultulu_sinyal = tum_sinyal + gurultu

# Temiz ve gürültülü sinyali karşılaştır
plt.figure(figsize=(12, 4))
plt.plot(tum_sinyal, label='Temiz Sinyal', alpha=0.7)
plt.plot(gurultulu_sinyal, label='Gürültülü Sinyal', alpha=0.7)
plt.title('Kanal Üzerinden Geçiş: Temiz ve Gürültülü Sinyal')
plt.xlabel('Örnek Numarası')
plt.ylabel('Genlik')
plt.legend()
plt.grid(alpha=0.3)
plt.show()



# 7) Alıcı taraf: gürültülü sinyalden fazı tahmin et
def faza_ait_bitleri_bul(faz):
    olası_fazlar = [0, np.pi/2, np.pi, 3*np.pi/2]
    olası_bitler = [[0,0], [0,1], [1,1], [1,0]]
    farklar = [abs(faz - of) for of in olası_fazlar]
    en_yakin_index = np.argmin(farklar)
    return olası_bitler[en_yakin_index]

tahmini_bitler = []
sembol_sayisi = len(fazlar)

for i in range(sembol_sayisi):
    baslangic = i * ornekleme_hizi
    bitis = baslangic + ornekleme_hizi
    sembol_sinyali = gurultulu_sinyal[baslangic:bitis]

    # Bu sembolün fazını tahmin et (basit korelasyon yöntemiyle)
    t = np.linspace(0, 1, ornekleme_hizi)
    en_iyi_faz = None
    en_yuksek_benzerlik = -np.inf

    for aday_faz in [0, np.pi/2, np.pi, 3*np.pi/2]:
        referans_dalga = np.cos(2 * np.pi * frekans * t + aday_faz)
        benzerlik = np.sum(sembol_sinyali * referans_dalga)
        if benzerlik > en_yuksek_benzerlik:
            en_yuksek_benzerlik = benzerlik
            en_iyi_faz = aday_faz

    bit_cifti = faza_ait_bitleri_bul(en_iyi_faz)
    tahmini_bitler.extend(bit_cifti)

tahmini_bitler = np.array(tahmini_bitler)
print("\nGerçek bitler:  ", bitler)
print("Tahmin edilen:  ", tahmini_bitler)

# 8) Hata oranını hesapla
hatalar = np.sum(bitler != tahmini_bitler)
hata_orani = hatalar / len(bitler)
print(f"\nToplam bit sayısı: {len(bitler)}")
print(f"Yanlış tahmin edilen bit sayısı: {hatalar}")
print(f"Hata oranı (BER): {hata_orani:.2%}")




# 9) BER vs Gürültü Seviyesi grafiği (eşik etkisini görselleştir)
def tek_simulasyon_calistir(gurultu_sev, bit_sayisi_test=1000):
    np.random.seed(1)  # her seferinde farklı ama karşılaştırılabilir olsun
    test_bitler = np.random.randint(0, 2, bit_sayisi_test)
    if bit_sayisi_test % 2 != 0:
        test_bitler = np.append(test_bitler, 0)
    test_ciftler = test_bitler.reshape(-1, 2)
    test_fazlar = np.array([bitleri_faza_cevir(c) for c in test_ciftler])

    test_sinyal = []
    for faz in test_fazlar:
        t_test = np.linspace(0, 1, ornekleme_hizi)
        test_sinyal.extend(np.cos(2 * np.pi * frekans * t_test + faz))
    test_sinyal = np.array(test_sinyal)

    test_gurultu = gurultu_sev * np.random.normal(0, 1, len(test_sinyal))
    test_gurultulu = test_sinyal + test_gurultu

    tahmin = []
    for i in range(len(test_fazlar)):
        b = i * ornekleme_hizi
        e = b + ornekleme_hizi
        sembol = test_gurultulu[b:e]
        t_test = np.linspace(0, 1, ornekleme_hizi)
        en_iyi, en_yuksek = None, -np.inf
        for aday in [0, np.pi/2, np.pi, 3*np.pi/2]:
            ref = np.cos(2 * np.pi * frekans * t_test + aday)
            benzerlik = np.sum(sembol * ref)
            if benzerlik > en_yuksek:
                en_yuksek, en_iyi = benzerlik, aday
        tahmin.extend(faza_ait_bitleri_bul(en_iyi))

    tahmin = np.array(tahmin)
    return np.sum(test_bitler != tahmin) / len(test_bitler)

gurultu_araligi = np.linspace(0, 4, 20)
ber_sonuclari = [tek_simulasyon_calistir(g) for g in gurultu_araligi]

plt.figure(figsize=(9, 5))
plt.plot(gurultu_araligi, ber_sonuclari, marker='o', color='#dc2626')
plt.title('Hata Oranı (BER) vs Gürültü Seviyesi')
plt.xlabel('Gürültü Seviyesi')
plt.ylabel('Hata Oranı (BER)')
plt.grid(alpha=0.3)
plt.show()