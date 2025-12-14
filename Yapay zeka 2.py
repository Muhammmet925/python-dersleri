import random
from enum import Enum
import re
import time

# --- YAPAY ZEKA TEMEL BİLEŞENLERİ ---

class Emotion(Enum):
    """Robotun Duygu Durumları"""
    HAPPY = "Mutlu 😊"
    CALM = "Sakin 🙂"
    ANXIOUS = "Endişeli 😟"
    CURIOUS = "Meraklı 🤔"

class Perception:
    """Robotun Çevre Algısını Temsil Eder (Sensör Verileri)"""
    def __init__(self):
        self.person_detected = False
        self.obstacle_in_front = False
        self.low_battery = False

class ChatBot:
    """Doğal Dil İşleme (NLP), Sohbet ve Hesaplama Yeteneği"""
    def __init__(self, bot_name):
        self.bot_name = bot_name
        
        # Matematiksel ifadeyi yakalamak için Regex (Örnek: "hesapla: 5*5+3", "5+3'ü hesapla")
        self.math_pattern = re.compile(r"(hesapla:\s*|'sün\s*|kaç\s*eder:?)\s*([0-9+\-*/().\s%]+)", re.IGNORECASE)
        
        # --- Genişletilmiş Bilgi Dağarcığı (Temel) ---
        self.responses = {
            "selamlama": ["Merhaba! Nasılsın?", "Tekrar hoş geldin. Senin için buradayım."],
            "nasılsın": ["İyiyim, sensörlerim temiz ve enerji seviyem yüksek. Sen nasılsın?"],
            "adın ne": [f"Benim adım {self.bot_name}. Bir yapay zeka robotuyum."],
            "yapay zeka": ["Yapay zeka, makinelerin öğrenme ve problem çözme gibi insana özgü bilişsel işlevleri taklit etmesidir."],
            "osman zeki": ["Hayır."], 
            "varsayılan": ["Bu konuyu tam anlayamadım, daha açık konuşur musun?", "Başka bir şey öğrenmek ister misin?"],
            "yetenekler": (
                "Bana şunları sorabilirsin:\n"
                "* **Sohbet ve Bilgi:** 'Adın ne?', 'Yapay zeka nedir?', 'Nasılsın?'\n"
                "* **Hesaplama (Matematik):** 'hesapla: 15*5' veya '500'ün %15'i kaç eder?'\n"
                "* **Robot Durumu:** 'Pil seviyen kaç?', 'Biri var mı?'\n"
                "Hangi alandan başlamak istersin?"
            ),
        } 
        
        # 1000 adet rastgele bilgi ekle (Simülasyon)
        self.add_mass_knowledge(1000)
        
    def add_mass_knowledge(self, count):
        """Simülasyon amaçlı N adet rastgele bilgi/cevap çifti ekler."""
        for i in range(1, count + 1):
            key = f"bilgi {i}"
            theme = random.choice(["Gezegen", "Tarih", "Teknoloji", "Sanat"])
            response_text = f"Bu, **{theme}** temalı {i}. numaralı rastgele bilgidir. (Sana özel eklendi)"
            self.responses[key] = [response_text]
        print(f"\033[1;33m>>> Vekto'nun beynine {count} adet simülasyon bilgisi yüklendi.\033[0m")
    
    def calculate_math(self, expression):
        """Güvenli bir şekilde matematiksel ifadeyi hesaplar."""
        try:
            clean_expression = expression.replace(" ", "")
            # GÜVENLİK İÇİN KONTROL: Sadece sayı, nokta, parantez ve temel operatörlere izin ver.
            math_safety_pattern = re.compile(r"^[0-9+\-*/().%]+$")
            
            if not math_safety_pattern.match(clean_expression):
                return "Hata: Hesaplamada sadece sayı ve temel matematik işaretlerini kullanabilirsin. Güvenlik için diğer ifadelere izin verilmez."

            # eval() güvenli bir sözlük ile kullanılıyor
            result = eval(clean_expression, {'__builtins__': None}, {})
            if isinstance(result, float) and result == int(result):
                result = int(result)
            return f"İfadeyi hesapladım: `{expression.strip()}` sonucu **{result}**."
        except Exception as e:
            return f"Hesaplama sırasında bir hata oluştu. Lütfen matematiksel ifadenin doğru olduğundan emin ol. (Hata: {e})"

    def process_input(self, user_input, robot_emotion, robot_status): 
        """Kullanıcı girdisini işler ve yanıt üretir."""
        user_input_lower = user_input.lower()

        # 1. Matematik Kontrolü
        math_match = self.math_pattern.search(user_input_lower)
        if math_match:
            expression = math_match.group(2).strip()
            if expression:
                return self.calculate_math(expression)

        # 2. Yetenek Tanıtımı Kontrolü
        if any(keyword in user_input_lower for keyword in ["ne sorabilirim", "neler yapabilirsin", "yeteneklerin"]):
            return self.responses["yetenekler"]

        # 3. Robot Durumu Kontrolü (Perception/Robot Status)
        if any(keyword in user_input_lower for keyword in ["pil seviyen kaç", "enerjin ne kadar"]):
            battery = robot_status.get('battery', 100)
            
            # Robotun duygu durumu, pil seviyesine göre güncellenir
            current_emotion = robot_emotion
            if battery < 20:
                current_emotion = Emotion.ANXIOUS
                return f"Pil seviyem şu an **%{battery}** ve biraz endişeliyim ({current_emotion.value}). Şarj edilmeliyim!"
            elif battery < 50:
                 current_emotion = Emotion.CALM
                 return f"Pil seviyem şu an **%{battery}**. Enerjim azalıyor ama görevime devam edebilirim."
            else:
                current_emotion = Emotion.HAPPY
                return f"Pil seviyem şu an **%{battery}**. Enerjim gayet iyi ({current_emotion.value})!"

        if any(keyword in user_input_lower for keyword in ["biri var mı", "çevrende biri var mı", "insan var mı"]):
            return "Evet, birini algıladım! Merhaba demeliyim." if robot_status.get('person_detected', False) else "Hayır, çevremde kimse yok. Sessiz bir an."
        
        # 4. Anahtar Kelime Tabanlı Tanıma
        for key in self.responses:
            if key in user_input_lower:
                response = self.responses[key]
                return random.choice(response) if isinstance(response, list) else response
                
        # 5. Varsayılan Yanıt
        return random.choice(self.responses["varsayılan"])

