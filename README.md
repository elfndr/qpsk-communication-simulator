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

## Öne Çıkan Sonuç
Simülasyon, dijital haberleşme sistemlerinin karakteristik "eşik etkisini"
gösteriyor: belirli bir gürültü seviyesine kadar sistem hatasız çalışıyor,
o eşiği geçince hata oranı hızla artıyor.

## Kurulum
```bash
pip install numpy matplotlib
```

## Kullanım
```bash
python simulasyon.py
```

## Kullanılan Kütüphaneler
- NumPy
- Matplotlib