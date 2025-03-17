def optimize_customer_support_assignment(representatives, customers):
    # Temsilci ve müşteri sayılarını belirle
    n_reps = len(representatives)
    n_customers = len(customers)
    
    # Maliyet matrisini oluştur - her temsilci-müşteri çifti için bir maliyet değeri hesapla
    cost_matrix = [[0 for _ in range(n_customers)] for _ in range(n_reps)]
    
    for i in range(n_reps):
        for j in range(n_customers):
            # Mesafe maliyeti: Aynı şehirde ise 0, değilse 10 puan
            distance_cost = 0 if representatives[i]['location'] == customers[j]['location'] else 10
            
            # Uzmanlık uyumu: Temsilcinin becerileri müşterinin talep türünü karşılıyorsa 0, değilse 5 puan
            expertise_match = 5
            if customers[j]['request_type'] in representatives[i]['skills']:
                expertise_match = 0
                
            # Uygunluk maliyeti: Temsilci ne kadar uygunsa o kadar düşük maliyet (10 - uygunluk değeri)
            availability_cost = 10 - representatives[i]['availability']
            
            # Tüm faktörlerin ağırlıklı toplamı
            cost_matrix[i][j] = distance_cost + expertise_match + availability_cost
    # O(n^2)

    # DP tablosunu oluştur: dp[i][j], ilk i temsilcinin ilk j müşteriye atanmasının minimum maliyeti
    dp = [[float('inf') for _ in range(n_customers + 1)] for _ in range(n_reps + 1)]
    dp[0][0] = 0
    
    # İlk satırı başlat - temsilci olmadan müşterilere atama yapılamaz (sonsuz maliyet)
    # 0 müşteri için maliyet her zaman 0'dır
    for j in range(1, n_customers + 1):
        dp[0][j] = float('inf')
    # O(n)
    
    # İlk sütunu başlat - 0 müşteri için maliyet her zaman 0'dır
    for i in range(n_reps + 1):
        dp[i][0] = 0
    
    # Hangi atamaların optimal çözüme yol açtığını takip et
    choices = [[-1 for _ in range(n_customers + 1)] for _ in range(n_reps + 1)]
    
    # DP tablosunu doldur
    for i in range(1, n_reps + 1):
        for j in range(1, n_customers + 1):
            # Seçenek 1: Mevcut temsilciyi yeni bir müşteriye atama
            dp[i][j] = dp[i-1][j]
            choices[i][j] = -1  # -1, "atama yapma" anlamına gelir
            
            # Bu temsilciyi atanmamış her müşteriye atamayı dene
            for k in range(1, j + 1):
                # Mevcut temsilciyi k. müşteriye atamanın daha iyi olup olmadığını kontrol et
                if dp[i-1][k-1] != float('inf'):
                    new_cost = dp[i-1][k-1] + cost_matrix[i-1][k-1]
                    if new_cost < dp[i][j]:
                        dp[i][j] = new_cost
                        choices[i][j] = k-1  # Müşteri indeksini sakla (0-tabanlı)
    
    # Çözümü yeniden yapılandır
    assignments = {}
    i, j = n_reps, n_customers
    
    while i > 0 and j > 0:
        if choices[i][j] != -1:
            customer_idx = choices[i][j]
            assignments[customers[customer_idx]['id']] = representatives[i-1]['id']
            j = customer_idx  # Bu atamadan önceki duruma geç
        i -= 1
    
    return assignments

