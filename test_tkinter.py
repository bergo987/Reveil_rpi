from tkinter import *

#initialissation de la fenetre et de ses paramètres
fenetre = Tk()
fenetre.config(bg = "#87CEEB")
fenetre.geometry("640x480")

fenetre.maxsize(800,600)
fenetre.minsize(300,400)



# frame 1
Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=30, pady=30)

# frame 2
Frame2 = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame2.pack(side=LEFT, padx=10, pady=10)

# frame 3 dans frame 2
Frame3 = Frame(Frame2, bg="white", borderwidth=2, relief=GROOVE)
Frame3.pack(side=RIGHT, padx=5, pady=5)

# Ajout de labels
Label(Frame1, text="Frame 1").pack(padx=10, pady=10)
Label(Frame2, text="Frame 2").pack(padx=10, pady=10)
Label(Frame3, text="Frame 3",bg="white").pack(padx=10, pady=10)

champ_label = Label(fenetre, text="Salut à tous")
bouton_quitter = Button(Frame3,text="Quitter", command=fenetre.quit)

champ_label.pack()


var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()


var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()

# radiobutton
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peu être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()

# liste
liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")
liste.pack()

# canvas
canvas = Canvas(fenetre, width=150, height=120, background='yellow')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
canvas.pack()

#scale (fait de pouvoire recupérer une valeur chiffré grace a un scroll)
value = DoubleVar()
scale = Scale(fenetre, variable=value)
scale.pack()





bouton_quitter.pack()
fenetre.mainloop()