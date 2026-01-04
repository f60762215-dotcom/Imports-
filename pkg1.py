import time
import tkinter as tk

def create_page(name, size_x, size_y):
  e = tk.Tk()
  e.title(f"{name}")
  e.geometry(f"{size_x}x{size_y}")
  e.mainloop()
if __name__ == '__main__':
  print("wellcome to my pkg farzad")
  print("commands: create_page(name, size_x, size_y")
