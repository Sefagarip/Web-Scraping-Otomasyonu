from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os

class SeleniumOtomasyon:
    def __init__(self):
        self.driver = None
        self.element_dict = {
            "ID": By.ID,
            "NAME": By.NAME,
            "XPATH": By.XPATH,
            "LINK_TEXT": By.LINK_TEXT,
            "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
            "TAG_NAME": By.TAG_NAME,
            "CLASS_NAME": By.CLASS_NAME,
            "CSS_SELECTOR": By.CSS_SELECTOR
        }
    
    def tarayici_baslat(self):
        """Tarayıcıyı başlatır"""
        print("Tarayıcı başlatılıyor...")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        print("Tarayıcı başlatıldı!")
    
    def url_git(self, url):
        """Belirtilen URL'ye gider"""
        try:
            self.driver.get(url)
            print(f"{url} adresine gidildi.")
            return True
        except Exception as e:
            print(f"URL'ye giderken hata oluştu: {e}")
            return False
    
    def element_bul(self, secici_tipi, secici_degeri, bekleme_suresi=10):
        """Belirtilen seçici türü ve değerine göre elementi bulur"""
        try:
            if secici_tipi not in self.element_dict:
                print(f"Geçersiz seçici tipi: {secici_tipi}. Geçerli tipler: {', '.join(self.element_dict.keys())}")
                return None
            
            by_type = self.element_dict[secici_tipi]
            element = WebDriverWait(self.driver, bekleme_suresi).until(
                EC.presence_of_element_located((by_type, secici_degeri))
            )
            return element
        except TimeoutException:
            print(f"Element bulunamadı: {secici_tipi}={secici_degeri}")
            return None
        except Exception as e:
            print(f"Element bulunurken hata oluştu: {e}")
            return None
    
    def elementleri_bul(self, secici_tipi, secici_degeri, bekleme_suresi=10):
        """Belirtilen seçici türü ve değerine göre birden fazla elementi bulur"""
        try:
            if secici_tipi not in self.element_dict:
                print(f"Geçersiz seçici tipi: {secici_tipi}. Geçerli tipler: {', '.join(self.element_dict.keys())}")
                return []
            
            by_type = self.element_dict[secici_tipi]
            WebDriverWait(self.driver, bekleme_suresi).until(
                EC.presence_of_element_located((by_type, secici_degeri))
            )
            elements = self.driver.find_elements(by_type, secici_degeri)
            return elements
        except TimeoutException:
            print(f"Elementler bulunamadı: {secici_tipi}={secici_degeri}")
            return []
        except Exception as e:
            print(f"Elementler bulunurken hata oluştu: {e}")
            return []
    
    def tikla(self, secici_tipi, secici_degeri, bekleme_suresi=10):
        """Belirtilen elemente tıklar"""
        element = self.element_bul(secici_tipi, secici_degeri, bekleme_suresi)
        if element:
            try:
                WebDriverWait(self.driver, bekleme_suresi).until(
                    EC.element_to_be_clickable((self.element_dict[secici_tipi], secici_degeri))
                )
                element.click()
                print(f"{secici_tipi}={secici_degeri} elementine tıklandı.")
                return True
            except Exception as e:
                print(f"Elemente tıklarken hata oluştu: {e}")
                return False
        return False
    
    def metin_yaz(self, secici_tipi, secici_degeri, metin, bekleme_suresi=10):
        """Belirtilen elemente metin yazar"""
        element = self.element_bul(secici_tipi, secici_degeri, bekleme_suresi)
        if element:
            try:
                element.clear()  # Önce mevcut içeriği temizle
                element.send_keys(metin)
                print(f"{secici_tipi}={secici_degeri} elementine '{metin}' yazıldı.")
                return True
            except Exception as e:
                print(f"Metni yazarken hata oluştu: {e}")
                return False
        return False
    
    def enter_bas(self, secici_tipi, secici_degeri, bekleme_suresi=10):
        """Belirtilen elemente Enter tuşu gönderir"""
        element = self.element_bul(secici_tipi, secici_degeri, bekleme_suresi)
        if element:
            try:
                element.send_keys(Keys.RETURN)
                print(f"{secici_tipi}={secici_degeri} elementine Enter tuşu basıldı.")
                return True
            except Exception as e:
                print(f"Enter tuşuna basarken hata oluştu: {e}")
                return False
        return False
    
    def tus_gonder(self, secici_tipi, secici_degeri, tus, bekleme_suresi=10):
        """Belirtilen elemente özel tuş gönderir"""
        element = self.element_bul(secici_tipi, secici_degeri, bekleme_suresi)
        if element:
            try:
                tus_mapping = {
                    "ENTER": Keys.RETURN,
                    "TAB": Keys.TAB,
                    "ESC": Keys.ESCAPE,
                    "SPACE": Keys.SPACE,
                    "BACKSPACE": Keys.BACK_SPACE,
                    "DELETE": Keys.DELETE,
                    "ARROW_UP": Keys.ARROW_UP,
                    "ARROW_DOWN": Keys.ARROW_DOWN,
                    "ARROW_LEFT": Keys.ARROW_LEFT,
                    "ARROW_RIGHT": Keys.ARROW_RIGHT,
                    "PAGE_UP": Keys.PAGE_UP,
                    "PAGE_DOWN": Keys.PAGE_DOWN,
                    "HOME": Keys.HOME,
                    "END": Keys.END,
                    "F1": Keys.F1,
                    "F2": Keys.F2,
                    "F3": Keys.F3,
                    "F4": Keys.F4,
                    "F5": Keys.F5,
                    "F6": Keys.F6,
                    "F7": Keys.F7,
                    "F8": Keys.F8,
                    "F9": Keys.F9,
                    "F10": Keys.F10,
                    "F11": Keys.F11,
                    "F12": Keys.F12
                }
                
                if tus.upper() in tus_mapping:
                    element.send_keys(tus_mapping[tus.upper()])
                    print(f"{secici_tipi}={secici_degeri} elementine {tus.upper()} tuşu gönderildi.")
                    return True
                else:
                    print(f"Geçersiz tuş: {tus}. Desteklenen tuşlar: {', '.join(tus_mapping.keys())}")
                    return False
            except Exception as e:
                print(f"Tuş gönderirken hata oluştu: {e}")
                return False
        return False
    
    def metin_oku(self, secici_tipi, secici_degeri, bekleme_suresi=10):
        """Belirtilen elementin metnini okur"""
        element = self.element_bul(secici_tipi, secici_degeri, bekleme_suresi)
        if element:
            try:
                metin = element.text
                if not metin:  # Bazen text yerine value attribute'u kullanılabilir
                    metin = element.get_attribute("value")
                print(f"{secici_tipi}={secici_degeri} elementinden metin okundu: {metin}")
                return metin
            except Exception as e:
                print(f"Metni okurken hata oluştu: {e}")
                return None
        return None
    
    def coklu_metin_oku(self, secici_tipi, secici_degeri, bekleme_suresi=10):
        """Belirtilen seçiciye uyan tüm elementlerin metinlerini okur"""
        elements = self.elementleri_bul(secici_tipi, secici_degeri, bekleme_suresi)
        if elements:
            try:
                metin_listesi = []
                for i, element in enumerate(elements):
                    metin = element.text
                    if not metin:  # Bazen text yerine value attribute'u kullanılabilir
                        metin = element.get_attribute("value")
                    metin_listesi.append(metin)
                print(f"{len(metin_listesi)} adet elementten metin okundu.")
                return metin_listesi
            except Exception as e:
                print(f"Çoklu metin okurken hata oluştu: {e}")
                return []
        return []
    
    def bekle(self, saniye):
        """Belirtilen saniye kadar bekler"""
        print(f"{saniye} saniye bekleniyor...")
        time.sleep(saniye)
        print("Bekleme tamamlandı.")
    
    def attribute_oku(self, secici_tipi, secici_degeri, attribute_adi, bekleme_suresi=10):
        """Belirtilen elementin belirtilen attribute değerini okur"""
        element = self.element_bul(secici_tipi, secici_degeri, bekleme_suresi)
        if element:
            try:
                deger = element.get_attribute(attribute_adi)
                print(f"{secici_tipi}={secici_degeri} elementinin {attribute_adi} değeri: {deger}")
                return deger
            except Exception as e:
                print(f"Attribute değeri okunurken hata oluştu: {e}")
                return None
        return None
    
    def tablo_oku(self, tablo_secici_tipi, tablo_secici_degeri, bekleme_suresi=10):
        """HTML tablosunu okur ve pandas DataFrame'e dönüştürür"""
        tabloElement = self.element_bul(tablo_secici_tipi, tablo_secici_degeri, bekleme_suresi)
        if tabloElement:
            try:
                # Tablo başlıklarını bul
                basliklar = []
                baslik_elementleri = tabloElement.find_elements(By.TAG_NAME, "th")
                if baslik_elementleri:
                    for baslik in baslik_elementleri:
                        basliklar.append(baslik.text)
                else:
                    # Bazı tablolarda th yerine ilk satırdaki td'ler başlık olabilir
                    ilk_satir = tabloElement.find_element(By.TAG_NAME, "tr")
                    baslik_elementleri = ilk_satir.find_elements(By.TAG_NAME, "td")
                    for baslik in baslik_elementleri:
                        basliklar.append(baslik.text)
                
                # Eğer başlık bulunamadıysa, otomatik sütun adları oluştur
                if not basliklar:
                    satir_elementleri = tabloElement.find_elements(By.TAG_NAME, "tr")
                    if satir_elementleri:
                        sutun_sayisi = len(satir_elementleri[0].find_elements(By.TAG_NAME, "td"))
                        basliklar = [f"Sütun {i+1}" for i in range(sutun_sayisi)]
                
                # Tablo verilerini bul
                veriler = []
                satir_elementleri = tabloElement.find_elements(By.TAG_NAME, "tr")
                
                # İlk satır başlık olabilir, kontrol et
                baslangic = 0
                if baslik_elementleri and len(satir_elementleri) > 0:
                    if len(satir_elementleri[0].find_elements(By.TAG_NAME, "th")) > 0:
                        baslangic = 1
                
                # Satırlardaki verileri topla
                for i in range(baslangic, len(satir_elementleri)):
                    satir = satir_elementleri[i]
                    hucre_elementleri = satir.find_elements(By.TAG_NAME, "td")
                    if hucre_elementleri:
                        satir_verileri = []
                        for hucre in hucre_elementleri:
                            satir_verileri.append(hucre.text)
                        veriler.append(satir_verileri)
                
                # DataFrame oluştur
                if veriler:
                    df = pd.DataFrame(veriler)
                    if len(basliklar) == len(df.columns):
                        df.columns = basliklar
                    print(f"Tablo okundu. Boyut: {df.shape}")
                    return df
                else:
                    print("Tabloda veri bulunamadı.")
                    return None
            except Exception as e:
                print(f"Tablo okunurken hata oluştu: {e}")
                return None
        return None
    
    def sayfa_kaynagini_al(self):
        """Sayfanın kaynak kodunu alır"""
        try:
            kaynak = self.driver.page_source
            print("Sayfa kaynağı alındı.")
            return kaynak
        except Exception as e:
            print(f"Sayfa kaynağı alınırken hata oluştu: {e}")
            return None
    
    def ekran_goruntusu_al(self, dosya_adi="ekran_goruntusu.png"):
        """Ekran görüntüsü alır"""
        try:
            self.driver.save_screenshot(dosya_adi)
            print(f"Ekran görüntüsü {dosya_adi} olarak kaydedildi.")
            return True
        except Exception as e:
            print(f"Ekran görüntüsü alınırken hata oluştu: {e}")
            return False
    
    def yeni_sekme_ac(self):
        """Yeni sekme açar"""
        try:
            self.driver.execute_script("window.open('', '_blank');")
            pencereler = self.driver.window_handles
            self.driver.switch_to.window(pencereler[-1])
            print("Yeni sekme açıldı.")
            return True
        except Exception as e:
            print(f"Yeni sekme açılırken hata oluştu: {e}")
            return False
    
    def sekme_degistir(self, sekme_index):
        """Belirtilen indexteki sekmeye geçiş yapar"""
        try:
            pencereler = self.driver.window_handles
            if 0 <= sekme_index < len(pencereler):
                self.driver.switch_to.window(pencereler[sekme_index])
                print(f"{sekme_index + 1}. sekmeye geçildi.")
                return True
            else:
                print(f"Geçersiz sekme indeksi. Toplam sekme sayısı: {len(pencereler)}")
                return False
        except Exception as e:
            print(f"Sekme değiştirilirken hata oluştu: {e}")
            return False
    
    def sekme_kapat(self):
        """Aktif sekmeyi kapatır"""
        try:
            self.driver.close()
            pencereler = self.driver.window_handles
            if pencereler:
                self.driver.switch_to.window(pencereler[0])
            print("Aktif sekme kapatıldı.")
            return True
        except Exception as e:
            print(f"Sekme kapatılırken hata oluştu: {e}")
            return False
    
    def tarayici_kapat(self):
        """Tarayıcıyı kapatır"""
        if self.driver:
            print("Tarayıcı kapatılıyor...")
            self.driver.quit()
            self.driver = None
            print("Tarayıcı kapatıldı!")
            return True
        return False
    
    def scroll_yap(self, miktar=None, element=None, yukari=False):
        """Sayfada ya da element içinde scroll yapar"""
        try:
            if element:
                # Element içinde scroll
                if yukari:
                    # Yukarı scroll
                    self.driver.execute_script("arguments[0].scrollTop -= arguments[1];", element, miktar or 300)
                else:
                    # Aşağı scroll
                    self.driver.execute_script("arguments[0].scrollTop += arguments[1];", element, miktar or 300)
                print(f"Element içinde {'yukarı' if yukari else 'aşağı'} scroll yapıldı.")
            else:
                # Sayfa içinde scroll
                if miktar is not None:
                    # Belirli bir miktar scroll
                    if yukari:
                        # Yukarı scroll
                        self.driver.execute_script(f"window.scrollBy(0, -{miktar});")
                    else:
                        # Aşağı scroll
                        self.driver.execute_script(f"window.scrollBy(0, {miktar});")
                    print(f"Sayfada {miktar}px {'yukarı' if yukari else 'aşağı'} scroll yapıldı.")
                else:
                    # Sayfanın en altına veya en üstüne scroll
                    if yukari:
                        # En üste scroll
                        self.driver.execute_script("window.scrollTo(0, 0);")
                        print("Sayfanın en üstüne scroll yapıldı.")
                    else:
                        # En alta scroll
                        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        print("Sayfanın en altına scroll yapıldı.")
            return True
        except Exception as e:
            print(f"Scroll yapılırken hata oluştu: {e}")
            return False
    
    def tum_tablolari_oku(self, tablo_secici_tipi, tablo_secici_degeri, sonraki_buton_secici_tipi, sonraki_buton_secici_degeri, bekleme_suresi=10):
        """
         Tablonun bulunduğu sayfadan başlayarak, 
         her sayfada tabloyu okuyup verileri toplar ve
         tüm sayfalardaki verileri tek bir DataFrame'e dönüştürür.
         """
        tum_veriler = []
        sayfa = 1

        while True:
            print(f"\nSayfa {sayfa} okunuyor...")
            # Her sayfadaki tablo verilerini oku
            df = self.tablo_oku(tablo_secici_tipi, tablo_secici_degeri, bekleme_suresi)
            if df is not None:
                tum_veriler.append(df)
            else:
                print(f"Sayfa {sayfa}'da tablo bulunamadı.")
        
            # Sonraki butonunu bulup tıklamaya çalış
            sonraki_buton = self.element_bul(sonraki_buton_secici_tipi, sonraki_buton_secici_degeri, bekleme_suresi)
            if sonraki_buton:
                try:
                    # Butonun aktif veya tıklanabilir olduğundan emin olun
                    WebDriverWait(self.driver, bekleme_suresi).until(
                        EC.element_to_be_clickable((self.element_dict[sonraki_buton_secici_tipi], sonraki_buton_secici_degeri))
                    )
                    sonraki_buton.click()
                    sayfa += 1
                    self.bekle(2)  # Sayfa yüklemesi için kısa bir bekleme ekleyebilirsiniz
                except Exception as e:
                    print(f"Sonraki butona tıklanırken hata oluştu: {e}")
                    break
            else:
                print("Sonraki sayfa bulunamadı. Döngü sona erdi.")
                break

        if tum_veriler:
            # Tüm DataFrame'leri birleştir
            sonuc_df = pd.concat(tum_veriler, ignore_index=True)
            print(f"Toplam {sayfa} sayfa okundu. Birleştirilmiş DataFrame boyutu: {sonuc_df.shape}")
            return sonuc_df
        else:
            print("Hiç veri bulunamadı.")
            return None

    def resimleri_indir(self, resim_secici_tipi, resim_secici_degeri, kayit_klasoru=None, max_resim=None, bekleme_suresi=10):
    
        import requests
        import os
        from urllib.parse import urljoin, urlparse
        import time
        
        # Kayıt klasörünü ayarla
        if kayit_klasoru is None:
            kayit_klasoru = "images"
        
        # Klasörü oluştur (yoksa)
        if not os.path.exists(kayit_klasoru):
            os.makedirs(kayit_klasoru)
            print(f"{kayit_klasoru} klasörü oluşturuldu.")
        
        # Resimleri bul
        resimler = self.elementleri_bul(resim_secici_tipi, resim_secici_degeri, bekleme_suresi)
        
        if not resimler:
            print("Hiç resim bulunamadı!")
            return []
        
        # Sınırlama kontrolü
        if max_resim is not None and isinstance(max_resim, int):
            resimler = resimler[:max_resim]
            print(f"Maksimum {max_resim} resim indirilecek.")
        
        indirilen_dosyalar = []
        basarisiz = 0
        
        for i, resim in enumerate(resimler):
            try:
                # Resim URL'sini al
                resim_url = resim.get_attribute("src")
                if not resim_url:
                    # Bazı web siteleri src yerine data-src vb. kullanabilir
                    alt_attrlar = ["data-src", "data-original", "data-lazy-src", "data-original-src"]
                    for attr in alt_attrlar:
                        alt_url = resim.get_attribute(attr)
                        if alt_url:
                            resim_url = alt_url
                            break
                
                if not resim_url:
                    print(f"Resim #{i+1} için URL bulunamadı. Atlanıyor.")
                    basarisiz += 1
                    continue
                
                # Göreceli URL'yi mutlak URL'ye çevir
                if not resim_url.startswith(('http://', 'https://')):
                    resim_url = urljoin(self.driver.current_url, resim_url)
                
                # Dosya adını URL'den çıkar
                dosya_adi = os.path.basename(urlparse(resim_url).path)
                
                # Dosya adı boşsa veya geçersizse, sıralı bir isim ver
                if not dosya_adi or '.' not in dosya_adi:
                    dosya_adi = f"image_{i+1}.jpg"
                
                # Dosya zaten varsa, ismini değiştir
                dosya_yolu = os.path.join(kayit_klasoru, dosya_adi)
                if os.path.exists(dosya_yolu):
                    dosya_adi = f"{os.path.splitext(dosya_adi)[0]}_{int(time.time())}_{i}{os.path.splitext(dosya_adi)[1]}"
                    dosya_yolu = os.path.join(kayit_klasoru, dosya_adi)
                
                # Resmi indir
                response = requests.get(resim_url, stream=True, timeout=10)
                if response.status_code == 200:
                    with open(dosya_yolu, 'wb') as dosya:
                        for chunk in response.iter_content(1024):
                            dosya.write(chunk)
                    
                    indirilen_dosyalar.append(dosya_yolu)
                    print(f"Resim #{i+1} indirildi: {dosya_yolu}")
                else:
                    print(f"Resim #{i+1} indirilemedi. HTTP kodu: {response.status_code}")
                    basarisiz += 1
            
            except Exception as e:
                print(f"Resim #{i+1} indirilirken hata oluştu: {str(e)}")
                basarisiz += 1
        
        print(f"\nİşlem tamamlandı: {len(indirilen_dosyalar)} resim indirildi, {basarisiz} resim indirilemedi.")
        return indirilen_dosyalar


