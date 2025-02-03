import tkinter as tk
import random

class RandomNumberGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("QRX-generator ALPHA V0.1")
        self.root.configure(bg='lightblue')
        self.button = tk.Button(self.root, text="Generate", command=self.toggle_generation)
        self.button.pack(pady=20)
        self.output = tk.Text(self.root, height=10, width=40, bg='white', wrap='word')
        self.output.pack(pady=10)
        self.generating = False
    def toggle_generation(self):
        self.generating = not self.generating
        if self.generating:
            self.button.config(text="Stop")
            self.generate_number()
        else:
            self.button.config(text="Generate")
    def generate_number(self):
        if self.generating:
            number = random.randint(0, 204800000)
            self.output.insert(tk.END, f"{number}\n")
            self.root.after(100, self.generate_number)

if __name__ == "__QRXgenerateV0.1__":
    root = tk.Tk()
    app = RandomNumberGenerator(root)
    root.mainloop()