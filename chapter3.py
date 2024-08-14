import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import pygame

# Inisialisasi pygame mixer
pygame.mixer.init()

# Fungsi untuk memutar musik
def play_music(file_path='yo.wav'):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Error playing audio: {e}")

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Memuat gambar menggunakan Pillow dan mengubah ukurannya
image = Image.open('wan.jpg')
image = image.resize((400, 400))  # Ubah ukuran gambar sesuai kebutuhan
photo = ImageTk.PhotoImage(image)

# Membuat label untuk menampilkan gambar
label = tk.Label(root, image=photo)
label.pack()

# Membuat tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=lambda: play_music('aliyah.mp3'))
play_button.pack(side=tk.BOTTOM, pady=10)  # Menempatkan tombol di bawah gambar dengan padding

# Menjalankan loop acara Tkinter
root.mainloop()
