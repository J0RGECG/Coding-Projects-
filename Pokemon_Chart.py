import tkinter as tk
root = tk.Tk()
root.geometry("700x500")
def normal_weak():
   labble = tk.Label(root,text="normal weakness")
   labble.pack()
   labble1 =tk.Label(root,text="FIGHTING",foreground="#8B0000")
   labble1.pack()
   
def flying_weak():
   labble = tk.Label(root,text="flying weakness")
   labble.pack()
   weakness1 = tk.Label(root,text="ELECTRIC",foreground="#8B8000")
   weakness2 = tk.Label(root,text="ROCK",fg="brown")
   weakness3 = tk.Label(root,text="ICE",foreground="#0D98BA")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()

def psychic_weak():
   labble = tk.Label(root,text="PSYCHIC WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="GHOST",foreground="#CBC3E3")
   weakness2 = tk.Label(root,text="BUG",foreground="#90EE90")
   weakness3 = tk.Label(root,text="DARK",fg="black")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()
   
def rock_weak():
   labble = tk.Label(root,text="ROCK WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="WATER",fg="blue")
   weakness2 = tk.Label(root,text='GRASS',fg="green")
   weakness3 = tk.Label(root,text='FIGHTING',foreground="#8B0000")
   weakness4 = tk.Label(root,text='GROUND',foreground="#5C4033")
   weakness5 = tk.Label(root,text='STEEL',foreground="#D3D3D3")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()
   weakness4.pack()
   weakness5.pack()

def bug_weakness():
   labble = tk.Label(root,text="BUG WEAkNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="FIRE",fg="red")
   weakness2 = tk.Label(root,text="ROCK",fg="brown")
   weakness3 = tk.Label(root,text="FLYING",foreground="#89CFF0")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()

def dark_weakness():
   labble = tk.Label(root,text="DARK WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="FIGHTING",foreground="#8B0000")
   weakness2 = tk.Label(root,text="BUG",foreground="#90EE90")
   weakness3 = tk.Label(root,"FAIRY",fg="pink")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()

def Ghost_weakness():
   labble = tk.Label(root,text="GHOST WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="GHOST")
   weakness2 = tk.Label(root,text="DARK")
   weakness1.pack()
   weakness2.pack()

def water_weakness():
   labble = tk.Label(root,text="WATER WEAKNESS")
   labble.pack
   weakness2 = tk.Label(root,text='GRASS',fg="green")
   weakness1 = tk.Label(root,text="ELECTRIC",foreground="#8B8000")
   weakness1.pack()
   weakness2.pack()

def grass_weakness():
   labble = tk.Label(root,text="GRASS WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="FIRE",fg="red")
   weakness2 = tk.Label(root,text="ICE",foreground="#0D98BA")
   weakness3 = tk.Label(root,text='POISON',fg='purple')
   weakness4 = tk.Label(root,text="FLYING",foreground="#89CFF0")
   weakness5 = tk.Label(root,text="BUG",foreground="#90EE90")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()
   weakness4.pack()
   weakness5.pack()

def electric_weakness():
   labble = tk.Label(root,text="ELECTRIC WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text='GROUND',foreground="#5C4033")
   weakness1.pack()

def fire_weakness():
   labble = tk.Label(root,text="FIRE WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text='GROUND',foreground="#5C4033")
   weakness2 = tk.Label(root,text="WATER",fg="blue")
   weakness3 = tk.Label(root,text="ROCK",fg="brown")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()

def dragon_weakness():
   labble = tk.Label(root,text="DRAGON WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="ICE",foreground="#0D98BA")
   weakness2 = tk.Label(root,text="DRAGON",foreground='#00008B')
   weakness3 = tk.Label(root,text="FAIRY",fg="pink")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()

def ice_weakness():
   labble = tk.Label(root,text="ICE WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="FIRE",fg="red")
   weakness2 = tk.Label(root,text='FIGHTING',foreground="#8B0000")
   weakness3 = tk.Label(root,text="ROCK",fg="brown")
   weakness4 = tk.Label(root,text='STEEL',foreground="#D3D3D3")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()
   weakness4.pack()

def fairy_weakness():
   labble = tk.Label(root,text="FAIRY WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text='POISON',fg='purple')
   weakness2 = tk.Label(root,text='STEEL',foreground="#D3D3D3")   
   weakness1.pack()
   weakness2.pack()

def fight_weakness():
   labble = tk.Label(root,text="FIGHTING WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="FLYING",foreground="#89CFF0")
   weakness2 = tk.Label(root,text="PSYCHIC",fg="purple")
   weakness3 = tk.Label(root,text="FAIRY",fg="pink")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()

def ground_weakness():
   labble = tk.Label(root,text="GROUND WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="WATER",fg="blue")
   weakness2 = tk.Label(root,text='GRASS',fg="green" )
   weakness3 = tk.Label(root,text="ICE",foreground="#0D98BA")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()

def steel_weakness():
   labble = tk.Label(root,text="STEEL WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text="FIRE",fg="red")
   weakness2 = tk.Label(root,text='FIGHTING',foreground="#8B0000")
   weakness3 = tk.Label(root,text='GROUND',foreground="#5C4033")
   weakness1.pack()
   weakness2.pack()
   weakness3.pack()

def poison_weakness():
   labble = tk.Label(root,text="POISON WEAKNESS")
   labble.pack()
   weakness1 = tk.Label(root,text='GROUND',foreground="#5C4033")
   weakness2 = tk.Label(root,text= "PSYCHIC",fg="purple")
   weakness1.pack()
   weakness2.pack()


def button_for_chart():

   normal = tk.Button(my_topframe,text="NORMAL",fg="gray",font=("arial",17),width=7,height=1,command= normal_weak)
   normal.pack(side="left")

   flying = tk.Button(my_topframe,text="FLYING",foreground="#89CFF0",font=("arial",17),width=7,height=1,command=flying_weak)
   flying.pack(side="left")

   psychic = tk.Button(my_topframe,text="PSYCHIC",fg="purple",font=('arial',17),width=7,height=1,command=psychic_weak)
   psychic.pack(side="left")

   rock = tk.Button(my_topframe,text="ROCK",fg="brown",font=("arial",17),width=7,height=1,command=rock_weak)
   rock.pack(side='left')

   bug = tk.Button(my_topframe,text="BUG",foreground="#90EE90",font=('arial',17),width=7,height=1,command=bug_weakness)
   bug.pack(side="left")

   dark = tk.Button(my_topframe,text="DARK",fg="black",font=('arial',17),width=7,height=1,command=dark_weakness)
   dark.pack(side="left")

   Ghost = tk.Button(mybotton,text="GHOST",foreground="#CBC3E3",font=('arial',17),width=7,height=1,command=Ghost_weakness)
   Ghost.pack(side="left")

   water = tk.Button(mybotton,text="WATER",fg="blue",font=('arial',17),width=7,height=1,command=water_weakness)
   water.pack(side="left")

   grass = tk.Button(mybotton,text='GRASS',fg="green",font=('arial',17),width=7,height=1,command=grass_weakness)
   grass.pack(side="left")

   electric = tk.Button(mybotton,text="ELECTRIC",foreground="#8B8000",font=("arial",17),width=7,height=1,command=electric_weakness)
   electric.pack(side="left")

   fire = tk.Button(mybotton,text="FIRE",fg="red",font=('arial',17),width=7,height=1,command=fire_weakness)
   fire.pack(side='left')

   dragon = tk.Button(mybotton,text="DRAGON",foreground='#00008B',font=('arial',17),width=7,height=1,command= dragon_weakness)
   dragon.pack(side="left")

   ice = tk.Button(lastframe,text="ICE",foreground="#0D98BA",font=('arial',17),width=7,height=1,command=ice_weakness)
   ice.pack(side="left")

   fairy = tk.Button(lastframe,text="FAIRY",fg="pink",font=('arial',17),width=7,height=1,command=fairy_weakness)
   fairy.pack(side="left")

   fighting = tk.Button(lastframe,text='FIGHTING',foreground="#8B0000",font=('arial',17),width=7,height=1,command=fight_weakness)
   fighting.pack(side="left")

   ground = tk.Button(lastframe,text='GROUND',foreground="#5C4033",font=('arial',17),width=7,height=1,command=ground_weakness)
   ground.pack(side='left')

   steel = tk.Button(lastframe,text='STEEL',foreground="#D3D3D3",font=('arial',17),width=7,height=1,command=steel_weakness)
   steel.pack(side="left")

   poison = tk.Button(lastframe,text='POISON',fg='purple',font=('arial',17),width=7,height=1)
   poison.pack(side="left")


labbleTop = tk.Label(root,text="Hello welcome to POkX.",font=('arial',18))
labbleTop.pack()


ButtonforPK = tk.Button(root,text="Click to view type chart!",command=button_for_chart)
ButtonforPK.pack()



my_topframe = tk.Frame(root,highlightthickness=4)
my_topframe.pack()



mybotton =tk.Frame(root,highlightthickness=4)
mybotton.pack()

lastframe = tk.Frame(root,highlightthickness=4)
lastframe.pack()


root.mainloop()
