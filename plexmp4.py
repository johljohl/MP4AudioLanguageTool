import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import threading

# En enkel mappning mellan språk och deras ISO 639-2 koder
languages = {
    "Japanese": "jpn",
    "English": "eng",
    "French": "fra",
    "Spanish": "spa",
    "German": "ger",
    "Swedish": "swe",
    "Italian": "it",
    # Lägg till fler språk och koder här
}

def set_audio_language(file_path, language_code, mp4box_path="C:\\Program Files\\GPAC\\MP4Box.exe"):
    if file_path.endswith('.mp4'):
        try:
            command = f'"{mp4box_path}" -lang {language_code} "{file_path}"'
            subprocess.run(command, shell=True)
            messagebox.showinfo("Success", "Språket har ändrats.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Filen är inte en MP4-fil.")
    progress_bar.stop()
    progress_frame.pack_forget()

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(0, file_path)

def perform_action():
    file_path = entry_file_path.get()
    language = combo_language.get()
    language_code = languages.get(language, "und")  # 'und' är ISO 639-2 koden för 'undefined'
    progress_frame.pack()  # Show the progress frame
    progress_bar.start(10)  # Start the indeterminant progress bar
    threading.Thread(target=set_audio_language, args=(file_path, language_code), daemon=True).start()

# Skapa huvudfönstret
root = tk.Tk()
root.title("MP4 Ljudspår Språkändrare")

# Lägg till en etikett för filväg
label_file_path = tk.Label(root, text="MP4-filens sökväg:")
label_file_path.pack()

# Lägg till en textinmatning för filvägen
entry_file_path = tk.Entry(root, width=50)
entry_file_path.pack()

# Lägg till en knapp för att öppna filvalsdialogen
button_browse = tk.Button(root, text="Bläddra", command=open_file_dialog)
button_browse.pack()

# Lägg till en etikett för språkval
label_language = tk.Label(root, text="Välj språk:")
label_language.pack()

# Lägg till en rullgardinsmeny för språkval
combo_language = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
combo_language.pack()

# Lägg till en progressbar i en ram
progress_frame = tk.Frame(root)
progress_bar = ttk.Progressbar(progress_frame, orient="horizontal", mode="indeterminate", length=200)
progress_bar.pack()

# Lägg till en knapp för att utföra ändringen
button_change_language = tk.Button(root, text="Ändra Språk", command=perform_action)
button_change_language.pack()

# Starta GUI-loopen
root.mainloop()
