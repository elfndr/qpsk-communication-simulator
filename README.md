# QPSK Haberleşme Simülasyonu

Python ile geliştirilmiş bir QPSK (Quadrature Phase Shift Keying)
modülasyon/demodülasyon simülasyonu. Rastgele bir bit dizisini QPSK ile
modüle eder, gürültülü bir kanaldan geçirir, alıcı tarafında demodüle
eder ve hata oranını (BER) hesaplar.

## Özellikler

- Rastgele bit dizisi üretme
- Bitleri QPSK fazlarına (0°, 90°, 180°, 270°) kodlama
- Fazlardan sinüs dalgaları oluşturma
- Kanal gürültüsü ekleme (AWGN benzeri)
- Korelasyon tabanlı demodülasyon
- Bit Hata Oranı (BER) hesaplama
- Farklı gürültü seviyelerinde BER değişimini gösteren grafik
- I/Q constellation diyagramı
- Simülasyon sonuçlarının teorik BER formülüyle karşılaştırılması

## Bulgular

**Eşik etkisi:** Gürültü seviyesini kademeli artırdığımda, hata oranı
doğrusal değil, belirli bir eşiğe kadar sıfırda kalıp sonra aniden
yükseliyor. Bu, dijital haberleşme sistemlerinin tipik bir davranışı.

**Constellation diyagramı:** Düşük gürültüde alınan semboller ideal
noktaların (0°, 90°, 180°, 270°) çok yakınında toplanırken, yüksek
gürültüde noktalar dağılıp komşu bölgelere kayıyor — yüksek hata
oranının görsel karşılığı bu.

**Teorik formülle karşılaştırma:** Alıcıda 100 örnek üzerinden yapılan
entegrasyon (korelasyon), sistemi standart teorik formülün varsaydığından
daha dayanıklı hale getiriyor. Bunu telafi etmek için formüle bir düzeltme
çarpanı ekledim; sonuç olarak iki eğri birebir örtüşmüyor ama aynı eşik
davranışını (genel eğilimi) gösteriyor. Tam sayısal örtüşme için sinyal
gücü normalizasyonunun daha titiz yapılması gerekiyor.

## Kurulum

```bash
pip install numpy matplotlib scipy
```

## Kullanım

```bash
python simulasyon.py
```

## Kullanılan Kütüphaneler
- NumPy
- Matplotlib
- SciPy