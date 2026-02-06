"""
💖 DIMMER LED - С МИЛЫМИ ФОТОЧКАМИ! 💖
Управляй светом как принцесса с магической палочкой!
"""

import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # Библиотека для красивых картинок
import os
import time

# 🎀 ФУНКЦИИ-ПОМОЩНИЦЫ 🎀
def blueLED():
    """
    Включает синюю лампочку (в воображении)
    Кнопка временно 'засыпает' 💤
    """
    try:
        # Берем время и яркость
        delay = float(entry_time.get())
        brightness = slider_brightness.get()
        
        # Делаем кнопку серенькой (она спит)
        btn_blue.config(state=tk.DISABLED, bg='#f0f0f0')
        
        # Показываем анимацию
        label_status.config(text=f"💙 Синий свет горит {delay} сек...", fg='#3498db')
        
        # Обновляем окошко
        win.update()
        
        # Ждем... (можно представить, что лампочка горит)
        win.after(int(delay * 1000), lambda: finish_blue())
        
    except ValueError:
        messagebox.showerror("Ой! 😅", "Введи число в поле времени!\nНапример: 2.5 или 3")

def finish_blue():
    """Заканчиваем магию с синим светом"""
    btn_blue.config(state=tk.NORMAL, bg='#3498db')
    label_status.config(text="✨ Готово! Можно нажимать снова", fg='#2ecc71')

def redLED():
    """
    Включает красную лампочку (очень романтично)
    """
    try:
        delay = float(entry_time.get())
        brightness = slider_brightness.get()
        
        btn_red.config(state=tk.DISABLED, bg='#f0f0f0')
        label_status.config(text=f"❤️ Красный свет горит {delay} сек...", fg='#e74c3c')
        win.update()
        
        win.after(int(delay * 1000), lambda: finish_red())
        
    except ValueError:
        messagebox.showerror("Ой! 😅", "Введи число в поле времени!\nНапример: 2.5 или 3")

def finish_red():
    """Заканчиваем магию с красным светом"""
    btn_red.config(state=tk.NORMAL, bg='#e74c3c')
    label_status.config(text="✨ Готово! Можно нажимать снова", fg='#2ecc71')

def show_about():
    """
    Показываем милое окошко 'О программе'
    С сердечками и комплиментами! 💕
    """
    about_text = """🎀 LED Fairy Controller v1.0 🎀

✨ Программа для управления светом ✨

Сделано с любовью для самых красивых пользовательниц!

Функции:
💙 Синий свет - для спокойствия
❤️ Красный свет - для романтики
✨ Регулировка яркости - как в фильтрах
⏰ Таймер - чтобы не забыть выключить

Автор: Волшебница-программистка 💻

P.S. Ты сегодня выглядишь прекрасно! 😊"""
    
    messagebox.showinfo("💝 О программе", about_text)

def exit_program():
    """
    Выходим из программы красиво
    С прощальным сообщением 💌
    """
    if messagebox.askyesno("До свидания! 👋", "Точно хочешь выйти?\nМы будем скучать!"):
        win.destroy()

# 🎀 СОЗДАЕМ ГЛАВНОЕ ОКОШКО 🎀
win = tk.Tk()
win.title("🎀 LED Fairy Controller 🎀")
win.geometry("500x500")
win.configure(bg='#ffe6f2')  # Розовый фон как у принцессы

# Стиль для красивых кнопочек
style = ttk.Style()
style.theme_use('clam')

# 🎀 ЗАГОЛОВОК С СЕРДЕЧКАМИ 🎀
frame_header = tk.Frame(win, bg='#ffccdd', height=80)
frame_header.pack(fill='x', padx=10, pady=10)

label_title = tk.Label(frame_header, 
                      text="✨ LED Fairy Controller ✨",
                      font=('Comic Sans MS', 20, 'bold'),
                      bg='#ffccdd',
                      fg='#ff3366')
label_title.pack(pady=20)

# 🎀 ОСНОВНОЙ БЛОК С НАСТРОЙКАМИ 🎀
frame_main = tk.Frame(win, bg='#ffe6f2')
frame_main.pack(pady=20)

