import requests
import tkinter as tk
from tkinter import filedialog as fd
import PyPDF2
import os

screen = tk.Tk()
screen.config(pady=20, padx=20)

URL = "https://api.voicerss.org/"
API = os.environ.get("api")


def pdf():
    filetypes = (
            ('pdf', '.pdf'),
        )
    filename = fd.askopenfilename(title="Open PDF",
                                  initialdir="/",
                                  filetypes=filetypes)
    if filename:
        file = open(filename, "rb")
        read = PyPDF2.PdfReader(file)
        pages = read.pages
        for page in pages:
            text = page.extract_text()
            speech(text)
        done = tk.Label(screen, text="Done! your mp3 is in mp3 folder.", fg="green")
        done.grid(column=1, row=2)


def speech(text):
    parameters = {
        "key": API,
        "src": text,
        "hl": "en-us",
        "v": "Amy",
        "c": "MP3",
        "f": "16khz_16bit_stereo"

    }
    response = requests.get(url=URL, params=parameters)
    response.raise_for_status()
    with open('mp3/text.mp3', "wb") as f:
        f.write(response.content)


button = tk.Button(screen, text="Take PDF", command=pdf)
button.grid(column=0, row=2)
write = tk.Label(text="Take PDF and it will save MP3 of your text")
write.grid(column=1, row=0)


if __name__ == "__main__":
    screen.mainloop()
