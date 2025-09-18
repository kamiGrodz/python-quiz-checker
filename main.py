import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import random
import sqlite3
import os

# Konfiguracja CustomTkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class RegistrationQuiz:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Quiz Tablic Rejestracyjnych")
        self.root.geometry("800x600")
        self.root.configure(fg_color="#f0f4f8")
        
        # Zmienne aplikacji
        self.current_question = None
        self.correct_answer = None
        self.answer_buttons = []
        self.wrong_answers_count = 3
        self.question_answered = False
        
        # Inicjalizacja bazy danych
        self.init_database()
        
        # Tworzenie interfejsu
        self.create_widgets()
        
    def init_database(self):
        """Inicjalizacja bazy danych z tablicami rejestracyjnymi"""
        db_file = "registrations.db"  # Plik bazy danych
        
        # Sprawdź czy baza już istnieje
        database_exists = os.path.exists(db_file)
        
        # Połącz z bazą (utworzy plik jeśli nie istnieje)
        self.conn = sqlite3.connect(db_file)
        cursor = self.conn.cursor()
        
        # Jeśli baza nie istnieje lub jest pusta - inicjalizuj
        if not database_exists:
            print("Tworzenie nowej bazy danych...")
            
            # Tworzenie tabeli
            cursor.execute('''
                CREATE TABLE registrations (
                    code TEXT PRIMARY KEY,
                    city TEXT NOT NULL
                )
            ''')
            
            # Przykładowe dane - polskie tablice rejestracyjne
            registrations_data = [
                ('DW', 'Wrocław'), ('KR', 'Kraków'), ('WA', 'Warszawa'),
                ('GD', 'Gdańsk'), ('PO', 'Poznań'), ('SZ', 'Szczecin'),
                ('LU', 'Lublin'), ('BI', 'Białystok'), ('KA', 'Katowice'),
                ('OP', 'Opole'), ('RZ', 'Rzeszów'), ('KI', 'Kielce'),
                ('TO', 'Toruń'), ('BY', 'Bydgoszcz'), ('ZG', 'Zielona Góra'),
                ('OL', 'Olsztyn'), ('LO', 'Łódź'), ('GS', 'Gorzów Wielkopolski'),
                ('RA', 'Radom'), ('CZ', 'Częstochowa'), ('SO', 'Sosnowiec'),
                ('TY', 'Tychy'), ('ZA', 'Zabrze'), ('GL', 'Gliwice'),
                ('RU', 'Ruda Śląska'), ('CH', 'Chorzów'), ('DA', 'Dąbrowa Górnicza'),
                ('JA', 'Jaworzno'), ('MY', 'Mysłowice'), ('SI', 'Siemianowice Śląskie')
            ]
            
            cursor.executemany('INSERT INTO registrations VALUES (?, ?)', registrations_data)
            self.conn.commit()
            print(f"Baza danych utworzona z {len(registrations_data)} rekordami.")
        else:
            # Sprawdź ile rekordów jest w istniejącej bazie
            cursor.execute('SELECT COUNT(*) FROM registrations')
            count = cursor.fetchone()[0]
            print(f"Używam istniejącej bazy danych z {count} rekordami.")
    
    def create_widgets(self):
        """Tworzenie elementów interfejsu"""
        # Główny kontener
        main_frame = ctk.CTkFrame(self.root, fg_color="#ffffff", corner_radius=15)
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Tytuł
        title_label = ctk.CTkLabel(
            main_frame,
            text="🚗 Quiz Tablic Rejestracyjnych",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#1e3a8a"
        )
        title_label.pack(pady=(20, 10))
        
        # Ustawienia quizu
        settings_frame = ctk.CTkFrame(main_frame, fg_color="#eff6ff", corner_radius=10)
        settings_frame.pack(fill="x", padx=20, pady=10)
        
        settings_label = ctk.CTkLabel(
            settings_frame,
            text="Ustawienia:",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#1e40af"
        )
        settings_label.pack(pady=(10, 5))
        
        # Slider dla liczby nieprawidłowych odpowiedzi
        slider_frame = ctk.CTkFrame(settings_frame, fg_color="transparent")
        slider_frame.pack(pady=(0, 10))
        
        slider_label = ctk.CTkLabel(
            slider_frame,
            text="Liczba nieprawidłowych odpowiedzi:",
            font=ctk.CTkFont(size=14),
            text_color="#1e40af"
        )
        slider_label.pack(side="left", padx=(10, 5))
        
        self.wrong_answers_slider = ctk.CTkSlider(
            slider_frame,
            from_=1,
            to=8,
            number_of_steps=7,
            command=self.update_wrong_answers_count,
            button_color="#2563eb",
            progress_color="#3b82f6"
        )
        self.wrong_answers_slider.set(3)
        self.wrong_answers_slider.pack(side="left", padx=5)
        
        self.wrong_answers_label = ctk.CTkLabel(
            slider_frame,
            text="3",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color="#1e40af"
        )
        self.wrong_answers_label.pack(side="left", padx=(5, 10))
        
        # Obszar pytania
        self.question_frame = ctk.CTkFrame(main_frame, fg_color="#f8fafc", corner_radius=10)
        self.question_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Wyświetlacz kodu rejestracyjnego
        self.question_label = ctk.CTkLabel(
            self.question_frame,
            text="Kliknij 'Nowe Pytanie' aby rozpocząć",
            font=ctk.CTkFont(size=48, weight="bold"),
            text_color="#1e3a8a",
            fg_color="#ffffff",
            corner_radius=10,
            width=200,
            height=100
        )
        self.question_label.pack(pady=30)
        
        # Kontener na odpowiedzi
        self.answers_frame = ctk.CTkFrame(self.question_frame, fg_color="transparent")
        self.answers_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Przyciski kontroli
        buttons_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        buttons_frame.pack(fill="x", padx=20, pady=(10, 20))
        
        self.new_question_btn = ctk.CTkButton(
            buttons_frame,
            text="Nowe Pytanie",
            command=self.generate_question,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#2563eb",
            hover_color="#1d4ed8",
            height=40,
            width=150
        )
        self.new_question_btn.pack(side="left", padx=(0, 10))
        
        self.check_btn = ctk.CTkButton(
            buttons_frame,
            text="Sprawdź",
            command=self.check_answer,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#16a34a",
            hover_color="#15803d",
            height=40,
            width=120,
            state="disabled"
        )
        self.check_btn.pack(side="left", padx=5)
        
        self.next_btn = ctk.CTkButton(
            buttons_frame,
            text="Dalej",
            command=self.next_question,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color="#dc2626",
            hover_color="#b91c1c",
            height=40,
            width=120,
            state="disabled"
        )
        self.next_btn.pack(side="left", padx=(5, 0))
        
        # Status
        self.status_label = ctk.CTkLabel(
            buttons_frame,
            text="Gotowy do rozpoczęcia",
            font=ctk.CTkFont(size=14),
            text_color="#6b7280"
        )
        self.status_label.pack(side="right", padx=20)
    
    def update_wrong_answers_count(self, value):
        """Aktualizacja liczby nieprawidłowych odpowiedzi"""
        self.wrong_answers_count = int(value)
        self.wrong_answers_label.configure(text=str(self.wrong_answers_count))
    
    def get_all_registrations(self):
        """Pobieranie wszystkich danych z bazy"""
        cursor = self.conn.cursor()
        cursor.execute('SELECT code, city FROM registrations')
        return cursor.fetchall()
    
    def generate_question(self):
        """Generowanie nowego pytania"""
        try:
            registrations = self.get_all_registrations()
            
            if len(registrations) < self.wrong_answers_count + 1:
                messagebox.showerror("Błąd", "Za mało danych w bazie dla wybranej liczby odpowiedzi!")
                return
            
            # Losowanie poprawnej odpowiedzi
            correct_reg = random.choice(registrations)
            self.current_question = correct_reg[0]
            self.correct_answer = correct_reg[1]
            
            # Generowanie nieprawidłowych odpowiedzi
            wrong_options = [reg for reg in registrations if reg != correct_reg]
            wrong_answers = random.sample(wrong_options, self.wrong_answers_count)
            
            # Wszystkie opcje odpowiedzi
            all_answers = [correct_reg[1]] + [reg[1] for reg in wrong_answers]
            random.shuffle(all_answers)
            
            # Aktualizacja interfejsu
            self.question_label.configure(text=self.current_question)
            self.create_answer_buttons(all_answers)
            
            # Aktualizacja przycisków
            self.check_btn.configure(state="normal")
            self.next_btn.configure(state="disabled")
            self.question_answered = False
            
            # Aktualizacja statusu
            total_answers = self.wrong_answers_count + 1
            self.status_label.configure(text=f"Pytanie: {self.current_question} | Odpowiedzi: {total_answers}")
            
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił błąd podczas generowania pytania: {str(e)}")
    
    def create_answer_buttons(self, answers):
        """Tworzenie przycisków odpowiedzi"""
        # Czyszczenie starych przycisków
        for widget in self.answers_frame.winfo_children():
            widget.destroy()
        
        self.answer_buttons = []
        self.selected_answer = tk.StringVar()
        
        # Obliczanie układu przycisków
        total_answers = len(answers)
        cols = min(3, total_answers)
        rows = (total_answers + cols - 1) // cols
        
        for i, answer in enumerate(answers):
            row = i // cols
            col = i % cols
            
            # Frame dla każdego przycisku (dla obwódki)
            button_frame = ctk.CTkFrame(
                self.answers_frame,
                fg_color="#ffffff",
                border_color="#000000",
                border_width=2,
                corner_radius=8
            )
            button_frame.grid(row=row, col=col, padx=10, pady=10, sticky="ew")
            
            # Radiobutton
            radio_btn = ctk.CTkRadioButton(
                button_frame,
                text=answer,
                variable=self.selected_answer,
                value=answer,
                font=ctk.CTkFont(size=14),
                text_color="#000000",
                fg_color="#2563eb",
                hover_color="#eff6ff"
            )
            radio_btn.pack(pady=15, padx=20)
            
            self.answer_buttons.append((button_frame, radio_btn, answer))
        
        # Konfiguracja grid
        for i in range(cols):
            self.answers_frame.grid_columnconfigure(i, weight=1)
    
    def check_answer(self):
        """Sprawdzanie odpowiedzi"""
        if not self.selected_answer.get():
            messagebox.showwarning("Uwaga", "Proszę wybrać odpowiedź!")
            return
        
        self.question_answered = True
        
        # Kolorowanie odpowiedzi
        for frame, radio, answer in self.answer_buttons:
            if answer == self.correct_answer:
                # Poprawna odpowiedź - zielona
                frame.configure(fg_color="#22c55e", border_color="#16a34a")
                radio.configure(text_color="#ffffff")
            else:
                # Niepoprawna odpowiedź - czerwona
                frame.configure(fg_color="#ef4444", border_color="#dc2626")
                radio.configure(text_color="#ffffff")
        
        # Aktualizacja przycisków
        self.check_btn.configure(state="disabled")
        self.next_btn.configure(state="normal")
        
        # Sprawdzenie czy odpowiedź była poprawna
        if self.selected_answer.get() == self.correct_answer:
            self.status_label.configure(text="✅ Poprawna odpowiedź!", text_color="#16a34a")
        else:
            self.status_label.configure(
                text=f"❌ Niepoprawna! Prawidłowa odpowiedź: {self.correct_answer}",
                text_color="#dc2626"
            )
    
    def next_question(self):
        """Przejście do następnego pytania"""
        self.generate_question()
        self.status_label.configure(text_color="#6b7280")
    
    def run(self):
        """Uruchomienie aplikacji"""
        self.root.mainloop()
    
    def __del__(self):
        """Cleanup - zamknięcie połączenia z bazą danych"""
        if hasattr(self, 'conn'):
            self.conn.close()

# Uruchomienie aplikacji
if __name__ == "__main__":
    app = RegistrationQuiz()
    app.run()
