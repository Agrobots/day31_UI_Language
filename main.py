from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Play")
# window.config(padx=50, pady=50)

flash = Canvas(height=200, width=200)
back_img = PhotoImage(file="./images/card_back.png")
flash.create_image(100, 100, image=back_img)
flash.grid(row=0, column=0)

window.mainloop()