# ⏰ ВРЕМЯ ГОРЕНИЯ
frame_time = tk.Frame(frame_main, bg='#ffe6f2')
frame_time.pack(pady=10)

label_time = tk.Label(frame_time, 
                     text="⏰ Время (секунды):",
                     font=('Arial', 12),
                     bg='#ffe6f2',
                     fg='#333333')
label_time.pack(side='left', padx=(0, 10))

entry_time = tk.Entry(frame_time,
                     font=('Arial', 12),
                     width=10,
                     bd=3,
                     relief='solid',
                     bg='white')
entry_time.pack(side='left')
entry_time.insert(0, "3")  # Стандартное значение

# ✨ ЯРКОСТЬ
frame_brightness = tk.Frame(frame_main, bg='#ffe6f2')
frame_brightness.pack(pady=15)

label_brightness = tk.Label(frame_brightness,
                           text="✨ Яркость:",
                           font=('Arial', 12),
                           bg='#ffe6f2',
                           fg='#333333')
label_brightness.pack()

slider_brightness = tk.Scale(frame_brightness,
                            from_=0,
                            to=100,
                            orient='horizontal',
                            length=300,
                            sliderlength=30,
                            bg='#ffccdd',
                            troughcolor='white',
                            highlightbackground='#ffe6f2',
                            font=('Arial', 10))
slider_brightness.pack(pady=5)
slider_brightness.set(50)  # Средняя яркость

# 🎀 КНОПОЧКИ ЛАМПОЧЕК 🎀
frame_buttons = tk.Frame(frame_main, bg='#ffe6f2')
frame_buttons.pack(pady=20)

# Синяя кнопка
btn_blue = tk.Button(frame_buttons,
                    text="💙 Blue LED",
                    font=('Arial', 14, 'bold'),
                    bg='#3498db',
                    fg='white',
                    activebackground='#2980b9',
                    width=12,
                    height=2,
                    command=blueLED,
                    bd=0,
                    relief='raised',
                    cursor='hand2')
btn_blue.pack(side='left', padx=10)

# Красная кнопка
btn_red = tk.Button(frame_buttons,
                   text="❤️ Red LED",
                   font=('Arial', 14, 'bold'),
                   bg='#e74c3c',
                   fg='white',
                   activebackground='#c0392b',
                   width=12,
                   height=2,
                   command=redLED,
                   bd=0,
                   relief='raised',
                   cursor='hand2')
btn_red.pack(side='left', padx=10)

# 🎀 СТРОКА СТАТУСА 🎀
label_status = tk.Label(win,
                       text="✨ Выбери настройки и нажми кнопку!",
                       font=('Arial', 11),
                       bg='#ffe6f2',
                       fg='#2ecc71')
label_status.pack(pady=10)

# 🎀 НИЖНИЕ КНОПОЧКИ 🎀
frame_bottom = tk.Frame(win, bg='#ffe6f2')
frame_bottom.pack(pady=20)

# Кнопка "Справка"
btn_about = tk.Button(frame_bottom,
                     text="💝 Справка",
                     font=('Arial', 11),
                     bg='#9b59b6',
                     fg='white',
                     width=10,
                     height=1,
                     command=show_about,
                     cursor='heart')
btn_about.pack(side='left', padx=20)

# Кнопка "Выход"
btn_exit = tk.Button(frame_bottom,
                    text="👋 Выход",
                    font=('Arial', 11),
                    bg='#e67e22',
                    fg='white',
                    width=10,
                    height=1,
                    command=exit_program,
                    cursor='pirate')
btn_exit.pack(side='left', padx=20)

# 🎀 ПОДВАЛ С АВТОРСКИМИ ПРАВАМИ 🎀
label_footer = tk.Label(win,
                       text="Сделано с 💖 для самых милых пользовательниц | 2024",
                       font=('Arial', 9),
                       bg='#ffe6f2',
                       fg='#999999')
label_footer.pack(side='bottom', pady=10)

# 🎀 ЗАПУСКАЕМ ВОЛШЕБСТВО! 🎀
win.mainloop()
