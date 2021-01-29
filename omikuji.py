#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter as tk
import random

threeletters = []
with open("", mode="r") as f:
    threeletters = f.readlines()
threeletters = [i.strip("\n") for i in threeletters]


def displayLabel():
    wordlist = []
    omikuji = ""
    for i in range(30):
        ind = random.randint(0, 199-i)
        wordlist.append(threeletters[ind])
        threeletters.remove(threeletters[ind])
    for i in range(10):
        omikuji += "{}   {}   {}\n".format(
            wordlist[0+3*i], wordlist[1+3*i], wordlist[2+3*i])
    # omikuji = ["大吉", "中吉", "小吉", "吉", "凶", "大凶"]
    label.configure(text=omikuji, font=("游明朝 Demibold", 30))


root = tk.Tk()
root.geometry("600x900")
label = tk.Label(text="おみくじボタンを押してね", font=("游明朝 Demibold", 30))
button = tk.Button(text="おみくじを引く", font=(
    "游明朝 Demibold", 30), command=displayLabel)
label.pack()
button.pack()
tk.mainloop()
