import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk,Image
from matplotlib import style

df= pd.read_csv("pokemon.csv")
df.set_index('Name',inplace=True)
x = []
TotalCash = 2000
j = 0
i = 0
tot = 0
def pokecash(): # Creating "Choose Dream Team" which alow you to choose and save pokemon into a list depends on the amount of their total points.

    def add(): #Adding pokemons into list under limitation of up to 6 pokemons and sum of total points under 2000.
        global x
        global j
        global TotalCash
        global tot
        try:
            name1 = txt.get().capitalize()
            while j <= 6:
                if j >= 6:
                    mb.showerror('Pokedex',"You can only choose up to 6 Pokemons!")
                    j=0
                    break
                if TotalCash - (df.loc[name1]["Total"]) < 0:
                    j=0
                    break
                else:
                    global lbl

                    res = name1
                    lbl = Label(cash, text=res,font=("Arial Bold", 12),bg="white")
                    lbl.grid(column=1, row=6 + j)
                    lbl = Label(cash, text=df.loc[name1]["Total"],font=("Arial Bold", 12),bg="white")
                    lbl.grid(column=2, row=6 + j)
                    lbl = Label(cash, text=str(int(TotalCash - df.loc[name1]["Total"])),font=("Arial Bold", 12), bg='white', fg='black', width=8)
                    lbl.grid(column=1, row=2)
                    tot += df.loc[name1]["Total"]
                    lbl = Label(cash, text=int(tot), font=("Arial Bold", 12), bg='white', fg='black', width=8)
                    lbl .grid(column=3, row=4)
                    TotalCash -= df.loc[name1]["Total"]
                    x.append(name1)
                    myImage = ImageTk.PhotoImage(Image.open("images\\" + name1 + ".png"))
                    lbl = Label(cash, image=myImage, bg="white")
                    lbl.image = myImage
                    lbl.grid(column=0, row=6 + j)
                    j += 1
                    # print(tot)
                    # print(TotalCash)
                    break
        except:

            mb.showerror('Pokedex',"This Pokemon does not exist")

    def save(): # saving the list of the pokemon into csv file.
        text_file = open("MyDreamTeam.txt", "a")
        text_file.write(str(x) + "\n")
        text_file.close()
        mb.showinfo("MyDreamTeam", "Your Pokemon dream team saved at file:-MyDreamTeam-")
    def restart(): #clean the list from any data.
        global TotalCash
        global  tot
        global j
        global x

        tot=0
        lbl = Label(cash, text=int(tot), font=("Arial Bold", 12), bg='white', fg='black', width=8)
        lbl.grid(column=3, row=4)
        TotalCash=2000
        lbl = Label(cash, text=str(TotalCash), font=("Arial Bold", 12), bg='white', fg='black', width=8)
        lbl.grid(column=1, row=2)
        for lbl in cash.grid_slaves():

            if int(lbl.grid_info()["row"]) > 5:
                lbl.grid_forget()
        j=0
        x=[]

    cash = Toplevel(root)
    cash.title("Pokemon Dream Team")
    cash.iconbitmap('pokemon_icon.ico')


    img = Image.open("58401.jpg")
    img = img.resize((750, 450), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    img = ImageTk.PhotoImage(img)


    logolbl = Label(cash, image=img)
    logolbl.image = img
    logolbl.place(relwidth=1, relheight=1)

    lbl1 = Label(cash, text="Goota Choose E'm Wisley...", font=("Arial Bold", 20), bg='white', fg='crimson').grid(column=0, row=0)
    lbl2 = Label(cash, text="youre PokeCash Balance is:", font=("Arial Bold", 12), bg='white', fg='black').grid(column=0, row=2)
    lbl3 = Label(cash, text=str(int(TotalCash)), font=("Arial Bold", 12), bg='white', fg='black').grid(column=1, row=2)
    Label(cash, text="Enter Choosen Pokemon Name", font=("Arial Bold", 12), bg='white', fg='black').grid(column=0, row=3)
    txt = Entry(cash, width=20)
    txt.grid(column=1, row=3)
    btn1 = Button(cash, text="Choose!", command=add, font=("Arial Bold", 10), bg='white', fg='crimson').grid(column=2, row=3)
    lbl11 = Label(cash, text="Team Total:", font=("Arial Bold", 8), bg='white', fg='black').grid(column=2, row=4)
    lbl5 = Label(cash, text="youre DreamTeam is:", font=("Arial Bold", 12), bg='white', fg='black').grid(column=0, row=4)
    btn2 = Button(cash, text="Save!", command=save, font=("Arial Bold", 10), bg='white', fg='crimson').grid(column=2,row=0)
    lbl10 = Label(cash, text=tot, font=("Arial Bold", 12), bg='white', fg='black', width=8).grid(column=3, row=4)
    btn3 = Button(cash, text="Reset", command=restart, font=("Arial Bold", 10), bg='white', fg='crimson').grid(column=3, row=3)



def image(): #allow you to present the image of the pokemon you type in the text box.
    imageroot = Toplevel(root)
    imageroot.iconbitmap('pokemon_icon.ico')
    imageroot.minsize(200, 100)
    name=txt.get()
    img = Image.open("58401.jpg")
    img = img.resize((750, 450), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    img = ImageTk.PhotoImage(img)

    logolbl = Label(imageroot, image=img)
    logolbl.image = img
    logolbl.place(relwidth=1, relheight=1)

    try:
      myImage = ImageTk.PhotoImage(Image.open("images\\" + name + ".png"))
      label = Label(imageroot,image=myImage, bg="white")
      label.image = myImage
      label.grid(column=0, row=0)

    except:
       mb.showerror("Pokedex", "This Pokemon does not exist")

def FirstGen(): #present a list of names of the first generation of pokemon
    gen1List=Toplevel(root)
    gen1List.iconbitmap('pokemon_icon.ico')
    df = pd.read_csv("pokemon.csv")
    count=0
    for i in range(21):
        for j in range(8):
            if count < 800:
                Label(gen1List, text=str(df.loc[count]["Name"])).grid(row=i, column=j)
                count += 1
def secondGen():#present a list of names of the second generation of pokemon
    gen2List=Toplevel(root)
    gen2List.iconbitmap('pokemon_icon.ico')
    df = pd.read_csv("pokemon.csv")
    count=166
    for i in range(21):
        for j in range(5):
            if count < 800:
                Label(gen2List, text=str(df.loc[count]["Name"])).grid(row=i, column=j)
                count += 1
def thirdGen():#present a list of names of the third generation of pokemon
    gen3List=Toplevel(root)
    gen3List.iconbitmap('pokemon_icon.ico')
    df = pd.read_csv("pokemon.csv")
    count=272
    for i in range(20):
        for j in range(8):
            if count < 800:
                Label(gen3List, text=str(df.loc[count]["Name"])).grid(row=i, column=j)
                count += 1
def forthGen():#present a list of names of the forth generation of pokemon
    gen4List = Toplevel(root)
    gen4List.iconbitmap('pokemon_icon.ico')
    df = pd.read_csv("pokemon.csv")
    count=432
    for i in range(12):
        for j in range(10):
            if count < 800:
                Label(gen4List, text=str(df.loc[count]["Name"])).grid(row=i, column=j)
                count += 1
def fifthGen():#present a list of names of the fifth generation of pokemon
    gen5List=Toplevel(root)
    gen5List.iconbitmap('pokemon_icon.ico')
    df = pd.read_csv("pokemon.csv")
    count=554
    for i in range(20):
        for j in range(8):
            if count < 800:
                Label(gen5List, text=str(df.loc[count]["Name"])).grid(row=i, column=j)
                count += 1
def sixthGen():#present a list of names of the sixth generation of pokemon
    gen6List=Toplevel(root)
    gen6List.iconbitmap('pokemon_icon.ico')
    df = pd.read_csv("pokemon.csv")
    count=718
    for i in range(10):
        for j in range(8):
            if count < 800:
                Label(gen6List, text=str(df.loc[count]["Name"])).grid(row=i, column=j)
                count += 1



def setMenu(win): #Creating menubar for diffrent topics.
    menubar = Menu(win)

    filemenu = Menu(menubar)
    filemenu.add_command(label="First Gen", command=FirstGen)
    filemenu.add_command(label="Second Gen", command=secondGen)
    filemenu.add_command(label="Third Gen", command=thirdGen)
    filemenu.add_command(label="Forth Gen", command=forthGen)
    filemenu.add_command(label="Fifth Gen", command=fifthGen)
    filemenu.add_command(label="Sixth Gen", command=sixthGen)

    teammenu = Menu(menubar)
    teammenu.add_command(label="Make a Team", command=pokecash)
    menubar.add_cascade(label="Choose Dream Team", menu=teammenu)
    menubar.add_cascade(label="Pokemon List", menu=filemenu)

    win.config(menu=menubar)

def battle(): #compering two pokemons and present the stronger of them
    global lblbtl
    try:
        if df.loc[txt3.get().capitalize() ]['Total'] > df.loc[txt4.get().capitalize() ]['Total']:
            lblbtl.configure(text=txt3.get().capitalize() +" is the winner!")
        if (df.loc[txt3.get().capitalize() ]['Total']) < (df.loc[txt4.get().capitalize() ]['Total']):
            lblbtl.configure(text=txt4.get().capitalize() +" is the winner!")
        if (df.loc[txt3.get().capitalize()]['Total']) == (df.loc[txt4.get().capitalize()]['Total']):
            lblbtl.configure(text="It's a tie!")
    except:
            mb.showerror("Pokedex", "Choose other Pokemons")
    lblbtl.grid(column=2, row=5)

def pkstats(): #showing the stats of the pokemon using pandas libary
    try:

        axis_x = [ 'HP', 'Atk', 'Def', 'Sp.atk', 'Sp.def', 'Speed']
        axis_y = [ df.loc[txt.get().capitalize() ]['HP'], df.loc[txt.get().capitalize() ]['Attack'],
                  df.loc[txt.get().capitalize() ]['Defense'], df.loc[txt.get().capitalize() ]['Sp. Atk'], df.loc[txt.get().capitalize() ]['Sp. Def'],
                  df.loc[txt.get().capitalize() ]['Speed']]
        plt.bar(axis_x, axis_y)
        plt.xlabel("Stats")
        plt.ylabel("Points")
        plt.title(txt.get().capitalize(),size=20,color='brown')
        plt.grid(True,color='r')
        plt.show()
    except:
        mb.showerror("Pokedex", "This Pokemon does not exist")

def showhp(): #comparing the chosen pokemon hp to the rest of the pokemon.
    try:
        HP = df['HP']
        number = df['#']
        numpoke = df.loc[txt.get().capitalize() ]['#']
        hppoke = df.loc[txt.get().capitalize() ]['HP']
        plt.scatter(number, HP, c='blue', alpha=0.5, vmin=-3, vmax=3, cmap="Spectral")
        plt.scatter(numpoke, hppoke, c='crimson', s=75, vmin=-3, vmax=3, cmap="Spectral",label=txt.get())
        plt.title('Compering Pokemon',size=20,color='red')
        plt.ylabel('HP Points')
        plt.xlabel('Pokemon')
        plt.grid(True, color='black')
        plt.legend()
        plt.show()
    except:
        mb.showerror("Pokedex", "This Pokemon does not exist")
def showatk():#comparing the chosen pokemon attack to the rest of the pokemon.
    try:
        Attack = df['Attack']
        number = df['#']
        numpoke = df.loc[txt.get().capitalize() ]['#']
        Attackpoke = df.loc[txt.get().capitalize() ]['Attack']

        plt.scatter(number, Attack, c='blue', alpha=0.5, vmin=-3, vmax=3, cmap="Spectral")
        plt.scatter(numpoke, Attackpoke, c='crimson', s=75, vmin=-3, vmax=3, cmap="Spectral",label=txt.get())
        plt.title('Compering Pokemon',size=20,color='red')
        plt.ylabel('Attack Points')
        plt.xlabel('Pokemon')
        plt.grid(True, color='black')
        plt.legend()
        plt.show()
    except:
        mb.showerror("Pokedex", "This Pokemon does not exist")

def showdef():#comparing the chosen pokemon defence to the rest of the pokemon.
    try:
        Defense = df['Defense']
        number = df['#']
        numpoke = df.loc[txt.get().capitalize() ]['#']
        Defensepoke = df.loc[txt.get().capitalize() ]['Defense']
        plt.scatter(number, Defense, c='blue', alpha=0.5, vmin=-3, vmax=3, cmap="Spectral")
        plt.scatter(numpoke, Defensepoke, c='crimson', s=75, vmin=-3, vmax=3, cmap="Spectral",label=txt.get())
        plt.title('Compering Pokemon',size=20,color='red')
        plt.ylabel('Defense Points')
        plt.xlabel('Pokemon')
        plt.grid(True, color='black')
        plt.legend()
        plt.show()
    except:
        mb.showerror("Pokedex", "This Pokemon does not exist")

def showspa():#comparing the chosen pokemon  super attack to the rest of the pokemon.
    try:
        Sp_Atk = df['Sp. Atk']
        number = df['#']
        numpoke = df.loc[txt.get().capitalize() ]['#']
        Sp_Atkpoke = df.loc[txt.get().capitalize() ]['Sp. Atk']
        plt.scatter(number, Sp_Atk, c='blue', alpha=0.5, vmin=-3, vmax=3, cmap="Spectral")
        plt.scatter(numpoke, Sp_Atkpoke, c='crimson', s=75, vmin=-3, vmax=3, cmap="Spectral",label=txt.get())
        plt.title('Compering Pokemon',size=20,color='red')
        plt.ylabel('Special Attack Points')
        plt.xlabel('Pokemon')
        plt.grid(True, color='black')
        plt.legend()
        plt.show()
    except:
        mb.showerror("Pokedex", "This Pokemon does not exist")

def showspd():#comparing the chosen pokemon super defence to the rest of the pokemon.
    try:
        Sp_Def = df['Sp. Def']
        number = df['#']
        numpoke = df.loc[txt.get().capitalize() ]['#']
        Sp_Defpoke = df.loc[txt.get().capitalize() ]['Sp. Def']
        plt.scatter(number, Sp_Def, c='blue', alpha=0.5, vmin=-3, vmax=3, cmap="Spectral")
        plt.scatter(numpoke, Sp_Defpoke, c='crimson', s=75, vmin=-3, vmax=3, cmap="Spectral",label=txt.get())
        plt.title('Spiceal Defense Pokemon',size=20,color='red')
        plt.ylabel('HP Points')
        plt.xlabel('Pokemon')
        plt.grid(True, color='black')
        plt.legend()
        plt.show()
    except:
        mb.showerror("Pokedex", "This Pokemon does not exist")

def showspeed():#comparing the chosen pokemon speed to the rest of the pokemon.
    try:
        Speed = df['Speed']
        number = df['#']
        numpoke = df.loc[txt.get().capitalize() ]['#']
        Speedpoke = df.loc[txt.get().capitalize() ]['Speed']

        plt.scatter(number, Speed, c='blue', alpha=0.5, vmin=-3, vmax=3, cmap="Spectral")
        plt.scatter(numpoke, Speedpoke, c='crimson', s=75, vmin=-3, vmax=3, cmap="Spectral",label=txt.get())
        plt.title('Compering Pokemon',size=20,color='red')
        plt.ylabel('Speed Points')
        plt.xlabel('Pokemon')
        plt.grid(True, color='black')
        plt.legend()
        plt.show()
    except:
        mb.showerror("Pokedex", "This Pokemon does not exist")

def showtot():#comparing the chosen pokemon total to the rest of the pokemon.
    try:
        Total = df['Total']
        number = df['#']
        numpoke = df.loc[txt.get().capitalize() ]['#']
        Totalpoke = df.loc[txt.get().capitalize() ]['Total']

        plt.scatter(number, Total, c='blue', alpha=0.5, vmin=-3, vmax=3, cmap="Spectral")
        plt.scatter(numpoke, Totalpoke, c='crimson', s=75, vmin=-3, vmax=3, cmap="Spectral",label=txt.get())
        plt.title('Compering Pokemon',size=20,color='red')
        plt.ylabel('Total Points')
        plt.xlabel('Pokemon')
        plt.grid(True, color='black')
        plt.legend()
        plt.show()
    except:
        mb.showerror("Pokedex", "This Pokemon does not exist")

def mainpie():#showing pie chart of the frequency of the main type.
    global ax1
    ax1 = plt.figure(1)
    ax1 = df['Type 1'].value_counts().plot(kind='pie', autopct='%1.1f%%', pctdistance=1.0)
    plt.title('Main Type')
    plt.show()

def secpie():#showing pie chart of the frequency of the secondary type.
    global ax2
    ax2 = plt.figure(2)
    ax2 = df['Type 2'].value_counts().plot(kind='pie', autopct='%1.1f%%', pctdistance=1.0)
    plt.title('Second Type')
    plt.show()


def topest(): #presenting the top 5 pokemon from different kind of abilities
    try:
        Top = ''
        if var.get()==1:
            Top='HP'
            Col='red'
        if var.get() == 2:
            Top='Attack'
            Col='blue'
        if var.get() == 3:
            Top='Defense'
            Col='green'
        if var.get() == 4:
            Top='Speed'
            Col='pink'
        if var.get() == 5:
            Top='Total'
            Col='brown'
        df = pd.read_csv("pokemon.csv")
        x = df.nlargest(5, Top, keep='first')["Name"]
        y = df.nlargest(5, Top, keep='first')[Top]
        plt.figure(figsize=(25,5))
        plt.bar(x, y, color=Col,width=0.4 )
        plt.title('Top 5 ' + Top,size=20)
        plt.xlabel('Pokemons Names',size=15,color='brown')
        plt.ylabel(Top+" Points")
        plt.grid(color='black')
        plt.show()
    except:
        mb.showerror("Pokedex", "You need to choose one of the options!")
root=Tk()
var=IntVar()
root.iconbitmap('pokemon_icon.ico')
root.title('Pokedex')

img = Image.open("backgroud.jpeg")
img = img.resize((750, 450), Image.ANTIALIAS) #The (250, 250) is (height, width)
img = ImageTk.PhotoImage(img)
logolbl=Label(root,image=img)
logolbl.place(relwidth=1,relheight=1)

#main titels

imageBtn=Button(root, text="See Image", command=image,font=("Arial Bold", 10)).grid(column=0, row=4)
lbl = Label(root, text="Pokemon Stats:  ",font=("Impact", 20),bg='Midnight blue',fg='Lemon Chiffon')
lbl4 = Label(root, text="Pokemons Info:  ",font=("Impact", 20),bg='Midnight blue',fg='Lemon Chiffon')
lbl7 = Label(root, text="Pokemons Battle",font=("Impact", 20),bg='Midnight blue',fg='Lemon Chiffon')

#secondery titles
lbl2=Label(root, text="Enter a Pokemon name:",font=("Impact", 12),bg='Navy',fg='Lemon Chiffon')
lbl5=Label(root, text="Choose category Top 5:",font=("Impact", 12),bg='Navy',fg='Lemon Chiffon')
lbl8=Label(root, text="Enter 2 Pokemon for battle:",font=("Impact", 12),bg='Navy',fg='Lemon Chiffon')
lbl3=Label(root, text="Relative Stats of your Pokemon:",font=("Impact", 12),bg='Navy',fg='Lemon Chiffon')
lbl6=Label(root, text="See Pie chart type:",font=("Impact", 12),bg='Navy',fg='Lemon Chiffon')

#other labels and btns
txt = Entry(root)
btn=Button(root, text="See Stats",font=("Arial Bold", 10),command=pkstats)
btn2=Button(root, text="HP",command=showhp,font=("Arial Bold", 10))
btn3=Button(root, text="Attack",command=showatk,font=("Arial Bold", 10))
btn4=Button(root, text="Defense",command=showdef,font=("Arial Bold", 10))
btn5=Button(root, text="SP.Atk",command=showspa,font=("Arial Bold", 10))
btn6=Button(root, text="SP.Def",command=showspd,font=("Arial Bold", 10))
btn7=Button(root, text="Speed",command=showspeed,font=("Arial Bold", 10))
btn1=Button(root, text="Total",command=showtot,font=("Arial Bold", 10))
rad1=Radiobutton(root,text='HP', value=1,variable=var,font=("Arial Bold", 10)).grid(column=1, row=2)
rad2=Radiobutton(root,text='Attack', value=2,variable=var,font=("Arial Bold", 10)).grid(column=1, row=3)
rad3=Radiobutton(root,text='Defense', value=3,variable=var,font=("Arial Bold", 10)).grid(column=1, row=4)
rad4=Radiobutton(root,text='Speed', value=4,variable=var,font=("Arial Bold", 10)).grid(column=1, row=5)
rad5=Radiobutton(root,text='Total', value=5,variable=var,font=("Arial Bold", 10)).grid(column=1, row=6)
btn8=Button(root, text="OK",command=topest,font=("Arial Bold", 10))
btn9=Button(root, text="Main Type",command=mainpie,font=("Arial Bold", 10))
btn10=Button(root, text="Secondary Type",command=secpie,font=("Arial Bold", 10))
txt3 = Entry(root)
txt4 = Entry(root)
btn11=Button(root, text="Let's Battle!!!",command=battle,font=("Arial Bold", 10))
lblbtl=Label(root,text=' ',bg="crimson")
lbl9 = Label(root, text="Pokemons Save",font=("Arial Bold", 20),bg='white',fg='yellow')

setMenu(root)

lbl.grid(column=0, row=0)
lbl2.grid(column=0, row=1)
txt.grid(column=0, row=2)
btn.grid(column=0, row=3)
lbl3.grid(column=0, row=5)
btn2.grid(column=0, row=6)
btn3.grid(column=0, row=7)
btn4.grid(column=0, row=8)
btn5.grid(column=0, row=9)
btn6.grid(column=0, row=10)
btn7.grid(column=0, row=11)
btn1.grid(column=0, row=12)

lbl4.grid(column=1, row=0)
lbl5.grid(column=1, row=1)
btn8.grid(column=1, row=7)
lbl6.grid(column=1, row=9)
btn9.grid(column=1, row=10)
btn10.grid(column=1, row=11)

lbl7.grid(column=2, row=0)
lbl8.grid(column=2, row=1)
txt3.grid(column=2, row=2)
txt4.grid(column=2, row=3)
btn11.grid(column=2, row=4)
lblbtl.grid(column=2, row=5)

root.mainloop()

