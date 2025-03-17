# CRM Optimizasyon Sistemi

Bu proje, müşteri ilişkileri yönetimi (CRM) sisteminde müşteri destek temsilcisi atamaları ile pazarlama kampanyası seçiminde optimizasyon algoritmalarını uygulayan bir Python çözümüdür. Sistem, dinamik programlama tekniklerini kullanarak aşağıdaki iki temel problemi çözmeyi amaçlar:

- **Müşteri Destek Temsilcisi Ataması:**  
  Müşterilerin temsilciler arasında en uygun şekilde dağıtılmasını sağlar. Temsilci lokasyonu, beceri uyumu ve müsaitlik durumu gibi kriterler dikkate alınır.

- **Pazarlama Kampanyası Seçimi:**  
  Toplam bütçe dahilinde, kampanya maliyetleri ve beklenen yatırım getirisine (ROI) göre en karlı kampanya kombinasyonunu belirler. Bu bölüm klasik knapsack problemi çözümü yaklaşımını kullanır.

---

## Özellikler

- **Dinamik Programlama ile Atama:**  
  Müşteri ve temsilci bilgilerini kullanarak, minimum maliyetle en uygun atamayı gerçekleştirir.

- **Bütçe Optimizasyonu:**  
  Kampanya seçiminde, belirlenen bütçe dahilinde maksimum ROI elde edilmesi için optimal kampanya kombinasyonunu belirler.

- **Kapsamlı Raporlama:**  
  Atama sonuçları, seçilen kampanyalar, toplam müşteri sayısı, atanan/atanmayan müşteri sayısı gibi detaylı verileri içeren raporlar üretir.

- **Kolay Genişletilebilirlik:**  
  Sistemin modüler yapısı sayesinde yeni özellikler veya iyileştirmeler kolaylıkla eklenebilir.

---

## Kurulum ve Kullanım

### 1. Projeyi Klonlayın

Terminal veya komut satırında aşağıdaki komutları kullanın:

```bash
git clone https://github.com/kullanici_adiniz/crm-optimizasyon-sistemi.git
cd crm-optimizasyon-sistemi
```

### 2. Sanal Ortam Oluşturun (Opsiyonel)

Proje Python 3 ile uyumlu olduğundan, tercihen sanal ortam kullanarak bağımlılıkları izole edebilirsiniz:

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Projeyi Çalıştırın

Gerekli ek paketlere ihtiyaç duyulmadan, proje standart kütüphaneleri kullanmaktadır. Projeyi çalıştırmak için:

```bash
python main.py
```

`main.py` dosyası, örnek verilerle CRM sistemi üzerinde müşteri destek atamaları ve pazarlama kampanyası seçim optimizasyonunu gerçekleştirir ve sonuçları konsola yazdırır.

---

## Proje Yapısı

```
├── main.py                 # Uygulamanın ana çalıştırma dosyası
├── crm_system.py           # CRM sistemi ve optimizasyon algoritmalarını içeren modül
└── README.md               # Bu dosya
```

---

## Algoritmaların Detayları

### Müşteri Destek Temsilcisi Ataması

- **Amaç:**  
  Müşterileri, temsilciler arasına optimal olarak dağıtarak, maliyetleri minimize etmek.

- **Kriterler:**  
  - **Mesafe Maliyeti:** Aynı şehirde ise 0, farklı şehirde ise 10 puan.
  - **Uzmanlık Uyum:** Müşterinin talep ettiği konu, temsilcinin becerileriyle eşleşiyorsa 0, aksi halde 5 puan.
  - **Uygunluk:** Temsilcinin müsaitlik puanı (10 üzerinden; yüksek puan düşük maliyeti temsil eder).

- **Yaklaşım:**  
  Dinamik programlama kullanılarak, önceki atama durumlarına bağlı olarak minimum toplam maliyet hesaplanır.

### Pazarlama Kampanyası Seçimi

- **Amaç:**  
  Belirlenen bütçe dahilinde, kampanya maliyetleri ve beklenen ROI'ye göre en iyi kampanya kombinasyonunu seçmek.

- **Yaklaşım:**  
  Klasik "knapsack" (sırt çantası) problemi çözümüne benzer şekilde, kampanyaların maliyet ve ROI değerleri üzerinden dinamik programlama uygulanır.

---

## Geliştirici Notları

- **Kod Yapısı:**  
  Kod, işlevselliği artırmak ve okunabilirliği sağlamak amacıyla modüler bir şekilde düzenlenmiştir.
  
- **Genişletme:**  
  Yeni temsilci, müşteri veya kampanya kriterleri eklemek için ilgili fonksiyonlarda güncelleme yapabilirsiniz.
  
- **Hata Bildirimi ve Katkıda Bulunma:**  
  Herhangi bir hata, öneri ya da geliştirme fikriniz varsa lütfen GitHub üzerinden issue oluşturun veya pull request gönderin.
