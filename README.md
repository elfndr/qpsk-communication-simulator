# QPSK Haberleşme Simülasyonu

Python ile geliştirilmiş, uçtan uca bir QPSK (Quadrature Phase Shift Keying)
modülasyon/demodülasyon simülasyonu. Rastgele bit verisini QPSK ile modüle
eder, gürültülü bir kanaldan geçirir, demodüle eder ve hata oranını (BER)
ölçer.

## Neler Yapıyor?
- Rastgele bit dizisi üretir
- Bitleri QPSK fazlarına (0°, 90°, 180°, 270°) kodlar
- Fazlardan gerçek sinüs dalgaları oluşturur
- Kanal gürültüsü ekler (AWGN - Additive White Gaussian Noise benzeri)
- Korelasyon tabanlı demodülasyon ile orijinal bitleri geri çözer
- Bit Hata Oranını (BER) hesaplar
- Farklı gürültü seviyelerinde BER'in nasıl değiştiğini grafikle gösterir
- I/Q constellation diyagramı çizerek alınan sembollerin ideal noktalara
  göre dağılımını görselleştirir
- Simülasyon sonuçlarını teorik QPSK BER formülüyle karşılaştırır

## Öne Çıkan Sonuçlar

**Eşik Etkisi:** Simülasyon, dijital haberleşme sistemlerinin karakteristik
"eşik etkisini" gösteriyor: belirli bir gürültü seviyesine kadar sistem
hatasız çalışıyor, o eşiği geçince hata oranı hızla artıyor.

**Constellation Diyagramı:** Düşük gürültüde alınan semboller ideal
noktaların (0°, 90°, 180°, 270°) çok yakınında sıkı bir küme oluştururken,
yüksek gürültüde noktalar dağılıp komşu bölgelere kayıyor — bu da yüksek
hata oranının görsel açıklaması.

**Teorik Formül Karşılaştırması:** Alıcıda kullanılan 100 örnekli
entegrasyon (matched filter benzeri korelasyon), sistemi standart teorik
QPSK formülünün varsaydığından daha dayanıklı hale getiriyor. Bu kazancı
telafi etmek için teorik formüle bir düzeltme çarpanı eklendi; yine de
iki eğri arasında birebir sayısal örtüşme yerine benzer eğilim (eşik
davranışı) gözlemleniyor. Tam örtüşme için sinyal gücü normalizasyonunun
daha titiz hesaplanması gerekir.

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