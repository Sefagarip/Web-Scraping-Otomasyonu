# Web Scraping Otomasyonu

Bu proje, web sitelerinden veri çekme ve otomatik işlemler gerçekleştirme amacıyla geliştirilmiş Selenium tabanlı kapsamlı bir otomasyon aracıdır. Kullanıcı dostu arayüzü ile teknik bilgisi olmayan kişilerin bile kolayca web scraping ve otomasyon işlemleri yapabilmesini sağlar.

## Özellikler

- **Kolay Kullanım**: Menü tabanlı Türkçe arayüz ile kolayca otomasyon işlemleri yapabilme
- **Web Tarama**: Web sitelerinde gezinme, etkileşim ve veri çekme
- **Veri Toplama**: Metin okuma, tablo verilerini CSV/Excel'e aktarma
- **Resim İndirme**: Web sitelerinden resimleri otomatik olarak indirme
- **Kombinasyon Özelliği**: Birden fazla işlemi sırayla otomatik olarak gerçekleştirme
- **Parametreleri Hatırlama**: Aynı işlemleri tekrar gerçekleştirmek için önceki parametreleri kullanabilme

## Kurulum

1. Python'u [python.org](https://www.python.org/downloads/) adresinden indirip kurun.
2. Projeyi indirin veya klonlayın:
   ```
   git clone https://github.com/Sefagarip/Web-Scraping-Otomasyonu.git
   cd Web-Scraping-Otomasyonu
   ```
3. Gerekli bağımlılıkları yükleyin:
   ```
   pip install -r requirements.txt
   ```

## Kullanım

Programı çalıştırmak için:

```
python "web scraping otomasyonu.py"
```

### Ana Menü Seçenekleri

1. **Tarayıcı başlat**: Chrome tarayıcısını açar
2. **URL'ye git**: Belirtilen web adresine gider
3. **Elemente tıkla**: Seçilen HTML elementine tıklar
4. **Metin yaz**: Belirtilen elemente metin yazar
5. **Enter tuşu gönder**: Enter tuşu gönderir
6. **Özel tuş gönder**: ENTER, TAB, ESC gibi özel tuşlar gönderir
7. **Metin oku**: Belirtilen elementin metnini okur
8. **Çoklu metin oku**: Birden fazla elementin metnini okur
9. **Bekleme süresi ekle**: Belirtilen süre kadar bekler
10. **Tablo oku**: HTML tablosunu bulup pandas DataFrame'e dönüştürür
11. **Tüm tablolarda veri oku**: Sayfalama yaparak tüm tablolardaki verileri toplar
12. **Scroll yap**: Sayfada veya element içinde aşağı/yukarı kaydırma yapar
13. **Yeni sekme aç**: Yeni bir sekme açar
14. **Sekme değiştir**: Belirtilen sekmeye geçiş yapar
15. **Aktif sekmeyi kapat**: Mevcut sekmeyi kapatır
16. **Resimleri indir**: Seçilen resim elementlerini bilgisayara indirir
17. **Tarayıcıyı kapat**: Chrome tarayıcısını kapatır
18. **Kombinasyon Çalıştır**: Birden fazla adımı otomatik olarak sırayla çalıştırır

### Kombinasyon Kullanımı

Kombinasyon özelliği sayesinde birçok işlemi sırayla otomatik olarak gerçekleştirebilirsiniz:

1. Ana menüden "18. Kombinasyon Çalıştır" seçeneğini seçin
2. Yapmak istediğiniz işlemlerin numaralarını boşlukla ayırarak girin (örn: "3 12 9 7")
3. Program sırayla her adımı çalıştıracak ve gerekli bilgileri sizden isteyecektir
4. Aynı adımı tekrar kullandığınızda, önceki bilgileri kullanıp kullanmamayı seçebilirsiniz

### Örnek Kullanım Senaryosu

Bir web sitesindeki ürün bilgilerini toplamak için:
1. Tarayıcıyı başlat
2. E-ticaret sitesine git
3. Arama kutusuna tıkla 
4. "Telefon" yazıp ara
5. Sonuçları tablo olarak oku
6. Verileri Excel'e aktar

## Bağımlılıklar

- Python 3.6+
- Selenium
- pandas
- webdriver-manager
- requests

## İletişim

Sorularınız veya önerileriniz için [GitHub Issues](https://github.com/Sefagarip/Web-Scraping-Otomasyonu/issues) bölümünü kullanabilirsiniz.
