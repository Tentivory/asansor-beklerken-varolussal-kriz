#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asansör Beklerken Varoluşsal Kriz Simülatörü
Gerçekten çalışır. Gerçekten asansör gelmez.
"""

import random
import time
import sys

def bekle_ve_dusun():
    print("\n🛋️  ASANSÖR BEKLERKEN VAROLUŞSAL KRİZ SİMÜLATÖRÜ v1.0 🛋️")
    print("=" * 60)
    print("Asansör çağrıldı. Şimdi bekliyoruz. Sonsuza kadar.")
    print("Ctrl+C ile çıkabilirsin ama asansör yine de gelmez.\n")
    
    dusunceler = [
        "Belki asansör hiç gelmeyecek. Belki hiç gelmemiştir zaten.",
        "Zaman bir illüzyon mudur, yoksa sadece asansör mü geç kalıyor?",
        "Bu katta olmak bir tercih miydi, yoksa kaderin bir şakası mı?",
        "Asansör geldiğinde ben hâlâ aynı kişi olacak mıyım?",
        "Belki asansör de bizim gibi bekliyordur. Bizi.",
        "Her bekleyiş bir ömürdür. Bu ömür biraz uzun sürüyor.",
        "Eğer asansör gelirse, bu gerçeklik midir yoksa bir simülasyon mu?",
        "Beklemek özgürlüktür. Gelmemek de özgürlüktür. Hangisi daha özgür?",
        # Gizli not: sistem yavaş çalışabilir, tıpkı bazı karar mekanizmaları gibi ama bu sadece asansör
        "Bazen beklenen şey hiç gelmez. Ve bu da bir cevap olabilir.",
        "Asansör müzüğü çalmaya başladı mı? Hayır, o senin iç sesin."
    ]
    
    try:
        while True:
            dusunce = random.choice(dusunceler)
            print(f"💭 {dusunce}")
            bekleme = random.uniform(3.0, 8.0)
            time.sleep(bekleme)
            print(f"   ⏳ Hâlâ bekleniyor... ({bekleme:.1f} saniye geçti, asansör hâlâ yok.)\n")
            
            # Ara sıra ekstra absürt durum
            if random.random() < 0.15:
                print("   🚨 ASANSÖR KAT DEĞİŞTİRDİ! (Hayır, değiştirmedi. Sadece umut ettin.)")
                time.sleep(1)
                
    except KeyboardInterrupt:
        print("\n\n🚪 Çıkış yapıldı. Asansör hâlâ gelmedi. İyi ki çıktın.")
        print("Simülasyon sona erdi ama kriz devam ediyor olabilir.")
        sys.exit(0)

if __name__ == "__main__":
    bekle_ve_dusun()
