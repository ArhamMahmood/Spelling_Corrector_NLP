import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from spelling_corrector import SpellingCorrector

corrector = SpellingCorrector()

is_dark_mode = False

def correct_text():
    input_text = input_box.get("1.0", tk.END)
    corrected = corrector.correct_text(input_text)
    output_box.config(state='normal')
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, corrected)
    output_box.config(state='disabled')

def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(output_box.get("1.0", tk.END))
        tk.messagebox.showinfo("Saved", f"File saved to {file_path}")

def toggle_dark_mode():
    global is_dark_mode
    if is_dark_mode:
        apply_light_mode()
    else:
        apply_dark_mode()
    is_dark_mode = not is_dark_mode

def apply_light_mode():
    root.config(bg="#fdfdfd")
    title_label.config(bg="#fdfdfd", fg="#1e1e1e")
    footer_label.config(bg="#fdfdfd", fg="gray")
    input_frame.config(style="Custom.TFrame")
    output_frame.config(style="Custom.TFrame")
    dark_button.config(text="🌙 Dark Mode")

def apply_dark_mode():
    root.config(bg="#2b2b2b")
    title_label.config(bg="#2b2b2b", fg="#ffffff")
    footer_label.config(bg="#2b2b2b", fg="lightgray")
    input_frame.config(style="Dark.TFrame")
    output_frame.config(style="Dark.TFrame")
    dark_button.config(text="☀️ Light Mode")

root = tk.Tk()
root.title("📝 Spelling Corrector")
root.geometry("700x550")
root.resizable(False, False)

### ✅ custom background color
root.config(bg="#f0f4f8")  # a cool soft blue-gray background

# Style for rounded buttons
style = ttk.Style()
style.theme_use('clam')
style.configure("Rounded.TButton",
                font=("Helvetica", 11),
                padding=10,
                relief="flat",
                borderwidth=0,
                background="#4A90E2",
                foreground="white")
style.map("Rounded.TButton",
          background=[('active', '#357ABD')],
          relief=[('pressed', 'sunken')])

style.configure("Custom.TFrame", background="#f0f4f8")
style.configure("Dark.TFrame", background="#2b2b2b")

# Title
title_label = tk.Label(root, text="Spelling Corrector", font=("Helvetica", 20, "bold"), bg="#f0f4f8", fg="#1e1e1e")
title_label.pack(pady=10)

input_frame = ttk.Frame(root, style="Custom.TFrame")
input_frame.pack(padx=20, pady=10, fill='x')

input_label = tk.Label(input_frame, text="Enter text:", font=("Helvetica", 12), bg="#f0f4f8")
input_label.pack(anchor='w')

input_box = scrolledtext.ScrolledText(input_frame, height=8, font=("Courier", 11))
input_box.pack(fill='x')

button_frame = ttk.Frame(root, style="Custom.TFrame")
button_frame.pack(pady=15)

correct_button = ttk.Button(button_frame, text="✔ Correct Spelling", command=correct_text, style="Rounded.TButton")
correct_button.grid(row=0, column=0, padx=8)

save_button = ttk.Button(button_frame, text="💾 Save to File", command=save_to_file, style="Rounded.TButton")
save_button.grid(row=0, column=1, padx=8)

dark_button = ttk.Button(button_frame, text="🌙 Dark Mode", command=toggle_dark_mode, style="Rounded.TButton")
dark_button.grid(row=0, column=2, padx=8)

output_frame = ttk.Frame(root, style="Custom.TFrame")
output_frame.pack(padx=20, pady=10, fill='x')

output_label = tk.Label(output_frame, text="Corrected text:", font=("Helvetica", 12), bg="#f0f4f8")
output_label.pack(anchor='w')

output_box = scrolledtext.ScrolledText(output_frame, height=8, font=("Courier", 11), state='disabled')
output_box.pack(fill='x')

footer_label = tk.Label(root, text="Created by Your Name", font=("Helvetica", 9), fg="gray", bg="#f0f4f8")
footer_label.pack(side='bottom', pady=5)

root.mainloop()