def ana_menu():
    print("\n" + "="*50)
    print("SELENIUM WEB OTOMASYON ARACI")
    print("="*50)
    print("1. Tarayıcı başlat")
    print("2. URL'ye git")
    print("3. Elemente tıkla")
    print("4. Metin yaz")
    print("5. Enter tuşu gönder")
    print("6. Özel tuş gönder")
    print("7. Metin oku")
    print("8. Çoklu metin oku")
    print("9. Bekleme süresi ekle")
    print("10. Tablo oku")
    print("11. Tüm tablolarda veri oku")
    print("12. Scroll yap")
    print("13. Yeni sekme aç")
    print("14. Sekme değiştir")
    print("15. Aktif sekmeyi kapat")
    print("16. Resimleri indir")
    print("17. Tarayıcıyı kapat")
    print("18. Kombinasyon Çalıştır")
    print("0. Programdan çık")
    print("="*50)
    secim = input("Yapmak istediğiniz işlemin numarasını girin: ")
    return secim

def secici_bilgisi_al():
    print("\nKullanılabilir seçici tipleri: ID, NAME, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, TAG_NAME, CLASS_NAME, CSS_SELECTOR")
    
    while True:
        secici_tipi = input("Seçici tipini girin: ").upper()
        if secici_tipi in ["ID", "NAME", "XPATH", "LINK_TEXT", "PARTIAL_LINK_TEXT", "TAG_NAME", "CLASS_NAME", "CSS_SELECTOR"]:
            break
        else:
            print("Geçersiz seçici tipi! Lütfen listeden birini seçin.")
    
    secici_degeri = input("Seçici değerini girin: ")
    return secici_tipi, secici_degeri


