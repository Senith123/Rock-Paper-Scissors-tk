from tkinter import*
import random
screen = Tk()
screen.geometry("500x500")
screen.title("sample")
screen.config(background = 'LightSteelBlue2')
list = ["Rock", "Paper", "Scissor"]
computer = ""
user = ""
cs = 0
ps = 0
def decidewinner(userchoice):
    global cs, ps, computer, user
    user = userchoice
    computer = random.choice(list)
    if user == computer:
        title2.config(text = "It's A Draw")
    elif user == 'Rock' and computer == 'Paper':
        title2.config(text = "AI Wins")
        cs = cs + 1
    elif user == 'Rock' and computer == 'Scissor':
        title2.config(text = "You Win")
        ps = ps + 1
    elif user == 'Paper' and computer == 'Rock':
        title2.config(text = "You Win")
        ps = ps + 1
    elif user == 'Paper' and computer == 'Scissor':
        title2.config(text = "AI Wins")
        cs = cs + 1
    elif user == 'Scissor' and computer == 'Paper':
        title2.config(text = "You Win")
        ps = ps + 1
    elif user == 'Scissor' and computer == 'Rock':
        title2.config(text = "AI Wins")
        cs = cs + 1
    title4.config(text = f"AI Says : {computer}")
    title5.config(text = f"You Said : {user}")
    title6.config(text = f"AI Score : {cs}")
    title7.config(text = f"Player Score : {ps}")
title1 = Label(screen, text = "Rock Paper Scissors", bg = "LightSkyBlue2", fg = "LightSkyBlue4", font = ("times", 35, "bold"))
title1.place(x = 47, y = 50)
title2 = Label(screen, text = "Press The Buttons To Start", bg = "LightSkyBlue2", fg = "LightSkyBlue4", font = ("times", 20, "bold"))
title2.place(x = 83, y = 150)
rock = Button (screen, text = "Rock", bg = "LightSteelBlue3", fg = "LightSkyBlue4", font = ("times", 20, "bold"), command = lambda : decidewinner("Rock"))
rock.place(x = 70, y = 200)
paper = Button (screen, text = "Paper", bg = "LightSteelBlue3", fg = "LightSkyBlue4", font = ("times", 20, "bold"), command = lambda : decidewinner("Paper"))
paper.place(x = 200, y = 200)
scissor = Button (screen, text = "Scissor", bg = "LightSteelBlue3", fg = "LightSkyBlue4", font = ("times", 20, "bold"), command = lambda : decidewinner("Scissor"))
scissor.place(x = 340, y = 200)
title3 = Label(screen, text = "LeaderBoard", bg = "LightSkyBlue2", fg = "LightSkyBlue4", font = ("times", 30, "bold"))
title3.place(x = 147, y = 290)
title4 = Label(screen, text = "AI Says : ", bg = "LightSkyBlue2", fg = "LightSkyBlue4", font = ("times", 15, "bold"))
title4.place(x = 60, y = 350)
title5 = Label(screen, text = "Player Says : ", bg = "LightSkyBlue2", fg = "LightSkyBlue4", font = ("times", 15, "bold"))
title5.place(x = 250, y = 350)
title6 = Label(screen, text = "AI Score : ", bg = "LightSkyBlue2", fg = "LightSkyBlue4", font = ("times", 15, "bold"))
title6.place(x = 60, y = 400)
title7 = Label(screen, text = "Player Score : ", bg = "LightSkyBlue2", fg = "LightSkyBlue4", font = ("times", 15, "bold"))
title7.place(x = 250, y = 400)
screen.mainloop()
