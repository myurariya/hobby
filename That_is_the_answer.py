# coding: utf-8

import os, sys, time
import tkinter as tk
import random

root = tk.Tk()
root.title("That is the answer!")
root.geometry("1024x720")

letters_default = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","て","と","な","の","は","ひ","ふ"\
    ,"へ","ほ","よ","ろ","り","じ"]
letters = letters_default
init = letters[random.randrange(len(letters))]
theme_list = ["赤いもの","四角いもの","青いもの","黄色いもの","緑色のもの","黒いもの","白いもの","あたたまるもの","読みたいもの","子供が好きなもの",\
    "お年寄りが好きなもの","若者らしいもの","憧れるもの","疲れること","癒されるもの","重いもの","嬉しいこと","盛り上がること","体に悪いこと","おしゃれなもの",\
    "面白い人","こわいもの","傑作","一目置いてもらえること","大切にしたいもの","丸いもの","大きいもの","小さいもの","冷たいもの","高いもの",\
    "お買い得なもの","便利なもの","びっくりすること","一人暮らしに便利なもの","カッコいいもの","流行っているもの","若いうちにやっておくべきこと","頭を使うこと",\
    "難しいこと","はやいもの","多くの人が好きなもの","大変なこと","広いもの","学びたいこと","センスのいい趣味","甘いもの","からいもの","短いもの",\
    "長いもの","古典的なもの","公共のもの","毎日やりたいこと","多いもの","健康的なこと","上品なもの","懐かしいもの","好みが分かれるもの","面倒なこと",\
    "重いもの","軽いもの","かわいいもの","感動すること","スッキリすること","頭のいい人","大人っぽいもの","意識が高いこと","痛いこと","親切なこと",\
    "気をつけたいこと","されたら嫌なこと","言ってみたいセリフ","もらって嬉しいもの","できたらカッコいいこと"]

theme_similar = [["赤いもの","青いもの","黄色いもの","緑色のもの","黒いもの","白いもの"],["あたたまるもの","つめたいもの"],["子供が好きなもの",\
    "お年寄りが好きなもの","若者らしいもの","大人っぽいもの"],["疲れること","癒されるもの"],["丸いもの","四角いもの"],["大きいもの","小さいもの"],["甘いもの","からいもの"],\
        ["一人暮らしに便利なもの","便利なもの"],["短いもの","長いもの"],["読みたいもの","傑作"],["古典的なもの","流行っているもの"],["重いもの","軽いもの"],\
        ["体に悪いこと","健康的なこと"]]

theme = theme_list[random.randrange(len(theme_list))]
# txt_1 = tk.Entry()
label_1 = tk.Label(root,text="それ正解！バー",font=("源暎ゴシックP SemiBold",100))
label_2 = tk.Label(root,text="一日店長：竹下りや",font=("源暎ゴシックP SemiBold",100))
label_dummy = tk.Label(root,text="",font=("",250))
count = 0
counter = tk.Label(root,text="はじまるよ",font=("游明朝",40))
def pushed():
    global count
    if count >= 1:
        global theme
        for i in theme_similar:
            if theme in i:
                for j in i:
                    try:
                        theme_list.remove(j)
                    except:
                        pass
                    # print(j)
        try:
            theme_list.remove(theme)
        except:
            pass
        global init
        global letters
        letters.remove(init)
    count += 1
    global label_1
    label_1.destroy()
    global label_2
    label_2.destroy()
    if len(letters) == 0:
        letters = letters_default
    init = letters[random.randrange(len(letters))]
    theme = theme_list[random.randrange(len(theme_list))]
    label_1 = tk.Label(root, text="「{}」で始まる".format(init),font=("源暎ゴシックP SemiBold",100),anchor="center")
    label_2 = tk.Label(root, text="{}は？".format(theme),font=("源暎ゴシックP SemiBold",100),anchor="center")
    counter = tk.Label(root,text="いま{}個目のお題".format(count),font=("游明朝",40))
    # label_dummy = tk.Label(root)
    # label_dummy = tk.Label(root)
    # label_dummy.pack(expand=0,fill="none",anchor="center")
    label_1.pack(expand=0,fill="none",anchor="center")
    label_2.pack(expand=0,fill="none",anchor="center")
    counter.place(relx=0.1,rely=0.9)
    # print(theme)
    # print(theme_list)

button = tk.Button(root, text="次のお題",command=pushed)
# txt_1.insert(tk.END,"{}で始まる".format(init))
# label_1 = tk.Label(root, text="{}で始まる".format(init),font=("",150))
# label_2 = tk.Label(root, text="{}は？".format(theme),font=("",50))
label_dummy.pack(expand=0,fill="both",anchor="center")
label_1.pack(expand=0,fill="both",anchor="center")
label_2.pack(expand=0,fill="both",anchor="center")
label_dummy.pack(expand=0,fill="both",anchor="center")
# txt_1.pack()
button.place(relx=0.9,rely=0.9)
counter.place(relx=0.1,rely=0.9)

root.mainloop()
