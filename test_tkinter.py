from tkinter import *

fenetre = Tk()

champ_label = Label(fenetre, text="salut à tous")
bouton_quitter = Button(fenetre,text="Quitter", command=fenetre.quit)

champ_label.pack()
bouton_quitter.pack()

var_texte = StringVar()
ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
ligne_texte.pack()


var_case = IntVar()
case = Checkbutton(fenetre, text="Ne plus poser cette question", variable=var_case)
case.pack()
fenetre.mainloop()