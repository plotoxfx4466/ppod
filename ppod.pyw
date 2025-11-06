import tkinter as tk
import random
import time

def make_popup(i):
    win = tk.Toplevel(root)
    win.title(f"github: plotoxfx4466{i+1}")
    win.geometry("300x120+{}+{}".format(random.randint(100,700), random.randint(100,500)))
    win.resizable(False, False)
    tk.Label(win, text="sıkıntı kardeşim ya", font=("Arial", 12)).pack(pady=10)


root = tk.Tk()
root.withdraw()
time.sleep(10 * 60)
for i in range(500):
    root.after(200*i, lambda i=i: make_popup(i))


root.mainloop()
