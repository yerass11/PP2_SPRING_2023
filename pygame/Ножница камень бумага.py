#требуемая библиотека
from tkinter import *
import random

# создать обьект
root = Tk()

#обьем
root.geometry("400x400")

#установить заголовок
root.title("Камень, ножницы, бумага")

#балл
computer_value = {
	"0": "камень",
	"1": "бумага",
	"2": "ножницы"}

#сбросить игру


def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text="Player")
	l3.config(text="Computer")
	l4.config(text="")

#отключить кнопку


def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

#если игрок выбрал камень


def isrock():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "камень":
		match_result = "ничья"
	elif c_v == "ножницы":
		match_result = "Игрок выиграл"
	else:
		match_result = "Компьютер выиграл"
	l4.config(text=match_result)
	l1.config(text="Камень")
	l3.config(text=c_v)
	button_disable()

#если игрок выбрал бумага


def ispaper():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "бумага":
		match_result = "ничья"
	elif c_v == "ножницы":
		match_result = "компьютер выиграл"
	else:
		match_result = "Игрок выиграл"
	l4.config(text=match_result)
	l1.config(text="бумага")
	l3.config(text=c_v)
	button_disable()

#если игрок выбрал ножницы


def isscissor():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "камень":
		match_result = "компьтер выиграл"
	elif c_v == "ножницы":
		match_result = "ничья"
	else:
		match_result = "игрок выиграл"
	l4.config(text=match_result)
	l1.config(text="ножницы")
	l3.config(text=c_v)
	button_disable()


#Дабавим метки, рамки и кнопку
Label(root,
	text="Камень Ножницы Бумага",
	font="normal 18 bold",
	fg="green").pack(pady=18)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
		text="Игрок",
		font=15)

l2 = Label(frame,
		text="VS",
		font="normal 15 bold")

l3 = Label(frame, text="Компьютер", font=15)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root,
		text="",
		font="normal 20 bold",
		bg="white",
		width=15,
		borderwidth=2,
		relief="solid")
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Камень",
			font=10, width=7,
			command=isrock)

b2 = Button(frame1, text="Бумага",
			font=10, width=7,
			command=ispaper)

b3 = Button(frame1, text="Ножницы",
			font=10, width=7,
			command=isscissor)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

Button(root, text="Сбросить игру",
	font=10, fg="yellow",
	bg="black", command=reset_game).pack(pady=20)

# Execute Tkinter
root.mainloop()