def kombinasyon_calistir(otomasyon):
    print("\n" + "="*50)
    print("KOMBİNASYON ÇALIŞTIR")
    print("="*50)
    print("Mevcut Adımlar:")
    print("1. Tarayıcı başlat")
    print("2. URL'ye git")
    print("3. Elemente tıkla")
    print("4. Metin yaz")
    print("5. Enter tuşu gönder")
    print("6. Özel tuş gönder")
    print("7. Metin oku")
    print("8. Çoklu metin oku")
    print("9. Bekleme süresi ekle")
    print("10. Tablo oku")
    print("11. Tüm tablolarda veri oku")
    print("12. Scroll yap")
    print("13. Yeni sekme aç")
    print("14. Sekme değiştir")
    print("15. Aktif sekmeyi kapat")
    print("16. Resimleri indir")
    print("17. Tarayıcıyı kapat")
    print("="*50)
    
    kombinasyon = input("Çalıştırmak istediğiniz adımları sırayla ve boşluklarla ayırarak girin (örn: 3 12 9 7): ")
    adimlar = kombinasyon.split()
    
    # Her adım için saklanan parametreleri tutacak sözlük
    saklanan_parametreler = {}
    
    # Adımları sırayla işle
    for adim in adimlar:
        print(f"\n{'-'*50}")
        print(f"Adım {adim} çalıştırılıyor...")
        
        # Daha önce aynı adım çalıştırıldı mı kontrol et
        onceki_bilgileri_kullan = False
        if adim in saklanan_parametreler:
            cevap = input(f"Adım {adim} için önceki bilgileri kullanmak ister misiniz? (E/H): ").upper()
            onceki_bilgileri_kullan = cevap == "E"
        
        # Ana menüdeki adımları çağır
        if adim == "1":
            otomasyon.tarayici_baslat()
            
        elif adim == "2":
            if onceki_bilgileri_kullan:
                url = saklanan_parametreler[adim]["url"]
                print(f"Kaydedilmiş URL kullanılıyor: {url}")
            else:
                url = input("Gitmek istediğiniz URL'yi girin: ")
                saklanan_parametreler[adim] = {"url": url}
            
            otomasyon.url_git(url)
            
        elif adim == "3":
            print("\nBir elemente tıklamak için element bilgilerini girin.")
            
            if onceki_bilgileri_kullan:
                secici_tipi = saklanan_parametreler[adim]["secici_tipi"]
                secici_degeri = saklanan_parametreler[adim]["secici_degeri"]
                bekleme_suresi = saklanan_parametreler[adim]["bekleme_suresi"]
                print(f"Kaydedilmiş bilgiler kullanılıyor: {secici_tipi}={secici_degeri}, Bekleme: {bekleme_suresi}s")
            else:
                secici_tipi, secici_degeri = secici_bilgisi_al()
                bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
                saklanan_parametreler[adim] = {
                    "secici_tipi": secici_tipi,
                    "secici_degeri": secici_degeri,
                    "bekleme_suresi": bekleme_suresi
                }
            
            otomasyon.tikla(secici_tipi, secici_degeri, bekleme_suresi)
            
        elif adim == "4":
            print("\nBir elemente metin yazmak için element bilgilerini girin.")
            
            if onceki_bilgileri_kullan:
                secici_tipi = saklanan_parametreler[adim]["secici_tipi"]
                secici_degeri = saklanan_parametreler[adim]["secici_degeri"]
                metin = saklanan_parametreler[adim]["metin"]
                bekleme_suresi = saklanan_parametreler[adim]["bekleme_suresi"]
                print(f"Kaydedilmiş bilgiler kullanılıyor: {secici_tipi}={secici_degeri}, Metin: '{metin}', Bekleme: {bekleme_suresi}s")
            else:
                secici_tipi, secici_degeri = secici_bilgisi_al()
                metin = input("Yazmak istediğiniz metni girin: ")
                bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
                saklanan_parametreler[adim] = {
                    "secici_tipi": secici_tipi,
                    "secici_degeri": secici_degeri,
                    "metin": metin,
                    "bekleme_suresi": bekleme_suresi
                }
            
            otomasyon.metin_yaz(secici_tipi, secici_degeri, metin, bekleme_suresi)
            
        elif adim == "5":
            print("\nBir elemente Enter tuşu göndermek için element bilgilerini girin.")
            
            if onceki_bilgileri_kullan:
                secici_tipi = saklanan_parametreler[adim]["secici_tipi"]
                secici_degeri = saklanan_parametreler[adim]["secici_degeri"]
                bekleme_suresi = saklanan_parametreler[adim]["bekleme_suresi"]
                print(f"Kaydedilmiş bilgiler kullanılıyor: {secici_tipi}={secici_degeri}, Bekleme: {bekleme_suresi}s")
            else:
                secici_tipi, secici_degeri = secici_bilgisi_al()
                bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
                saklanan_parametreler[adim] = {
                    "secici_tipi": secici_tipi,
                    "secici_degeri": secici_degeri,
                    "bekleme_suresi": bekleme_suresi
                }
            
            otomasyon.enter_bas(secici_tipi, secici_degeri, bekleme_suresi)
            
        elif adim == "6":
            print("\nBir elemente özel tuş göndermek için element bilgilerini girin.")
            
            if onceki_bilgileri_kullan:
                secici_tipi = saklanan_parametreler[adim]["secici_tipi"]
                secici_degeri = saklanan_parametreler[adim]["secici_degeri"]
                tus = saklanan_parametreler[adim]["tus"]
                bekleme_suresi = saklanan_parametreler[adim]["bekleme_suresi"]
                print(f"Kaydedilmiş bilgiler kullanılıyor: {secici_tipi}={secici_degeri}, Tuş: {tus}, Bekleme: {bekleme_suresi}s")
            else:
                secici_tipi, secici_degeri = secici_bilgisi_al()
                print("\nÖzel tuşlar: ENTER, TAB, ESC, SPACE, BACKSPACE, DELETE, ARROW_UP, ARROW_DOWN, ARROW_LEFT, ARROW_RIGHT")
                print("PAGE_UP, PAGE_DOWN, HOME, END, F1-F12")
                tus = input("Göndermek istediğiniz tuşu girin: ")
                bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
                saklanan_parametreler[adim] = {
                    "secici_tipi": secici_tipi,
                    "secici_degeri": secici_degeri,
                    "tus": tus,
                    "bekleme_suresi": bekleme_suresi
                }
            
            otomasyon.tus_gonder(secici_tipi, secici_degeri, tus, bekleme_suresi)
            
        elif adim == "7":
            print("\nBir elementten metin okumak için element bilgilerini girin.")
            
            if onceki_bilgileri_kullan:
                secici_tipi = saklanan_parametreler[adim]["secici_tipi"]
                secici_degeri = saklanan_parametreler[adim]["secici_degeri"]
                bekleme_suresi = saklanan_parametreler[adim]["bekleme_suresi"]
                print(f"Kaydedilmiş bilgiler kullanılıyor: {secici_tipi}={secici_degeri}, Bekleme: {bekleme_suresi}s")
            else:
                secici_tipi, secici_degeri = secici_bilgisi_al()
                bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
                saklanan_parametreler[adim] = {
                    "secici_tipi": secici_tipi,
                    "secici_degeri": secici_degeri,
                    "bekleme_suresi": bekleme_suresi
                }
            
            okunan_metin = otomasyon.metin_oku(secici_tipi, secici_degeri, bekleme_suresi)
            if okunan_metin is not None:
                print(f"Okunan metin: {okunan_metin}")
            
        elif adim == "8":
            print("\nBirden fazla elementten metin okumak için element bilgilerini girin.")
            
            if onceki_bilgileri_kullan:
                secici_tipi = saklanan_parametreler[adim]["secici_tipi"]
                secici_degeri = saklanan_parametreler[adim]["secici_degeri"]
                bekleme_suresi = saklanan_parametreler[adim]["bekleme_suresi"]
                print(f"Kaydedilmiş bilgiler kullanılıyor: {secici_tipi}={secici_degeri}, Bekleme: {bekleme_suresi}s")
            else:
                secici_tipi, secici_degeri = secici_bilgisi_al()
                bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
                saklanan_parametreler[adim] = {
                    "secici_tipi": secici_tipi,
                    "secici_degeri": secici_degeri,
                    "bekleme_suresi": bekleme_suresi
                }
            
            okunan_metinler = otomasyon.coklu_metin_oku(secici_tipi, secici_degeri, bekleme_suresi)
            if okunan_metinler:
                print("\nOkunan metinler:")
                for i, metin in enumerate(okunan_metinler):
                    print(f"{i+1}. {metin}")
            
        elif adim == "9":
            if onceki_bilgileri_kullan:
                sure = saklanan_parametreler[adim]["sure"]
                print(f"Kaydedilmiş bekleme süresi kullanılıyor: {sure}s")
            else:
                sure = int(input("Kaç saniye beklemek istiyorsunuz: ") or "5")
                saklanan_parametreler[adim] = {"sure": sure}
            
            otomasyon.bekle(sure)
            
        elif adim == "10":
            print("\nBir tabloyu okumak için tablo element bilgilerini girin.")
            
            if onceki_bilgileri_kullan:
                secici_tipi = saklanan_parametreler[adim]["secici_tipi"]
                secici_degeri = saklanan_parametreler[adim]["secici_degeri"]
                bekleme_suresi = saklanan_parametreler[adim]["bekleme_suresi"]
                print(f"Kaydedilmiş bilgiler kullanılıyor: {secici_tipi}={secici_degeri}, Bekleme: {bekleme_suresi}s")
            else:
                secici_tipi, secici_degeri = secici_bilgisi_al()
                bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
                saklanan_parametreler[adim] = {
                    "secici_tipi": secici_tipi,
                    "secici_degeri": secici_degeri,
                    "bekleme_suresi": bekleme_suresi
                }
            
            tablo_df = otomasyon.tablo_oku(secici_tipi, secici_degeri, bekleme_suresi)
            if isinstance(tablo_df, pd.DataFrame):
                print("\nTablo içeriği:")
                print(tablo_df)
                kaydet = input("Tabloyu xlsx dosyası olarak kaydetmek ister misiniz? (e/h): ").lower()
                if kaydet == "e":
                    dosya_adi = input("Dosya adını girin (varsayılan: tablo_verisi.xlsx): ") or "tablo_verisi.xlsx"
                    tablo_df.to_excel(dosya_adi, index=False)
                    print(f"Tablo {dosya_adi} olarak kaydedildi.")

        elif adim == "11":
            print("\nTüm sayfalardaki tabloyu oku:")
            
            if onceki_bilgileri_kullan:
                tablo_secici_tipi = saklanan_parametreler[adim]["tablo_secici_tipi"]
                tablo_secici_degeri = saklanan_parametreler[adim]["tablo_secici_degeri"]
                sonraki_buton_secici_tipi = saklanan_parametreler[adim]["sonraki_buton_secici_tipi"]
                sonraki_buton_secici_degeri = saklanan_parametreler[adim]["sonraki_buton_secici_degeri"]
                bekleme_suresi = saklanan_parametreler[adim]["bekleme_suresi"]
                print(f"Kaydedilmiş bilgiler kullanılıyor")
            else:
                # Tablo için seçici bilgileri
                print("Tablo için seçici bilgilerini girin:")
                tablo_secici_tipi, tablo_secici_degeri = secici_bilgisi_al()
                # Sonraki buton için seçici bilgileri
                print("Sonraki buton için seçici bilgilerini girin:")
                sonraki_buton_secici_tipi, sonraki_buton_secici_degeri = secici_bilgisi_al()
                bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
                
                saklanan_parametreler[adim] = {
                    "tablo_secici_tipi": tablo_secici_tipi,
                    "tablo_secici_degeri": tablo_secici_degeri,
                    "sonraki_buton_secici_tipi": sonraki_buton_secici_tipi,
                    "sonraki_buton_secici_degeri": sonraki_buton_secici_degeri,
                    "bekleme_suresi": bekleme_suresi
                }
            
            tum_df = otomasyon.tum_tablolari_oku(tablo_secici_tipi, tablo_secici_degeri, 
                                        sonraki_buton_secici_tipi, sonraki_buton_secici_degeri, bekleme_suresi)
            if isinstance(tum_df, pd.DataFrame):
                print("\nBirleştirilmiş tablo içeriği:")
                print(tum_df)
                kaydet = input("Tabloyu xlsx dosyası olarak kaydetmek ister misiniz? (e/h): ").lower()
                if kaydet == "e":
                    dosya_adi = input("Dosya adını girin (varsayılan: tum_tablo_verisi.xlsx): ") or "tum_tablo_verisi.xlsx"
                    tum_df.to_excel(dosya_adi, index=False)
                    print(f"Tablo {dosya_adi} olarak kaydedildi.")
                    
        elif adim == "12":
            print("\nSayfada scroll yapmak için:")
            
            if onceki_bilgileri_kullan:
                miktar = saklanan_parametreler[adim]["miktar"]
                element_kullan = saklanan_parametreler[adim]["element_kullan"]
                element = None
                if element_kullan:
                    secici_tipi = saklanan_parametreler[adim]["secici_tipi"]
                    secici_degeri = saklanan_parametreler[adim]["secici_degeri"]
                    element = otomasyon.element_bul(secici_tipi, secici_degeri)
                yukari = saklanan_parametreler[adim]["yukari"]
                
                print(f"Kaydedilmiş scroll bilgileri kullanılıyor")
            else:
                miktar_input = input("Scroll miktarı (boş bırakırsanız sayfanın sonuna kadar scroll yapılır): ")
                miktar = int(miktar_input) if miktar_input.strip() and miktar_input.isdigit() else None
                
                element_kullan = input("Belirli bir element içinde scroll yapmak ister misiniz? (e/h): ").lower() == "e"
                element = None
                secici_tipi = None
                secici_degeri = None
                if element_kullan:
                    print("Scroll yapmak istediğiniz elementi belirtin:")
                    secici_tipi, secici_degeri = secici_bilgisi_al()
                    element = otomasyon.element_bul(secici_tipi, secici_degeri)
                
                yukari = input("Yukarı yönde scroll yapmak ister misiniz? (e/h): ").lower() == "e"
                
                saklanan_parametreler[adim] = {
                    "miktar": miktar,
                    "element_kullan": element_kullan,
                    "secici_tipi": secici_tipi if element_kullan else None,
                    "secici_degeri": secici_degeri if element_kullan else None,
                    "yukari": yukari
                }
            
            otomasyon.scroll_yap(miktar, element, yukari)
            
        elif adim == "13":
            otomasyon.yeni_sekme_ac()
            
        elif adim == "14":
            sekme_sayisi = len(otomasyon.driver.window_handles)
            
            if onceki_bilgileri_kullan:
                sekme_index = saklanan_parametreler[adim]["sekme_index"]
                print(f"Kaydedilmiş sekme indeksi kullanılıyor: {sekme_index}")
            else:
                print(f"\nToplam {sekme_sayisi} sekme var.")
                sekme_index = int(input(f"Geçmek istediğiniz sekme numarasını girin (0-{sekme_sayisi-1}): "))
                saklanan_parametreler[adim] = {"sekme_index": sekme_index}
            
            otomasyon.sekme_degistir(sekme_index)
            
        elif adim == "15":
            otomasyon.sekme_kapat()
            
        elif adim == "16":
            print("\nSayfadaki resimleri indirmek için:")
            
            if onceki_bilgileri_kullan:
                resim_secici_tipi = saklanan_parametreler[adim]["resim_secici_tipi"]
                resim_secici_degeri = saklanan_parametreler[adim]["resim_secici_degeri"]
                kayit_klasoru = saklanan_parametreler[adim]["kayit_klasoru"]
                max_resim = saklanan_parametreler[adim]["max_resim"]
                bekleme_suresi = saklanan_parametreler[adim]["bekleme_suresi"]
                print(f"Kaydedilmiş resim indirme bilgileri kullanılıyor")
            else:
                resim_secici_tipi, resim_secici_degeri = secici_bilgisi_al()
                print("\nÖnerilen resim seçicileri:")
                print("TAG_NAME - img (tüm resimler)")
                print("CSS_SELECTOR - img.class_name (belirli class'daki resimler)")
                print("XPATH - //div[@id='gallery']//img (belirli bir div içindeki tüm resimler)")
                
                kayit_klasoru = input("\nResimlerin kaydedileceği klasör (varsayılan: images): ") or "images"
                
                max_resim_input = input("İndirilecek maksimum resim sayısı (sınırsız için boş bırakın): ")
                max_resim = int(max_resim_input) if max_resim_input.strip() else None
                
                bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
                
                saklanan_parametreler[adim] = {
                    "resim_secici_tipi": resim_secici_tipi,
                    "resim_secici_degeri": resim_secici_degeri,
                    "kayit_klasoru": kayit_klasoru,
                    "max_resim": max_resim,
                    "bekleme_suresi": bekleme_suresi
                }
            
            indirilen_resimler = otomasyon.resimleri_indir(resim_secici_tipi, resim_secici_degeri, 
                                                      kayit_klasoru, max_resim, bekleme_suresi)
            
        elif adim == "17":
            otomasyon.tarayici_kapat()
            
        else:
            print(f"Geçersiz adım numarası: {adim}")
        
        print(f"{'-'*50}")
    
    print("\nKombinasyon çalıştırma tamamlandı!")
    return True

