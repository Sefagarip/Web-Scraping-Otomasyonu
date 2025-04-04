# Web Scraping Automation - Web Scraping Otomasyonu

📌📌 Read this in: [English](#web-scraping-automation) | [Türkçe](#web-scraping-otomasyonu)

## Web Scraping Automation
This project is a comprehensive Selenium-based automation tool developed for web scraping and performing automated operations on websites. With its user-friendly interface, it allows even those without technical knowledge to easily perform web scraping and automation tasks.

### Features

- **Easy to Use**: Menu-based interface for simple automation operations
- **Web Browsing**: Navigate through websites, interact with elements and extract data
- **Data Collection**: Reading text, exporting table data to CSV/Excel
- **Image Download**: Automatically download images from websites
- **Combination Feature**: Perform multiple operations in sequence automatically
- **Parameter Memory**: Ability to reuse previous parameters for repeating the same operations

### Installation

1. Download and install Python from [python.org](https://www.python.org/downloads/)
2. Download or clone the project:
   ```
   git clone https://github.com/Sefagarip/Web-Scraping-Otomasyonu.git
   cd Web-Scraping-Otomasyonu
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

To run the program:

```
python "web scraping otomasyonu.py"
```

#### Main Menu Options

1. **Start browser**: Opens Chrome browser
2. **Go to URL**: Navigates to the specified web address
3. **Click on element**: Clicks on the selected HTML element
4. **Write text**: Writes text to the specified element
5. **Send Enter key**: Sends the Enter key
6. **Send special key**: Sends special keys like ENTER, TAB, ESC
7. **Read text**: Reads the text of the specified element
8. **Read multiple texts**: Reads text from multiple elements
9. **Add waiting time**: Waits for the specified duration
10. **Read table**: Finds an HTML table and converts it to a pandas DataFrame
11. **Read data from all tables**: Collects data from all tables with pagination
12. **Scroll**: Scrolls up/down within the page or an element
13. **Open new tab**: Opens a new tab
14. **Switch tab**: Switches to the specified tab
15. **Close active tab**: Closes the current tab
16. **Download images**: Downloads selected image elements to the computer
17. **Close browser**: Closes the Chrome browser
18. **Run Combination**: Runs multiple steps automatically in sequence

#### Using Combinations

With the combination feature, you can perform multiple operations in sequence automatically:

1. Select "18. Run Combination" from the main menu
2. Enter the numbers of the operations you want to perform separated by spaces (e.g., "3 12 9 7")
3. The program will run each step in sequence and ask you for the necessary information
4. When you use the same step again, you can choose whether to use the previous information

#### Example Usage Scenario

To collect product information from a website:
1. Start the browser
2. Go to an e-commerce site
3. Click on the search box
4. Write "Phone" and search
5. Read the results as a table
6. Export the data to Excel

### Dependencies

- Python 3.6+
- Selenium
- pandas
- webdriver-manager
- requests

### Contact

For questions or suggestions, you can use the [GitHub Issues](https://github.com/Sefagarip/Web-Scraping-Otomasyonu/issues) section.


## Web Scraping Otomasyonu

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
