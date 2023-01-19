from tkinter import *
window=Tk()
window.title("Weather app")
window.config(background="black")
window.geometry("260x580")

search_city=StringVar()
Label(window,text="WEATHER APP",bg="black",fg="white",font="none 30 bold").grid(row=0,column=0)
Label(window, text=" ",bg="black",fg="white",font="none 15 bold" ).grid(row=1,column=0)
enter_city=Entry(window, textvariable=search_city,bg="white",fg="black",font=("Comic Sans MS",16,"bold")).grid(row=2,column=0)
Label(window, text=" ",bg="black",fg="white",font="none 15 bold" ).grid(row=3,column=0)

search_button=Button(window,text='SEARCH WEATHER',width=10,bg="brown",fg="black",font=("none",10,"bold")).grid(row=2,column=2)
Label(window, text=" ",bg="black",fg="white",font="none 15 bold" ).grid(row=5,column=0)

location=Label(window,text='Bangalore',font=("\nComic Sans MS",30,"bold"),bg="brown").grid(row=6,column=0)
Label(window, text=" ",bg="black",fg="white",font="none 15 bold" ).grid(row=7,column=0)

temperature=Label(window,text='20 C',font=("\nComic Sans MS",30,"bold"),bg="brown").grid(row=10,column=0)
Label(window, text=" ",bg="black",fg="white",font="none 15 bold" ).grid(row=9,column=0)

weather=Label(window,text='Cloudy',font=("\nclearComic Sans MS",30,"bold"),bg="brown").grid(row=12,column=0)
Label(window, text=" ",bg="black",fg="white",font="none 15 bold" ).grid(row=11,column=0)

dandt=Label(window,text='Thursday',font=("\nclearComic Sans MS",30,"bold"),bg="brown").grid(row=8,column=0)
Label(window, text=" ",bg="black",fg="white",font="none 10 bold" ).grid(row=11,column=0)





window.mainloop()