def optimize_marketing_campaigns(campaigns, total_budget):
    # Bütçeyi tam sayıya çevir (bütçenin tam para birimi olduğunu varsayarak)
    budget = int(total_budget)
    n = len(campaigns)
    
    # DP tablosunu oluştur: dp[i][j], ilk i kampanyayı ve j bütçesini kullanarak 
    # elde edilebilecek maksimum ROI'yi temsil eder
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Optimal çözümde hangi öğelerin dahil edildiğini takip et
    included = [[False for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # DP tablosunu doldur
    for i in range(1, n + 1):
        campaign_cost = int(campaigns[i-1]['cost'])
        campaign_roi = campaigns[i-1]['expected_roi']
        
        for j in range(budget + 1):
            # Varsayılan olarak mevcut kampanyayı dahil etme
            dp[i][j] = dp[i-1][j]
            included[i][j] = False
            
            # Bu kampanyayı karşılayabilirsek, dahil etmenin ROI'yi iyileştirip iyileştirmediğini kontrol et
            if campaign_cost <= j:
                include_roi = dp[i-1][j-campaign_cost] + campaign_roi
                
                if include_roi > dp[i][j]:
                    dp[i][j] = include_roi
                    included[i][j] = True
    
    # Çözümü yeniden yapılandır
    selected_campaigns = []
    remaining_budget = budget
    
    for i in range(n, 0, -1):
        if included[i][remaining_budget]:
            selected_campaigns.append(campaigns[i-1]['id'])
            remaining_budget -= int(campaigns[i-1]['cost'])
    
    return selected_campaigns

class CRM_System:
    def __init__(self):
        self.representatives = []
        self.customers = []
        self.campaigns = []
        self.budget = 0
        
    def add_representative(self, rep_id, location, skills, availability):
        """Sisteme bir müşteri destek temsilcisi ekle."""
        self.representatives.append({
            'id': rep_id,
            'location': location,
            'skills': skills,
            'availability': availability  # 0-10 ölçeği, 10 en müsait demektir
        })
    
    def add_customer(self, customer_id, location, request_type, priority):
        """Sisteme bir müşteri ekle."""
        self.customers.append({
            'id': customer_id,
            'location': location,
            'request_type': request_type,
            'priority': priority  # 1-5 ölçeği, 5 en yüksek öncelik demektir
        })
    
    def add_campaign(self, campaign_id, cost, expected_roi):
        """Sisteme bir pazarlama kampanyası ekle."""
        self.campaigns.append({
            'id': campaign_id,
            'cost': cost,
            'expected_roi': expected_roi
        })
    
    def set_marketing_budget(self, budget):
        """Toplam pazarlama bütçesini ayarla."""
        self.budget = budget
    
    def optimize_support_assignments(self):
        """Müşteri destek temsilcisi atamalarını optimize et."""
        return optimize_customer_support_assignment(self.representatives, self.customers)
    
    def optimize_marketing_selection(self):
        """Pazarlama kampanyası seçimini optimize et."""
        return optimize_marketing_campaigns(self.campaigns, self.budget)
    
    def generate_report(self):
        """Optimize edilmiş sistem için kapsamlı bir rapor oluştur."""
        support_assignments = self.optimize_support_assignments()
        selected_campaigns = self.optimize_marketing_selection()
        
        # Seçilen kampanyalar için beklenen ROI'yi hesapla
        total_roi = 0
        for campaign in self.campaigns:
            if campaign['id'] in selected_campaigns:
                total_roi += campaign['expected_roi']
        
        report = {
            'support_assignments': support_assignments,
            'selected_campaigns': selected_campaigns,
            'total_customer_count': len(self.customers),
            'assigned_customer_count': len(support_assignments),
            'unassigned_customer_count': len(self.customers) - len(support_assignments),
            'campaign_count': len(self.campaigns),
            'selected_campaign_count': len(selected_campaigns),
            'marketing_budget': self.budget,
            'expected_roi': total_roi
        }
        
        return report

# CRM sistemi oluştur
crm = CRM_System()

# Temsilcileri ekle
crm.add_representative("REP001", "Istanbul", ["technical", "billing"], 8)
crm.add_representative("REP002", "Ankara", ["sales", "general"], 7)
crm.add_representative("REP003", "Istanbul", ["technical", "sales"], 9)

# Müşterileri ekle
crm.add_customer("CUST001", "Istanbul", "technical", 4)
crm.add_customer("CUST002", "Istanbul", "billing", 3)
crm.add_customer("CUST003", "Ankara", "general", 2)
crm.add_customer("CUST004", "Izmir", "sales", 5)

# Pazarlama kampanyalarını ekle
crm.add_campaign("CAMP001", 5000, 7500)  # ROI = 1.5
crm.add_campaign("CAMP002", 8000, 15000)  # ROI = 1.875
crm.add_campaign("CAMP003", 12000, 18000)  # ROI = 1.5
crm.add_campaign("CAMP004", 6000, 9000)  # ROI = 1.5
crm.add_campaign("CAMP005", 3000, 5500)  # ROI = 1.83

# Pazarlama bütçesini ayarla
crm.set_marketing_budget(20000)

# Rapor oluştur ve yazdır
report = crm.generate_report()
print("CRM Sistemi Optimizasyon Raporu:")
print("-------------------------------")
print(f"Toplam müşteri sayısı: {report['total_customer_count']}")
print(f"Atanan müşteri sayısı: {report['assigned_customer_count']}")
print(f"Atanmayan müşteri sayısı: {report['unassigned_customer_count']}")
print("\nMüşteri-Temsilci Atamaları:")
for customer_id, rep_id in report['support_assignments'].items():
    print(f"Müşteri {customer_id} -> Temsilci {rep_id}")

print("\nPazarlama Kampanyası Seçimi:")
print(f"Toplam kampanya sayısı: {report['campaign_count']}")
print(f"Seçilen kampanya sayısı: {report['selected_campaign_count']}")
print(f"Pazarlama bütçesi: {report['marketing_budget']}")
print(f"Beklenen ROI: {report['expected_roi']}")
print("\nSeçilen kampanyalar:")
for campaign_id in report['selected_campaigns']:
    print(f"- Kampanya {campaign_id}")