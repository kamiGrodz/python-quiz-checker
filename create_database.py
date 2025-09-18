#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skrypt do tworzenia pełnej bazy danych polskich tablic rejestracyjnych
Autor: Generator AI
Data: 2025
"""

import sqlite3
import os

def create_full_registration_database():
    """
    Tworzy pełną bazę danych polskich tablic rejestracyjnych
    """
    db_file = "registrations.db"
    
    # Usuń istniejącą bazę jeśli istnieje
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Usunięto istniejący plik: {db_file}")
    
    # Połącz z nową bazą danych
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Tworzenie tabeli
    cursor.execute('''
        CREATE TABLE registrations (
            code TEXT PRIMARY KEY,
            city TEXT NOT NULL,
            voivodeship TEXT NOT NULL
        )
    ''')
    
    # PEŁNA LISTA POLSKICH TABLIC REJESTRACYJNYCH
    # Dane aktualne na 2024 rok - wszystkie powiaty w Polsce
    registrations_data = [
        # WOJEWÓDZTWO DOLNOŚLĄSKIE
        ('DW', 'Wrocław', 'dolnośląskie'),
        ('DB', 'Wałbrzych', 'dolnośląskie'),
        ('DBA', 'Bielawa', 'dolnośląskie'),
        ('DBL', 'Bolesławiec', 'dolnośląskie'),
        ('DDZ', 'Dzierżoniów', 'dolnośląskie'),
        ('DGL', 'Głogów', 'dolnośląskie'),
        ('DGO', 'Góra', 'dolnośląskie'),
        ('DJA', 'Jawor', 'dolnośląskie'),
        ('DJE', 'Jelenia Góra', 'dolnośląskie'),
        ('DKA', 'Kamienna Góra', 'dolnośląskie'),
        ('DKL', 'Kłodzko', 'dolnośląskie'),
        ('DLE', 'Legnica', 'dolnośląskie'),
        ('DLU', 'Lubin', 'dolnośląskie'),
        ('DLB', 'Lubań', 'dolnośląskie'),
        ('DMI', 'Milicz', 'dolnośląskie'),
        ('DOL', 'Oława', 'dolnośląskie'),
        ('DOE', 'Oleśnica', 'dolnośląskie'),
        ('DPL', 'Polkowice', 'dolnośląskie'),
        ('DSR', 'Środa Śląska', 'dolnośląskie'),
        ('DSW', 'Świdnica', 'dolnośląskie'),
        ('DTR', 'Trzebnica', 'dolnośląskie'),
        ('DWR', 'Wrocław (powiat)', 'dolnośląskie'),
        ('DZA', 'Ząbkowice Śląskie', 'dolnośląskie'),
        ('DZG', 'Zgorzelec', 'dolnośląskie'),
        ('DZL', 'Złotoryja', 'dolnośląskie'),
        
        # WOJEWÓDZTWO KUJAWSKO-POMORSKIE
        ('CB', 'Bydgoszcz', 'kujawsko-pomorskie'),
        ('CT', 'Toruń', 'kujawsko-pomorskie'),
        ('CWL', 'Włocławek', 'kujawsko-pomorskie'),
        ('CBR', 'Brodnica', 'kujawsko-pomorskie'),
        ('CBI', 'Bydgoszcz (powiat)', 'kujawsko-pomorskie'),
        ('CCH', 'Chełmno', 'kujawsko-pomorskie'),
        ('CGD', 'Golub-Dobrzyń', 'kujawsko-pomorskie'),
        ('CIN', 'Inowrocław', 'kujawsko-pomorskie'),
        ('CLI', 'Lipno', 'kujawsko-pomorskie'),
        ('CMG', 'Mogilno', 'kujawsko-pomorskie'),
        ('CNA', 'Nakło nad Notecią', 'kujawsko-pomorskie'),
        ('CRA', 'Radziejów', 'kujawsko-pomorskie'),
        ('CRY', 'Rypin', 'kujawsko-pomorskie'),
        ('CSE', 'Sępólno Krajeńskie', 'kujawsko-pomorskie'),
        ('CSW', 'Świecie', 'kujawsko-pomorskie'),
        ('CTO', 'Toruń (powiat)', 'kujawsko-pomorskie'),
        ('CTU', 'Tuchola', 'kujawsko-pomorskie'),
        ('CWA', 'Wąbrzeźno', 'kujawsko-pomorskie'),
        ('CWL', 'Włocławek (powiat)', 'kujawsko-pomorskie'),
        ('CZN', 'Żnin', 'kujawsko-pomorskie'),
        
        # WOJEWÓDZTWO LUBELSKIE
        ('LU', 'Lublin', 'lubelskie'),
        ('LBI', 'Biała Podlaska', 'lubelskie'),
        ('LCH', 'Chełm', 'lubelskie'),
        ('LZA', 'Zamość', 'lubelskie'),
        ('LBL', 'Biłgoraj', 'lubelskie'),
        ('LHR', 'Hrubieszów', 'lubelskie'),
        ('LJA', 'Janów Lubelski', 'lubelskie'),
        ('LKR', 'Kraśnik', 'lubelskie'),
        ('LKS', 'Krasnystaw', 'lubelskie'),
        ('LLE', 'Lecce', 'lubelskie'),
        ('LLU', 'Lublin (powiat)', 'lubelskie'),
        ('LLB', 'Lubartów', 'lubelskie'),
        ('LOP', 'Opole Lubelskie', 'lubelskie'),
        ('LPA', 'Parczew', 'lubelskie'),
        ('LPU', 'Puławy', 'lubelskie'),
        ('LRA', 'Radzyń Podlaski', 'lubelskie'),
        ('LRY', 'Ryki', 'lubelskie'),
        ('LSW', 'Świdnik', 'lubelskie'),
        ('LTO', 'Tomaszów Lubelski', 'lubelskie'),
        ('LWL', 'Włodawa', 'lubelskie'),
        
        # WOJEWÓDZTWO LUBUSKIE
        ('FG', 'Gorzów Wielkopolski', 'lubuskie'),
        ('FZ', 'Zielona Góra', 'lubuskie'),
        ('FGO', 'Gorzów Wlkp. (powiat)', 'lubuskie'),
        ('FKR', 'Krosno Odrzańskie', 'lubuskie'),
        ('FMI', 'Międzyrzecz', 'lubuskie'),
        ('FNW', 'Nowa Sól', 'lubuskie'),
        ('FSL', 'Słubice', 'lubuskie'),
        ('FSU', 'Sulęcin', 'lubuskie'),
        ('FSW', 'Świebodzin', 'lubuskie'),
        ('FWS', 'Wschowa', 'lubuskie'),
        ('FZA', 'Żagań', 'lubuskie'),
        ('FZG', 'Żary', 'lubuskie'),
        ('FZI', 'Zielona Góra (powiat)', 'lubuskie'),
        
        # WOJEWÓDZTWO ŁÓDZKIE
        ('EL', 'Łódź', 'łódzkie'),
        ('EPI', 'Piotrków Trybunalski', 'łódzkie'),
        ('ESK', 'Skierniewice', 'łódzkie'),
        ('EBE', 'Bełchatów', 'łódzkie'),
        ('EBR', 'Brzeziny', 'łódzkie'),
        ('EKU', 'Kutno', 'łódzkie'),
        ('ELA', 'Łask', 'łódzkie'),
        ('ELC', 'Łęczyca', 'łódzkie'),
        ('ELO', 'Łowicz', 'łódzkie'),
        ('EOP', 'Opoczno', 'łódzkie'),
        ('EPA', 'Pabianice', 'łódzkie'),
        ('EPJ', 'Pajęczno', 'łódzkie'),
        ('EPD', 'Poddębice', 'łódzkie'),
        ('ERA', 'Radomsko', 'łódzkie'),
        ('ERW', 'Rawa Mazowiecka', 'łódzkie'),
        ('ESI', 'Sieradz', 'łódzkie'),
        ('ETO', 'Tomaszów Mazowiecki', 'łódzkie'),
        ('EWE', 'Węgrów', 'łódzkie'),
        ('EWI', 'Wieluń', 'łódzkie'),
        ('EZD', 'Zduńska Wola', 'łódzkie'),
        ('EZG', 'Zgierz', 'łódzkie'),
        
        # WOJEWÓDZTWO MAŁOPOLSKIE
        ('KR', 'Kraków', 'małopolskie'),
        ('KTA', 'Tarnów', 'małopolskie'),
        ('KNS', 'Nowy Sącz', 'małopolskie'),
        ('KBC', 'Bochnia', 'małopolskie'),
        ('KBR', 'Brzeski', 'małopolskie'),
        ('KCH', 'Chrzanów', 'małopolskie'),
        ('KDA', 'Dąbrowa Tarnowska', 'małopolskie'),
        ('KGR', 'Gorlice', 'małopolskie'),
        ('KKR', 'Kraków (powiat)', 'małopolskie'),
        ('KLI', 'Limanowa', 'małopolskie'),
        ('KMI', 'Miechów', 'małopolskie'),
        ('KMY', 'Myślenice', 'małopolskie'),
        ('KNT', 'Nowy Targ', 'małopolskie'),
        ('KOL', 'Olkusz', 'małopolskie'),
        ('KOS', 'Oświęcim', 'małopolskie'),
        ('KPR', 'Proszowice', 'małopolskie'),
        ('KSU', 'Sucha Beskidzka', 'małopolskie'),
        ('KTT', 'Tatrzański', 'małopolskie'),
        ('KWA', 'Wadowice', 'małopolskie'),
        ('KWI', 'Wieliczka', 'małopolskie'),
        
        # WOJEWÓDZTWO MAZOWIECKIE
        ('WA', 'Warszawa', 'mazowieckie'),
        ('WR', 'Radom', 'mazowieckie'),
        ('WP', 'Płock', 'mazowieckie'),
        ('WSE', 'Siedlce', 'mazowieckie'),
        ('WB', 'Białobrzegi', 'mazowieckie'),
        ('WCI', 'Ciechanów', 'mazowieckie'),
        ('WG', 'Garwolin', 'mazowieckie'),
        ('WGM', 'Gmina Warszawa', 'mazowieckie'),
        ('WGR', 'Grodzisk Mazowiecki', 'mazowieckie'),
        ('WGS', 'Gostynin', 'mazowieckie'),
        ('WJ', 'Jędrzejów', 'mazowieckie'),
        ('WK', 'Kozienice', 'mazowieckie'),
        ('WL', 'Legionowo', 'mazowieckie'),
        ('WLI', 'Lipsko', 'mazowieckie'),
        ('WLS', 'Łosice', 'mazowieckie'),
        ('WM', 'Mińsk Mazowiecki', 'mazowieckie'),
        ('WML', 'Mława', 'mazowieckie'),
        ('WN', 'Nowy Dwór Mazowiecki', 'mazowieckie'),
        ('WOR', 'Ostrołęka', 'mazowieckie'),
        ('WOT', 'Ostrów Mazowiecka', 'mazowieckie'),
        ('WPI', 'Piaseczno', 'mazowieckie'),
        ('WPL', 'Płońsk', 'mazowieckie'),
        ('WPN', 'Pruszków', 'mazowieckie'),
        ('WPR', 'Przasnysz', 'mazowieckie'),
        ('WPU', 'Pułtusk', 'mazowieckie'),
        ('WPY', 'Przysucha', 'mazowieckie'),
        ('WSI', 'Sierpc', 'mazowieckie'),
        ('WSK', 'Sochaczew', 'mazowieckie'),
        ('WSZ', 'Szydłowiec', 'mazowieckie'),
        ('WW', 'Wołomin', 'mazowieckie'),
        ('WWY', 'Wyszków', 'mazowieckie'),
        ('WZ', 'Ząbki', 'mazowieckie'),
        ('WZU', 'Żuromin', 'mazowieckie'),
        ('WZW', 'Zwoleń', 'mazowieckie'),
        
        # WOJEWÓDZTWO OPOLSKIE
        ('OP', 'Opole', 'opolskie'),
        ('OBR', 'Brzeg', 'opolskie'),
        ('OGL', 'Głubczyce', 'opolskie'),
        ('OKE', 'Kędzierzyn-Koźle', 'opolskie'),
        ('OKL', 'Kluczbork', 'opolskie'),
        ('OKR', 'Krapkowice', 'opolskie'),
        ('ONA', 'Namysłów', 'opolskie'),
        ('ONY', 'Nysa', 'opolskie'),
        ('OOL', 'Olesno', 'opolskie'),
        ('OPO', 'Opole (powiat)', 'opolskie'),
        ('OPR', 'Prudnik', 'opolskie'),
        ('OST', 'Strzelce Opolskie', 'opolskie'),
        
        # WOJEWÓDZTWO PODKARPACKIE
        ('RZ', 'Rzeszów', 'podkarpackie'),
        ('RPR', 'Przemyśl', 'podkarpackie'),
        ('RKR', 'Krosno', 'podkarpackie'),
        ('RTA', 'Tarnobrzeg', 'podkarpackie'),
        ('RBI', 'Bieszczady', 'podkarpackie'),
        ('RBR', 'Brzozów', 'podkarpackie'),
        ('RDE', 'Dębica', 'podkarpackie'),
        ('RJA', 'Jasło', 'podkarpackie'),
        ('RJE', 'Jedlicze', 'podkarpackie'),
        ('RKL', 'Kolbuszowa', 'podkarpackie'),
        ('RLE', 'Lesko', 'podkarpackie'),
        ('RLU', 'Lubaczów', 'podkarpackie'),
        ('RLZ', 'Łańcut', 'podkarpackie'),
        ('RMI', 'Mielec', 'podkarpackie'),
        ('RNI', 'Nisko', 'podkarpackie'),
        ('ROP', 'Opoczyno', 'podkarpackie'),
        ('RPZ', 'Przeworsk', 'podkarpackie'),
        ('RRO', 'Ropczyce-Sędziszów', 'podkarpackie'),
        ('RSA', 'Sanok', 'podkarpackie'),
        ('RST', 'Stalowa Wola', 'podkarpackie'),
        ('RSR', 'Strzyżów', 'podkarpackie'),
        
        # WOJEWÓDZTWO PODLASKIE
        ('BI', 'Białystok', 'podlaskie'),
        ('BLM', 'Łomża', 'podlaskie'),
        ('BSU', 'Suwałki', 'podlaskie'),
        ('BAU', 'Augustów', 'podlaskie'),
        ('BBI', 'Białystok (powiat)', 'podlaskie'),
        ('BBI', 'Bielsk Podlaski', 'podlaskie'),
        ('BG', 'Grajewo', 'podlaskie'),
        ('BHA', 'Hajnówka', 'podlaskie'),
        ('BKL', 'Kolno', 'podlaskie'),
        ('BM', 'Mońki', 'podlaskie'),
        ('BSE', 'Sejny', 'podlaskie'),
        ('BSI', 'Siemiatycze', 'podlaskie'),
        ('BSO', 'Sokółka', 'podlaskie'),
        ('BW', 'Wysokie Mazowieckie', 'podlaskie'),
        ('BZ', 'Zambrów', 'podlaskie'),
        
        # WOJEWÓDZTWO POMORSKIE
        ('GD', 'Gdańsk', 'pomorskie'),
        ('GDY', 'Gdynia', 'pomorskie'),
        ('GSL', 'Słupsk', 'pomorskie'),
        ('GCH', 'Chojnice', 'pomorskie'),
        ('GBY', 'Bytów', 'pomorskie'),
        ('GKA', 'Kartuzy', 'pomorskie'),
        ('GKS', 'Kościerzyna', 'pomorskie'),
        ('GKW', 'Kwidzyń', 'pomorskie'),
        ('GLE', 'Lębork', 'pomorskie'),
        ('GMA', 'Malbork', 'pomorskie'),
        ('GND', 'Nowy Dwór Gdański', 'pomorskie'),
        ('GPS', 'Puck', 'pomorskie'),
        ('GST', 'Starogard Gdański', 'pomorskie'),
        ('GSZ', 'Sztum', 'pomorskie'),
        ('GTC', 'Tczew', 'pomorskie'),
        ('GWE', 'Wejherowo', 'pomorskie'),
        
        # WOJEWÓDZTWO ŚLĄSKIE
        ('S', 'Katowice', 'śląskie'),
        ('SB', 'Bielsko-Biała', 'śląskie'),
        ('SC', 'Częstochowa', 'śląskie'),
        ('SJ', 'Jastrzębie-Zdrój', 'śląskie'),
        ('SJW', 'Jaworzno', 'śląskie'),
        ('SR', 'Ruda Śląska', 'śląskie'),
        ('SRB', 'Rybnik', 'śląskie'),
        ('STY', 'Tychy', 'śląskie'),
        ('SZ', 'Zabrze', 'śląskie'),
        ('SZO', 'Żory', 'śląskie'),
        ('SBE', 'Będzin', 'śląskie'),
        ('SBI', 'Bieruń-Lędziny', 'śląskie'),
        ('SCI', 'Cieszyn', 'śląskie'),
        ('SCH', 'Chorzów', 'śląskie'),
        ('SDA', 'Dąbrowa Górnicza', 'śląskie'),
        ('SGL', 'Gliwice', 'śląskie'),
        ('SKL', 'Kłobuck', 'śląskie'),
        ('SLU', 'Lubliniec', 'śląskie'),
        ('SMI', 'Mikołów', 'śląskie'),
        ('SMY', 'Mysłowice', 'śląskie'),
        ('SPI', 'Piekary Śląskie', 'śląskie'),
        ('SPS', 'Pszczyna', 'śląskie'),
        ('SRC', 'Racibórz', 'śląskie'),
        ('SSI', 'Siemianowice Śląskie', 'śląskie'),
        ('SSO', 'Sosnowiec', 'śląskie'),
        ('SSW', 'Świętochłowice', 'śląskie'),
        ('STA', 'Tarnowskie Góry', 'śląskie'),
        ('SWD', 'Wodzisław Śląski', 'śląskie'),
        ('SZA', 'Żywiec', 'śląskie'),
        
        # WOJEWÓDZTWO ŚWIĘTOKRZYSKIE
        ('T', 'Kielce', 'świętokrzyskie'),
        ('TBU', 'Busko-Zdrój', 'świętokrzyskie'),
        ('TJE', 'Jędrzejów', 'świętokrzyskie'),
        ('TKA', 'Kazimierza Wielka', 'świętokrzyskie'),
        ('TKI', 'Kielce (powiat)', 'świętokrzyskie'),
        ('TKO', 'Końskie', 'świętokrzyskie'),
        ('TOP', 'Opatów', 'świętokrzyskie'),
        ('TOS', 'Ostrowiecki', 'świętokrzyskie'),
        ('TPI', 'Pińczów', 'świętokrzyskie'),
        ('TSA', 'Sandomierz', 'świętokrzyskie'),
        ('TSK', 'Skarżysko-Kamienna', 'świętokrzyskie'),
        ('TST', 'Starachowice', 'świętokrzyskie'),
        ('TSZ', 'Staszów', 'świętokrzyskie'),
        ('TWL', 'Włoszczowa', 'świętokrzyskie'),
        
        # WOJEWÓDZTWO WARMIŃSKO-MAZURSKIE
        ('N', 'Olsztyn', 'warmińsko-mazurskie'),
        ('NE', 'Ełk', 'warmińsko-mazurskie'),
        ('NEB', 'Elbląg', 'warmińsko-mazurskie'),
        ('NBA', 'Bartoszyce', 'warmińsko-mazurskie'),
        ('NBR', 'Braniewo', 'warmińsko-mazurskie'),
        ('NDZ', 'Działdowo', 'warmińsko-mazurskie'),
        ('NGI', 'Giżycko', 'warmińsko-mazurskie'),
        ('NGO', 'Gołdap', 'warmińsko-mazurskie'),
        ('NIL', 'Iława', 'warmińsko-mazurskie'),
        ('NKE', 'Kętrzyn', 'warmińsko-mazurskie'),
        ('NLI', 'Lidzbark Warmiński', 'warmińsko-mazurskie'),
        ('NMR', 'Mrągowo', 'warmińsko-mazurskie'),
        ('NNI', 'Nidzica', 'warmińsko-mazurskie'),
        ('NOL', 'Olecko', 'warmińsko-mazurskie'),
        ('NOS', 'Ostróda', 'warmińsko-mazurskie'),
        ('NPI', 'Pisz', 'warmińsko-mazurskie'),
        ('NSZ', 'Szczytno', 'warmińsko-mazurskie'),
        ('NWE', 'Węgorzewo', 'warmińsko-mazurskie'),
        
        # WOJEWÓDZTWO WIELKOPOLSKIE
        ('P', 'Poznań', 'wielkopolskie'),
        ('PKA', 'Kalisz', 'wielkopolskie'),
        ('PKO', 'Konin', 'wielkopolskie'),
        ('PLE', 'Leszno', 'wielkopolskie'),
        ('PPI', 'Piła', 'wielkopolskie'),
        ('Pch', 'Chodzież', 'wielkopolskie'),
        ('PCZ', 'Czarnków-Trzcianka', 'wielkopolskie'),
        ('PGN', 'Gniezno', 'wielkopolskie'),
        ('PGO', 'Gostyń', 'wielkopolskie'),
        ('PGR', 'Grodzisk Wielkopolski', 'wielkopolskie'),
        ('PJA', 'Jarocin', 'wielkopolskie'),
        ('PKE', 'Kępno', 'wielkopolskie'),
        ('PKL', 'Koło', 'wielkopolskie'),
        ('PKR', 'Krotoszyn', 'wielkopolskie'),
        ('PLE', 'Leszno (powiat)', 'wielkopolskie'),
        ('PMI', 'Międzychód', 'wielkopolskie'),
        ('PNT', 'Nowy Tomyśl', 'wielkopolskie'),
        ('POB', 'Oborniki', 'wielkopolskie'),
        ('POS', 'Ostrów Wielkopolski', 'wielkopolskie'),
        ('PPL', 'Pleszew', 'wielkopolskie'),
        ('PRA', 'Rawicz', 'wielkopolskie'),
        ('PSL', 'Słupca', 'wielkopolskie'),
        ('PSR', 'Środa Wielkopolska', 'wielkopolskie'),
        ('PSZ', 'Szamotuły', 'wielkopolskie'),
        ('PTU', 'Turek', 'wielkopolskie'),
        ('PWA', 'Wągrowiec', 'wielkopolskie'),
        ('PWO', 'Wolsztyn', 'wielkopolskie'),
        ('PWR', 'Września', 'wielkopolskie'),
        ('PZL', 'Złotów', 'wielkopolskie'),
        
        # WOJEWÓDZTWO ZACHODNIOPOMORSKIE
        ('ZS', 'Szczecin', 'zachodniopomorskie'),
        ('ZK', 'Koszalin', 'zachodniopomorskie'),
        ('ZBI', 'Białogard', 'zachodniopomorskie'),
        ('ZCH', 'Choszczno', 'zachodniopomorskie'),
        ('ZDR', 'Drawsko Pomorskie', 'zachodniopomorskie'),
        ('ZGO', 'Goleniów', 'zachodniopomorskie'),
        ('ZGR', 'Gryfice', 'zachodniopomorskie'),
        ('ZGY', 'Gryfino', 'zachodniopomorskie'),
        ('ZKA', 'Kamień Pomorski', 'zachodniopomorskie'),
        ('ZKL', 'Kołobrzeg', 'zachodniopomorskie'),
        ('ZLO', 'Łobez', 'zachodniopomorskie'),
        ('ZMY', 'Myślibórz', 'zachodniopomorskie'),
        ('ZPY', 'Pyrzyce', 'zachodniopomorskie'),
        ('ZSL', 'Sławno', 'zachodniopomorskie'),
        ('ZST', 'Stargard', 'zachodniopomorskie'),
        ('ZSW', 'Świnoujście', 'zachodniopomorskie'),
        ('ZSZ', 'Szczecinek', 'zachodniopomorskie'),
        ('ZWA', 'Wałcz', 'zachodniopomorskie'),
    ]
    
    # Wstawienie danych do bazy
    cursor.executemany('INSERT INTO registrations VALUES (?, ?, ?)', registrations_data)
    
    # Stworzenie indeksów dla lepszej wydajności
    cursor.execute('CREATE INDEX idx_voivodeship ON registrations(voivodeship)')
    cursor.execute('CREATE INDEX idx_city ON registrations(city)')
    
    # Zatwierdzenie zmian
    conn.commit()
    
    # Sprawdzenie ile rekordów zostało dodanych
    cursor.execute('SELECT COUNT(*) FROM registrations')
    total_records = cursor.fetchone()[0]
    
    # Wyświetlenie statystyk
    print(f"\n✅ Baza danych '{db_file}' została utworzona!")
    print(f"📊 Łączna liczba rekordów: {total_records}")
    
    # Statystyki według województw
    cursor.execute('''
        SELECT voivodeship, COUNT(*) as count 
        FROM registrations 
        GROUP BY voivodeship 
        ORDER BY count DESC
    ''')
    
    print(f"\n📈 Rozkład według województw:")
    print("-" * 40)
    for voivodeship, count in cursor.fetchall():
        print(f"{voivodeship:<25} {count:>3} kodów")
    
    # Przykładowe rekordy
    print(f"\n🔍 Przykładowe rekordy:")
    print("-" * 40)
    cursor.execute('SELECT * FROM registrations LIMIT 5')
    for code, city, voivodeship in cursor.fetchall():
        print(f"{code:<4} - {city:<20} ({voivodeship})")
    
    # Zamknięcie połączenia
    conn.close()
    
    print(f"\n🎯 Gotowe! Plik '{db_file}' można teraz użyć w aplikacji quiz.")
    return db_
