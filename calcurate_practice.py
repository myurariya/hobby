import os, sys, time
import tkinter as tk
import tkinter.ttk as ttk
import random
from functools import partial

root = tk.Tk()
root.title("計算練習")
root.geometry("1024x720")


combo = ttk.Combobox(root,state="readonly")
combo["values"] = ["たしざん","ひきざん","かけざん","わりざん"]
combo.current(0)
combo.pack()
num1 = random.randrange(0,9)
num2 = random.randrange(0,9)
symbol = "×"
ans = "答え"

problem = tk.Label(root,text="{} {} {}".format(num1,symbol,num2),font=("源暎ゴシックP SemiBold",100))
def reroad(nproblem):
    nproblem.destroy()
    n_num1 = random.randrange(0,9)
    n_num2 = random.randrange(0,9)
    nproblem = tk.Label(root,text="{} {} {}".format(n_num1,symbol,n_num2),font=("源暎ゴシックP SemiBold",100))
    nproblem.pack()
    print(n_num1)

problem.pack()
button = ttk.Button(root,text="答え合わせと採点",command = partial(reroad,problem))
button.pack()
answer = tk.Label(root,text="{}".format(ans),font=("源暎ゴシックP SemiBold",100))
answer.pack()


root.mainloop()