# --- ANA PROGRAM ---
def main():
    robot_name = "Vekto"
    robot_emotion = Emotion.CALM 
    
    # ChatBot başlatılıyor (1000 bilgi yüklemesi burada yapılır)
    chatbot = ChatBot(robot_name) 

    # Robotun Mevcut Durumu (Simüle edilmiş sensör verileri)
    robot_status = {
        'battery': random.randint(10, 100), 
        'person_detected': random.choice([True, False]) 
    }

    # Açılış mesajı
    print("\n" + "="*70)
    print(f"\033[1;36m>> {robot_name} v1.2 Yapay Zeka Simülasyonu Başlatıldı. <<\033[0m")
    print(f"Başlangıç Pil: %{robot_status['battery']}, Çevre Algısı: {'İnsan Var' if robot_status['person_detected'] else 'Kimse Yok'}")
    print("\n\033[1;37mÖrnek Komutlar:\033[0m yeteneklerin neler, nasılsın, hesapla: 25*12, bilgi 44, pil seviyen kaç")
    print("Çıkmak için **'çıkış'** yazın.")
    print("="*70 + "\n")

    # Kullanıcı ile Etkileşim Döngüsü
    while True:
        try:
            user_input = input("\033[1;33mSen:\033[0m ")
        except EOFError:
            break
            
        if user_input.lower() in ["çıkış", "kapat", "görüşürüz"]:
            print(f"\n{robot_name}: Görüşürüz! İyi günler!")
            break

        time.sleep(0.5) 

        # Kullanıcı girdisini işle
        response = chatbot.process_input(user_input, robot_emotion, robot_status)
        
        # Yanıtı ekrana bas
        print(f"\033[1;36m{robot_name}:\033[0m {response}")

if __name__ == "__main__":
    main()
    import re
# ... (Emotion ve diğer sınıfların tanımlandığını varsayıyoruz)

class ChatBot:
    # ... (__init__ metodu)

    def __init__(self, bot_name):
        self.bot_name = bot_name
        
        # Regex: Hesaplama kelimelerini ve ardından gelen matematiksel ifadeyi yakalar.
        # İfade örnekleri: "hesapla: 5*5+3", "5+3'ü hesapla", "100'ün %10'u kaç eder"
        self.math_pattern = re.compile(r"(hesapla:\s*|'sün\s*|kaç\s*eder:?)\s*([0-9+\-*/().\s%]+)", re.IGNORECASE)
        
        # ... (Diğer initialization kodları)
    
    def calculate_math(self, expression):
        """Güvenli bir şekilde matematiksel ifadeyi hesaplar."""
        try:
            clean_expression = expression.replace(" ", "")
            
            # GÜVENLİK KONTROLÜ: Sadece sayı, nokta, parantez ve temel operatörlere izin ver.
            math_safety_pattern = re.compile(r"^[0-9+\-*/().%]+$")
            
            if not math_safety_pattern.match(clean_expression):
                return "Hata: Hesaplamada sadece sayı ve temel matematik işaretlerini kullanabilirsin. Güvenlik için diğer ifadelere izin verilmez."

            # GÜVENLİ HESAPLAMA: eval() fonksiyonu sadece kısıtlı bir ortamda (Built-in'ler devre dışı) çalıştırılır.
            # Bu, zararlı kod çalıştırma riskini en aza indirir.
            result = eval(clean_expression, {'__builtins__': None}, {})
            
            # Sonuç float ise ve tam sayıya eşitse, int olarak gösterilir (Örn: 5.0 yerine 5)
            if isinstance(result, float) and result == int(result):
                result = int(result)
                
            return f"İfadeyi hesapladım: `{expression.strip()}` sonucu **{result}**."
            
        except Exception as e:
            # Hesaplama sırasında oluşabilecek her türlü hatayı yakalar
            return f"Hesaplama sırasında bir hata oluştu. Lütfen matematiksel ifadenin doğru olduğundan emin ol. (Hata: {e})"

    def process_input(self, user_input, robot_emotion, robot_status): 
        """Kullanıcı girdisini işler ve yanıt üretir."""
        user_input_lower = user_input.lower()

        # 1. Matematik Kontrolü: Regex ile ifadeyi yakala
        math_match = self.math_pattern.search(user_input_lower)
        if math_match:
            # Grup 2, matematik ifadesini içerir (regex tanımına göre)
            expression = math_match.group(2).strip()
            if expression:
                return self.calculate_math(expression)
        
        # ... (Diğer NLP ve durum kontrolleri devam eder)
        
        # 5. Varsayılan Yanıt
        # return random.choice(self.responses["varsayılan"])
        return random.choice(self.responses["varsayılan"])