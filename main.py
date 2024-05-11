# -*- coding: utf-8 -*-
"""
Created on Sat May 11 12:15:53 2024

@author: user
"""

import tkinter as tk
import requests

def fetch_content():
    site_url = url_entry.get()
    try:
        response = requests.get(site_url)
        headers_text.delete("1.0", tk.END)
        #headers_text.insert(tk.END, str(response.headers))
        zagolovkiDict = response.headers
        textZgolovki = ''
        for item in zagolovkiDict:
            try:
                textZgolovki = f'{textZgolovki}\n{item}: {zagolovkiDict[item]}'
            except:
                textZgolovki = f'{item}: {zagolovkiDict[item]}'
        headers_text.insert(tk.END, textZgolovki)
        content_text.delete("1.0", tk.END)
        content_text.insert(tk.END, response.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка получения контента: {e}")

root = tk.Tk()
root.title("HTTP-Response Inspector - alekseycheremnykh.ru (GNU GPL v2)")

url_label = tk.Label(root, text="Адрес сайта:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

fetch_button = tk.Button(root, text="Получить", command=fetch_content)
fetch_button.pack()

headers_label = tk.Label(root, text="Заголовки:")
headers_label.pack()
headers_text = tk.Text(root)
headers_text.pack()

content_label = tk.Label(root, text="Код страницы:")
content_label.pack()
content_text = tk.Text(root)
content_text.pack()

root.mainloop()