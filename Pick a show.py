from tkinter import *
import tkinter.messagebox




from tkinter import *
import tkinter as tk
from tkinter import ttk
from functools import partial
import random
import string
c=0
mnam=""
sno=""
axe=""
ax=""
px=""
axyx=""
snx=[]




c = 0
price = 0
root = Tk()
root.title("Pick a Show")
root.configure(bg="black")
root.geometry("1600x900")


rot = Frame(root)

rot.pack()
movies = ["Vikram", "Varisu", "Ponniyan Selvan", "Naane Varuven", "Trigger", "Vendhu Thanindhadhu Kadu", "Sinam",
          "Sitha Raman", "Brahmasthra", "Aadhar", "Thiruchithrambalam", "Diary", "Kanam", "Cobra"]




def v(ab):
    global mnam
    global a
    global ax
    global axe
    if ab == vikram:
        mnam = "Vikram (Tamil)"
    if ab == varisu:
        mnam = "Varisu (Tamil)"
    if ab == ps:
        mnam = "Ponniyan Selvan (Tamil)"
    if ab == nv:
        mnam = "Naane Varuven (Tamil)"
    if ab == tr:
        mnam = "Trigger (Tamil)"
    if ab == vt:
        mnam = "Vendhu Thanindhadhu Kadu (Tamil)"
    if ab == sno:
        mnam = "Sinam (Tamil)"
    if ab == sr:
        mnam = "Sitha Raman (Telugu)"
    if ab == br:
        mnam = "Brahmasthra (Hindi)"
    if ab == aa:
        mnam = "Aadhar (Tamil)"
    if ab == re:
        mnam = "Rendagm (Tamil)"
    if ab == th:
        mnam = "Thiruchithrambalam (Tamil)"
    if ab == dr:
        mnam = "Diary (Tamil)"
    if ab == kn:
        mnam = "Kanam (Tamil)"
    if ab == cr:
        mnam = "Cobra (Tamil)"
    if ab == vv:
        mnam = "Vikram Vedha"



    roott = Tk()
    rtt = Frame(roott)
    rtt.grid()
    roott.title("Pick a show (Date,time and Venue)")
    roott.geometry("800x400")
    roott.resizable(0, 0)

    def chh():

        def dw():
            rp2 = tk.Tk()
            rp2.title("Select Snacks")
            rp2.geometry("1000x500")
            rp2.resizable(0, 0)

            def pay():

                def offl():
                    rp4 = tk.Tk()
                    rp4.title("Pick a show (offline)")
                    rp4.geometry("1000x700")
                    rp4.resizable(0, 0)
                    sa = Label(rp4,
                               text="BOOKING CONFIRMED \n Show the code" + xx + "at the booking counter to pay and aviail your ticket \n Thank you",
                               padx=300, pady=300, font=("arial", 14))
                    sa.grid(row=500, column=350, sticky="news")

                def onli():
                    rp5 = tk.Tk()
                    rp5.title("Pick a show (online)")
                    price = 0

                alpha = [chr(ay) for ay in range(65, 91)]
                num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                xx = random.choice(alpha) + random.choice(alpha) + random.choice(alpha) + str(random.choice(num)) + str(
                    random.choice(num)) + random.choice(alpha)
                global a
                global ax
                global axe
                rp3 = tk.Tk()
                rp3.geometry("400x400")
                rp3.resizable(0, 0)
                rp3.title("Pick a show (Bill)")
                b = Label(rp3, text="Final Bill : \n" + xx)
                b.grid(row=0, column=0, sticky="news")
                bc = Label(rp3, text=mnam + "\n" + "Number of tickets = " + str(c), padx=30, pady=20)
                bc.grid(row=1, column=0, sticky="news")
                bcd = Label(rp3, text="Seat numbers : " + "\n" + str(snx) + "\n" + axe + "\n" + ax + "\n" + axyx , padx=30, pady=20)
                bcd.grid(row=2, column=0, sticky="news")
                bdc = Label(rp3, text="Amount to be paid" + "\n" + str(price) + "\n" + "With taxes" + "\n" + str(price + ((price * 18) / 100)))
                bdc.grid(row=1, column=3, sticky="news")
                chck = Label(rp3, text="Mode of payment :")
                chck.grid(row=3, column=0, sticky="news")


                offl = Button(rp3, text="Offline", pady=20, padx=30, command=offl)
                offl.grid(row=5, column=0, sticky="news")

            def cv(x):
                global price
                x.configure(bg="green")
                if x == sn3:
                    price += 240
                if x == sn4:
                    price += 205
                if x == sn5:
                    price += 175
                if x == sn6:
                    price += 135
                if x == sn7:
                    price += 50
                if x == sn8:
                    price += 150
                if x == sn9:
                    price += 185
                if x == sn10:
                    price += 160
                if x == sn11:
                    price += 210
                if x == sn12:
                    price += 150
                if x == sn13:
                    price += 135
                if x == sn14:
                    price += 235
                if x == sn15:
                    price += 160
                if x == sn16:
                    price += 190
                if x == sn17:
                    price += 160
                if x == sn18:
                    price += 160
                if x == sn19:
                    price += 160
                if x == sn20:
                    price += 160


            sn = Label(rp2, text="Select the snacks you want")
            sn.grid(row=0, column=0)
            sns = Button(rp2, text="Next", padx=20, pady=10, command=pay)
            sns.grid(row=0, column=50)
            sn1 = Label(rp2, text="")
            sn1.grid(row=1)
            sn3 = Button(rp2, text="Large Popcorn \n Price:240", padx=50, pady=50)
            sn3.config(command=lambda d=sn3: cv(d))
            sn3.grid(row=2, column=0, sticky="news")
            sn4 = Button(rp2, text="Regular Popcorn \n Price:205", padx=50, pady=50)
            sn4.config(command=lambda d1=sn4: cv(d1))
            sn4.grid(row=2, column=1, sticky="news")
            sn5 = Button(rp2, text="Small Popcorn \n Price:175", padx=50, pady=50)
            sn5.config(command=lambda d2=sn5: cv(d2))
            sn5.grid(row=2, column=2, sticky="news")
            sn6 = Button(rp2, text="Cream donut \n Price:135", padx=50, pady=50)
            sn6.config(command=lambda d3=sn6: cv(d3))
            sn6.grid(row=2, column=3, sticky="news")
            sn7 = Button(rp2, text="Smart water (750 ml) \n Price:50", padx=50, pady=50)
            sn7.config(command=lambda d4=sn7: cv(d4))
            sn7.grid(row=2, column=4, sticky="news")
            sn8 = Button(rp2, text="Cold coffee \n Price:150", padx=50, pady=50)
            sn8.config(command=lambda d5=sn8: cv(d5))
            sn8.grid(row=2, column=5, sticky="news")
            sn9 = Button(rp2, text="French fries \n Price:185", padx=50, pady=50)
            sn9.config(command=lambda d6=sn9: cv(d6))
            sn9.grid(row=3, column=0, sticky="news")
            sn10 = Button(rp2, text="Bhel puri \n Price:160", padx=50, pady=50)
            sn10.config(command=lambda d7=sn10: cv(d7))
            sn10.grid(row=3, column=1, sticky="news")
            sn11 = Button(rp2, text="Grilled vegetable sandwich \n Price:210", padx=50, pady=50)
            sn11.config(command=lambda d8=sn11: cv(d8))
            sn11.grid(row=3, column=2, sticky="news")
            sn12 = Button(rp2, text="Filter coffee \n Price:150", padx=50, pady=50)
            sn12.config(command=lambda d9=sn12: cv(d9))
            sn12.grid(row=3, column=3, sticky="news")
            sn13 = Button(rp2, text="Choco donut \n Price:135", padx=50, pady=50)
            sn13.config(command=lambda d10=sn13: cv(d10))
            sn13.grid(row=3, column=4, sticky="news")
            sn14 = Button(rp2, text="Nachos \n Price:235", padx=50, pady=50)
            sn14.config(command=lambda d11=sn14: cv(d11))
            sn14.grid(row=3, column=5, sticky="news")
            sn15 = Button(rp2, text="Vada pav \n Price:160", padx=50, pady=50)
            sn15.config(command=lambda d12=sn15: cv(d12))
            sn15.grid(row=4, column=0, sticky="news")
            sn16 = Button(rp2, text="Burger \n Price:190", padx=50, pady=50)
            sn16.config(command=lambda d13=sn16: cv(d13))
            sn16.grid(row=4, column=1, sticky="news")
            sn17 = Button(rp2, text="Pav bhaji \n Price:160", padx=50, pady=50)
            sn17.config(command=lambda d14=sn17: cv(d14))
            sn17.grid(row=4, column=2, sticky="news")
            sn18 = Button(rp2, text="Masala puri \n Price:160", padx=50, pady=50)
            sn18.config(command=lambda d15=sn18: cv(d15))
            sn18.grid(row=4, column=3, sticky="news")
            sn19 = Button(rp2, text="Veg cutlet \n Price:160", padx=50, pady=50)
            sn19.config(command=lambda d16=sn19: cv(d16))
            sn19.grid(row=4, column=4, sticky="news")
            sn20 = Button(rp2, text="coca cola \n Price:100", padx=50, pady=50)
            sn20.config(command=lambda d17=sn20: cv(d17))
            sn20.grid(row=4, column=5, sticky="news")

            rp2.grid_columnconfigure(0, weight=1)
            rp2.grid_columnconfigure(1, weight=1)
            rp2.grid_columnconfigure(2, weight=1)
            rp2.grid_columnconfigure(3, weight=1)
            rp2.grid_columnconfigure(4, weight=1)
            rp2.grid_columnconfigure(5, weight=1)



        rp = tk.Tk()
        rp.geometry("700x400")
        rp.resizable(0, 0)
        rp.title("Pick a show (Select seats)")
        l = Label(rp, text="Available seats:")
        l.grid(row=0, column=0)
        l1 = Label(rp, text="Red=Booked seats,Green=Selected seats")
        l1.grid(row=1, column=0)
        n = Button(rp, text="Next", command=dw)
        n.grid(row=1, column=99)


        for x in range(3, 9):
            for y in range(2, 14):
                def pri(bxy):
                    global price
                    global sno
                    global c
                    c += 1

                    price += 220

                    bxy.configure(bg="green")
                bxy = Button(rp, text=str(x - 1) + '.' + str(y - 2), padx=2, pady=2)
                bxy.config(command=lambda x=bxy: pri(x))
                bxy.grid(row=x, column=y, sticky="news")


        for x1 in range(9, 12):
            for y1 in range(2, 14):
                bxy1 = Button(rp, padx=2, pady=2, bg="red", state=DISABLED)
                bxy1.grid(row=x1, column=y1, sticky="news")


        nx1 = Label(rp, text="-------------------------------------------------")

        nx1.grid(row=14, sticky="news")
        nx2 = Label(rp, text="Screen this way")
        nx2.grid(row=15, sticky="news")

    def sel(ax1):
        global ax

        ax1 = vara.get()
        ax = ax1
        drop.config(vara.set(ax))

    def sele(ax2):
        global axe

        ax2 = vari.get()
        axe = ax2
        drop1.config(vari.set(axe))

    def tro(a1):
        a1 = x.get(x)
        a = a1

    def click(event):
        x.configure(state=NORMAL)
        x.delete(0, END)
        x.unbind('<Button-1>', clicked)





    x = Entry(roott, text="Enter the date", width=30, borderwidth=4)
    axy = x.get()
    axyx = axy
    a = x.get()
    x.grid(row=0, column=8, sticky="news", columnspan=3)
    y = Label(rtt, text=" ")
    y.grid(row=3, columnspan=3)





    # Create a dropdown Menu
    vara = StringVar()

    vari = StringVar()
    quani = StringVar()
    drop = OptionMenu(roott, vara, "8:00", "9:30", "10:45", "11:30", "12:45", "1:30", "2:15", "4:30", '6:45', '8:30',
                 "9:15", '11:30')

    label_date=Label(roott,text="Date(DD/MM/YYYY)")
    label_date.grid(row=0,column=0)
    label_venue = Label(roott, text="Venue")
    label_venue.grid(row=4, column=0)
    label_time = Label(roott, text="Time")
    label_time.grid(row=3, column=0)
    label_quan = Label(roott, text="Quantity")
    label_quan.grid(row=5   , column=0)
    ax = vara.get()
    drop.grid(row=3, column=8,columnspan=3, sticky="nw")
    drop1 = OptionMenu(roott, vari, "PVR (Ampa)", "PVR (VR)", "SPI (Escape)", "SPI (Pallazo)", "AGS (Navlur)",
                       "INOX (Citi Centre)", "Rohini", "Sathyam", "Rohini", "PVR (Grand Gallada)")
    axe = vari.get()
    drop1.grid(row=4, column=8, sticky="nw")
    quan = OptionMenu(roott, quani, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    quan.grid(row=5, column=8, sticky="nw")

    xy = Button(roott, text="Book Tickets", padx=300, pady=5, fg="black", bg="white", command=chh)
    xy.grid(row=100, column=8, sticky="news")

    roott.grid_columnconfigure(0, weight=1)
    roott.grid_columnconfigure(1, weight=1)
    roott.grid_columnconfigure(2, weight=1)
    roott.grid_columnconfigure(3, weight=1)
    roott.grid_columnconfigure(4, weight=1)
    roott.grid_columnconfigure(5, weight=1)
    roott.grid_columnconfigure(6, weight=1)
    roott.grid_columnconfigure(7, weight=1)
    roott.grid_columnconfigure(8, weight=1)
    roott.grid_columnconfigure(9, weight=1)
    roott.grid_columnconfigure(10, weight=1)
    roott.grid_columnconfigure(11, weight=1)
    roott.grid_columnconfigure(12, weight=1)



def autofill():
    def update(data):
        my_lst.delete(0, END)
        for items in data:
            my_lst.insert(END, items)

    def fillout(e):
        search.delete(0, END)
        search.insert(0, my_lst.get(ACTIVE))

    def check(e):
        typed = search.get()
        if typed == "":
            data = movies
        else:
            data = []
            for items in movies:
                if typed.lower() in items.lower():
                    data.append(items)
        update(data)

    def search_func():
        movsearch = search.get()
        if search.get() == "Vikram":
            v(vikram)
        if search.get() == "Varisu":
            v(varisu)
        if search.get() == "Sita Raman":
            v(sr)
        if search.get() == "Naane Varuven":
            v(nv)
        if search.get() == "Ponniyan Selvan":
            v(ps)
        if search.get() == "Cobra":
            v(cr)
        if search.get() == "Vendhu Thanindhidhu Kadu":
            v(vt)
        if search.get() == "Thiruchithrambalam":
            v(th)
        if search.get() == "Brahmasthra":
            v(br)
        if search.get() == "Sinam":
            v(sno)
        if search.get() == "Aadhar":
            v(aa)
        if search.get() == "Rendagam":
            v(re)
        if search.get() == "Kanam":
            v(kn)
        if search.get() == "Diary":
            v(dr)
        if search.get() == "Trigger":
            v(tr)

    root2 = Tk()
    root2.title("SEARCH")
    root2.geometry("350x250")
    root2.resizable(0, 0)

    search = Entry(root2, width=40, borderwidth=3)
    search.grid(row=0, column=0, columnspan=5)
    find_button = Button(root2, text="SEARCH", command=search_func)
    find_button.grid(row=0, column=2)

    my_lst = Listbox(root2, width=40)
    my_lst.grid()

    update(movies)
    my_lst.bind("<<ListboxSelect>>", fillout)
    search.bind("<KeyRelease>", check)


search_canvas = Canvas(root)
search_canvas.pack()
# scrollbar

# frame inside canvas
r = Frame(search_canvas)
r.pack()

# config scrollbar
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

# navigation

search_button = Button(r, text="Search", command=autofill, width=1, height=1, bg="black", fg="white")
search_button.grid(row=3, column=0,columnspan=3  ,sticky="ewns")
#my_bookings = Button(r, text="My Bookings", bg="black", fg="white")
#my_bookings.grid(row=3, column=2, sticky="ewns")

# main label
l = Label(r, text="PICK A SHOW ", font=("gobold", 40), padx=600, pady=3, bg="black", fg="white")
l.grid(row=0, columnspan=5)

# image



# movie names
vikram = Button(second_frame, text="Vikram", padx=250, pady=100, bg="black", fg="white", )
vikram.config(command=lambda g=vikram: v(vikram))
vikram.configure()
vikram.grid(row=2, column=0, stick="ewns")
varisu = Button(second_frame, text="Varisu", padx=250, pady=100, bg="black", fg="white", )
varisu.config(command=lambda x=varisu: v(varisu))
varisu.grid(row=2, column=1, sticky="ewns")
ps = Button(second_frame, text="Ponniyan selvan", padx=250, pady=100, fg="white", bg="black", )
ps.config(command=lambda x=ps: v(ps))
ps.grid(row=2, column=2 , sticky="ewns")
nv = Button(second_frame, text="Naane Varuven", padx=100, pady=100, fg="white", bg="black",)
nv.config(command=lambda x=nv: v(nv))
nv.grid(row=4, column=0, sticky="ewns")
tr = Button(second_frame, text="Trigger", padx=100, pady=100, fg="white", bg="black",)
tr.config(command=lambda x=tr: v(tr))
tr.grid(row=4, column=1, sticky="ewns")
vt = Button(second_frame, text="Vendhu Thanindhidhu Kadu", padx=100, pady=100, fg="white", bg="black",)
vt.config(command=lambda x=vt: v(vt))
vt.grid(row=4, column=2, sticky="ewns")
sno = Button(second_frame, text="Sinam", padx=100, pady=100, fg="white", bg="black")
sno.config(command=lambda x=sno: v(sno))
sno.grid(row=6, column=0, sticky="ewns")
sr = Button(second_frame, text="Sita Raman", padx=100, pady=100, fg="white", bg="black",)
sr.config(command=lambda x=sr: v(sr))
sr.grid(row=6, column=0, sticky="ewns")
br = Button(second_frame, text="Brahmasthram", padx=100, pady=100, fg="white", bg="black",)
br.config(command=lambda x=br: v(br))
br.grid(row=6, column=1, sticky="ewns")
aa = Button(second_frame, text="Aadhar", padx=100, pady=100, fg="white", bg="black",)
aa.config(command=lambda x=aa: v(aa))
aa.grid(row=6, column=2, sticky="ewns")
re = Button(second_frame, text="Rendagm", padx=100, pady=100, fg="white", bg="black")
re.config(command=lambda x=re: v(re))
re.grid(row=8, column=0, sticky="ewns")
th = Button(second_frame, text="Thiruchithrambalam", padx=100, pady=100, fg="white", bg="black",)
th.config(command=lambda x=th: v(th))
th.grid(row=8, column=1, sticky="ewns")
dr = Button(second_frame, text="Diary", padx=100, pady=100, fg="white", bg="black",)
dr.config(command=lambda x=dr: v(dr))
dr.grid(row=8, column=2, sticky="ewns")
kn = Button(second_frame, text="Kanam", padx=100, pady=100, fg="white", bg="black")
kn.config(command=lambda x=kn: v(kn))
kn.grid(row=10, column=0, sticky="ewns")
cr = Button(second_frame, text="Cobra", padx=100, pady=100, fg="white", bg="black",)
cr.config(command=lambda x=cr: v(cr))
cr.grid(row=10, column=1, sticky="ewns")
vv = Button(second_frame, text="Vikram Vedha", padx=100, pady=100, fg="white", bg="black")
vv.config(command=lambda x=vv: v(vv))
vv.grid(row=10, column=2, sticky="ewns")

# create a scrollbar widget and set its command to the text widget


r.grid_columnconfigure(0, weight=1)
r.grid_columnconfigure(1, weight=1)
r.grid_columnconfigure(2, weight=1)

root.mainloop()