def main():
    otomasyon = SeleniumOtomasyon()
    
    while True:
        secim = ana_menu()
        
        if secim == "0":
            print("Programdan çıkılıyor...")
            if otomasyon.driver:
                otomasyon.tarayici_kapat()
            break
            
        elif secim == "1":
            otomasyon.tarayici_baslat()
            
        elif secim == "2":
            url = input("Gitmek istediğiniz URL'yi girin: ")
            otomasyon.url_git(url)
            
        elif secim == "3":
            print("\nBir elemente tıklamak için element bilgilerini girin.")
            secici_tipi, secici_degeri = secici_bilgisi_al()
            bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
            otomasyon.tikla(secici_tipi, secici_degeri, bekleme_suresi)
            
        elif secim == "4":
            print("\nBir elemente metin yazmak için element bilgilerini girin.")
            secici_tipi, secici_degeri = secici_bilgisi_al()
            metin = input("Yazmak istediğiniz metni girin: ")
            bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
            otomasyon.metin_yaz(secici_tipi, secici_degeri, metin, bekleme_suresi)
            
        elif secim == "5":
            print("\nBir elemente Enter tuşu göndermek için element bilgilerini girin.")
            secici_tipi, secici_degeri = secici_bilgisi_al()
            bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
            otomasyon.enter_bas(secici_tipi, secici_degeri, bekleme_suresi)
            
        elif secim == "6":
            print("\nBir elemente özel tuş göndermek için element bilgilerini girin.")
            secici_tipi, secici_degeri = secici_bilgisi_al()
            print("\nÖzel tuşlar: ENTER, TAB, ESC, SPACE, BACKSPACE, DELETE, ARROW_UP, ARROW_DOWN, ARROW_LEFT, ARROW_RIGHT")
            print("PAGE_UP, PAGE_DOWN, HOME, END, F1-F12")
            tus = input("Göndermek istediğiniz tuşu girin: ")
            bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
            otomasyon.tus_gonder(secici_tipi, secici_degeri, tus, bekleme_suresi)
            
        elif secim == "7":
            print("\nBir elementten metin okumak için element bilgilerini girin.")
            secici_tipi, secici_degeri = secici_bilgisi_al()
            bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
            okunan_metin = otomasyon.metin_oku(secici_tipi, secici_degeri, bekleme_suresi)
            if okunan_metin is not None:
                print(f"Okunan metin: {okunan_metin}")
            
        elif secim == "8":
            print("\nBirden fazla elementten metin okumak için element bilgilerini girin.")
            secici_tipi, secici_degeri = secici_bilgisi_al()
            bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
            okunan_metinler = otomasyon.coklu_metin_oku(secici_tipi, secici_degeri, bekleme_suresi)
            if okunan_metinler:
                print("\nOkunan metinler:")
                for i, metin in enumerate(okunan_metinler):
                    print(f"{i+1}. {metin}")
            
        elif secim == "9":
            sure = int(input("Kaç saniye beklemek istiyorsunuz: ") or "5")
            otomasyon.bekle(sure)
            
        elif secim == "10":
            print("\nBir tabloyu okumak için tablo element bilgilerini girin.")
            secici_tipi, secici_degeri = secici_bilgisi_al()
            bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
            tablo_df = otomasyon.tablo_oku(secici_tipi, secici_degeri, bekleme_suresi)
            if isinstance(tablo_df, pd.DataFrame):
                print("\nTablo içeriği:")
                print(tablo_df)
                kaydet = input("Tabloyu xlsx dosyası olarak kaydetmek ister misiniz? (e/h): ").lower()
                if kaydet == "e":
                    dosya_adi = input("Dosya adını girin (varsayılan: tablo_verisi.xlsx): ") or "tablo_verisi.xlsx"
                    tablo_df.to_excel(dosya_adi, index=False)
                    print(f"Tablo {dosya_adi} olarak kaydedildi.")

        elif secim == "11":  
            print("\nTüm sayfalardaki tabloyu oku:")
            # Tablo için seçici bilgileri
            print("Tablo için seçici bilgilerini girin:")
            tablo_secici_tipi, tablo_secici_degeri = secici_bilgisi_al()
            # Sonraki buton için seçici bilgileri
            print("Sonraki buton için seçici bilgilerini girin:")
            sonraki_buton_secici_tipi, sonraki_buton_secici_degeri = secici_bilgisi_al()
            bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
            tum_df = otomasyon.tum_tablolari_oku(tablo_secici_tipi, tablo_secici_degeri, 
                                        sonraki_buton_secici_tipi, sonraki_buton_secici_degeri, bekleme_suresi)
            if isinstance(tum_df, pd.DataFrame):
                print("\nBirleştirilmiş tablo içeriği:")
                print(tum_df)
                kaydet = input("Tabloyu xlsx dosyası olarak kaydetmek ister misiniz? (e/h): ").lower()
                if kaydet == "e":
                    dosya_adi = input("Dosya adını girin (varsayılan: tum_tablo_verisi.xlsx): ") or "tum_tablo_verisi.xlsx"
                    tum_df.to_excel(dosya_adi, index=False)
                    print(f"Tablo {dosya_adi} olarak kaydedildi.")
                    
        elif secim == "12":
            print("\nSayfada scroll yapmak için:")
            miktar = input("Scroll miktarı (boş bırakırsanız sayfanın sonuna kadar scroll yapılır): ")
            miktar = int(miktar) if miktar.isdigit() else None
            
            element_kullan = input("Belirli bir element içinde scroll yapmak ister misiniz? (e/h): ").lower()
            element = None
            if element_kullan == "e":
                print("Scroll yapmak istediğiniz elementi belirtin:")
                secici_tipi, secici_degeri = secici_bilgisi_al()
                element = otomasyon.element_bul(secici_tipi, secici_degeri)
            
            yukari = input("Yukarı yönde scroll yapmak ister misiniz? (e/h): ").lower() == "e"
            otomasyon.scroll_yap(miktar, element, yukari)
            
        elif secim == "13":
            otomasyon.yeni_sekme_ac()
            
        elif secim == "14":
            sekme_sayisi = len(otomasyon.driver.window_handles)
            print(f"\nToplam {sekme_sayisi} sekme var.")
            sekme_index = int(input(f"Geçmek istediğiniz sekme numarasını girin (0-{sekme_sayisi-1}): "))
            otomasyon.sekme_degistir(sekme_index)
            
        elif secim == "15":
            otomasyon.sekme_kapat()
            
        elif secim == "16":
            print("\nSayfadaki resimleri indirmek için:")
            resim_secici_tipi, resim_secici_degeri = secici_bilgisi_al()
            print("\nÖnerilen resim seçicileri:")
            print("TAG_NAME - img (tüm resimler)")
            print("CSS_SELECTOR - img.class_name (belirli class'daki resimler)")
            print("XPATH - //div[@id='gallery']//img (belirli bir div içindeki tüm resimler)")
            
            kayit_klasoru = input("\nResimlerin kaydedileceği klasör (varsayılan: images): ") or "images"
            
            max_resim_input = input("İndirilecek maksimum resim sayısı (sınırsız için boş bırakın): ")
            max_resim = int(max_resim_input) if max_resim_input.strip() else None
            
            bekleme_suresi = int(input("Bekleme süresi (saniye): ") or "10")
            
            indirilen_resimler = otomasyon.resimleri_indir(resim_secici_tipi, resim_secici_degeri, 
                                                      kayit_klasoru, max_resim, bekleme_suresi)
            
        elif secim == "17":
            otomasyon.tarayici_kapat()
            
        elif secim == "18":
            kombinasyon_calistir(otomasyon)
            
        else:
            print("\nGeçersiz seçim! Lütfen menüden geçerli bir seçenek seçin.")
        
        input("\nDevam etmek için Enter tuşuna basın...")

if __name__ == "__main__":
    main()