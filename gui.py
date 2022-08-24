import tkinter as tk
from tkinter import Label, filedialog
import main

window = tk.Tk()
window.title('CC & Haltstead Metrics')
window.geometry("800x650")
window.config(background = "white")

def browsefunc():
    filename =filedialog.askopenfilename(filetypes=(("c files","*.c"),("All files","*.*")))
    entryBox.insert(tk.END, filename) # add this
    filepath = entryBox.get()
    a = main.manageFile(filepath)

    codeBox = tk.Text(window, width=35, height=18, font=("Arial", 14))
    codeBox.place(x=50, y=200)
    codeBox.insert(tk.INSERT, a['codeBox'])

    cyclo = tk.Label(window, text=a['ccCount'], font=("Arial", 13), bg="#FFFFFF")
    cyclo.place(x=640, y=210)

    smallN1 = tk.Label(window, text=a['n1'], font=("Arial", 12), bg="#FFFFFF")
    smallN1.place(x=480, y=240)

    captialN1 = tk.Label(window, text=a['N1'], font=("Arial", 12), bg="#FFFFFF")
    captialN1.place(x=480, y=270)

    smallN2 = tk.Label(window, text=a['n2'], font=("Arial", 12), bg="#FFFFFF")
    smallN2.place(x=480, y=300)

    captialN2 = tk.Label(window, text=a['N2'], font=("Arial", 12), bg="#FFFFFF")
    captialN2.place(x=480, y=330)

    progLength = tk.Label(window, text=a['progLength'], font=("Arial", 12), bg="#FFFFFF")
    progLength.place(x=583, y=360)

    progVocab = tk.Label(window, text=a['progVocab'], font=("Arial", 12), bg="#FFFFFF")
    progVocab.place(x=580, y=390)

    estimatedLength = tk.Label(window, text=a['estimatedLength'], font=("Arial", 12), bg="#FFFFFF")
    estimatedLength.place(x=595, y=420)

    purityRatio = tk.Label(window, text=a['purityRatio'], font=("Arial", 12), bg="#FFFFFF")
    purityRatio.place(x=550, y=450)

    volume = tk.Label(window, text=a['volume'], font=("Arial", 12), bg="#FFFFFF")
    volume.place(x=518, y=480)

    difficulty = tk.Label(window, text=a['difficulty'], font=("Arial", 12), bg="#FFFFFF")
    difficulty.place(x=527, y=510)

    progEffort = tk.Label(window, text=a['progEffort'], font=("Arial", 12), bg="#FFFFFF")
    progEffort.place(x=573, y=540)

    progTime = tk.Label(window, text=a['progTime'], font=("Arial", 12), bg="#FFFFFF")
    progTime.place(x=567, y=570)

    deliveredBug = tk.Label(window, text=a['deliveredBug'], font=("Arial", 12), bg="#FFFFFF")
    deliveredBug.place(x=580, y=600)


label = tk.Label(window, text="CC & Haltstead Metrics", font=("Arial Bold", 20), bg="#FFD6EA")
label.place(x=250, y=20)

entryLabel = tk.Label(window, text="File Path Entry", font=("Arial black", 18), bg="#FFD6EA")
entryLabel.place(x=50, y=70)

entryBox = tk.Entry(window, width=41, bd=5, font=("Arial", 16))
entryBox.place(x=50, y=110)

codeLabel = tk.Label(window, text="Code Preveiw", font=("Arial black", 18), bg="#FFD6EA")
codeLabel.place(x=50, y=160)

resultLabel = tk.Label(window, text="Results", font=("Arial black", 18), bg="#FFD6EA")
resultLabel.place(x=450, y=160)

cyclo = tk.Label(window, text="Cyclomatic Complexity:", font=("Arial Bold", 13), bg="#FFFFFF")
cyclo.place(x=450, y=210)

smallN1 = tk.Label(window, text="n1:", font=("Arial Bold", 12), bg="#FFFFFF")
smallN1.place(x=450, y=240)

captialN1 = tk.Label(window, text="N1:", font=("Arial Bold", 12), bg="#FFFFFF")
captialN1.place(x=450, y=270)

smallN2 = tk.Label(window, text="n2:", font=("Arial Bold", 12), bg="#FFFFFF")
smallN2.place(x=450, y=300)

captialN2 = tk.Label(window, text="N2:", font=("Arial Bold", 12), bg="#FFFFFF")
captialN2.place(x=450, y=330)

progLength = tk.Label(window, text="Program Length:", font=("Arial Bold", 12), bg="#FFFFFF")
progLength.place(x=450, y=360)

progVocab = tk.Label(window, text="Program Vocab:", font=("Arial Bold", 12), bg="#FFFFFF")
progVocab.place(x=450, y=390)

estimatedLength = tk.Label(window, text="Estimated Length:", font=("Arial Bold", 12), bg="#FFFFFF")
estimatedLength.place(x=450, y=420)

purityRatio = tk.Label(window, text="Purity Ratio:", font=("Arial Bold", 12), bg="#FFFFFF")
purityRatio.place(x=450, y=450)

volume = tk.Label(window, text="Volume:", font=("Arial Bold", 12), bg="#FFFFFF")
volume.place(x=450, y=480)

difficulty = tk.Label(window, text="Difficulty:", font=("Arial Bold", 12), bg="#FFFFFF")
difficulty.place(x=450, y=510)

progEffort = tk.Label(window, text="Program Effort:", font=("Arial Bold", 12), bg="#FFFFFF")
progEffort.place(x=450, y=540)

progTime = tk.Label(window, text="Program Time:", font=("Arial Bold", 12), bg="#FFFFFF")
progTime.place(x=450, y=570)

deliveredBug = tk.Label(window, text="Delivered Bugs:", font=("Arial Bold", 12), bg="#FFFFFF")
deliveredBug.place(x=450, y=600)

pathButton = tk.Button(window, text="Select File Path", font=("Arial", 16), command=lambda: browsefunc(), bg="#FD3294")
pathButton.place(x=552, y=110)

window.mainloop()