from PyQt6.QtWidgets import QApplication, QDialog, QStackedWidget 
from PyQt6.QtGui import QIcon
from PyQt6.uic import loadUi  # type: ignore
import os
import pygame
import webbrowser
import sys

print("Hello world")
pygame.mixer.init()

class main(QDialog):
    def __init__(self):
        super(main, self).__init__()
        loadUi("ui_files/New_app.ui", self)
        self.Settings.clicked.connect(self.gotosett)   # type: ignore
        self.Home.clicked.connect(self.gotohome)  #type: ignore
        self.listtomus.clicked.connect(self.gotomusic)  #type: ignore
        self.song_dist.clicked.connect(self.gotodist)  #type: ignore
        self.make_song.clicked.connect(self.gotosong) #type: ignore
    
    def gotosong(self):
        home2 = makesong()
        widget.addWidget(home2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotodist(self):
        home1 = distribute()
        widget.addWidget(home1)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def gotosett(self):
        win2 = settings()
        widget.addWidget(win2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotohome(self):
        widget.addWidget(win)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotomusic(self):
        win3 = music()
        widget.addWidget(win3)
        widget.setCurrentIndex(widget.currentIndex()+1)

class makesong(QDialog):
    def __init__(self):
        super(makesong, self).__init__()
        loadUi("ui_files/New_app_makesongs.ui", self)
        self.Settings.clicked.connect(self.gotosett)   # type: ignore
        self.Home.clicked.connect(self.gotohome)  #type: ignore
        self.listtomus.clicked.connect(self.gotomusic)  #type: ignore
        self.goback.clicked.connect(self.gotohome) #type: ignore
        self.garageband.clicked.connect(self.gotogarage) #type: ignore
        self.flstudio.clicked.connect(self.gotofl) #type:ignore
        self.audacity.clicked.connect(self.gotoaud) #type: ignore

    def gotoaud(self):
        webbrowser.open("https://www.audacityteam.org")

    def gotofl(self):
        webbrowser.open("https://www.image-line.com")

    def gotogarage(self):
        webbrowser.open("https://www.apple.com/in/mac/garageband/")

    def gotosett(self):
        win2 = settings()
        widget.addWidget(win2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotohome(self):
        widget.addWidget(win)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotomusic(self):
        win3 = music()
        widget.addWidget(win3)
        widget.setCurrentIndex(widget.currentIndex()+1)

class distribute(QDialog):
    def __init__(self):
        super(distribute, self).__init__()
        loadUi("ui_files/New_app_homesongdist.ui", self)
        self.Settings.clicked.connect(self.gotosett)   # type: ignore
        self.Home.clicked.connect(self.gotohome)  #type: ignore
        self.listtomus.clicked.connect(self.gotomusic)  #type: ignore
        self.cdbaby.clicked.connect(self.gotocdbaby)  #type: ignore
        self.tunecore.clicked.connect(self.gototunecore)  #type: ignore
        self.distrokid.clicked.connect(self.gotokid) #type: ignore
        self.goback.clicked.connect(self.gotohome) #type: ignore

    def gotokid(self):
        webbrowser.open("https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiEvbzO2oD-AhXamWYCHWf_BuoYABAAGgJzbQ&ae=2&ohost=www.google.com&cid=CAESa-D2DCqdqnz5boE8eX8W-hB52WZWbtUb_X3Zs8ZUSblrKej4nGNVU5p03i2402WrwncnZtJFREHs5m8017joF-RmmiXW0-u1PkkR5sSjnaOSNQjKL4h_xLk0l8Ma9ahNJh2PshTDN45VvaPo&sig=AOD64_3Z0CRu8dofRrVZio6ki_wZEAZJTg&q&adurl&ved=2ahUKEwijirbO2oD-AhV8XWwGHec0BRAQ0Qx6BAgIEAE")

    def gototunecore(self):
        webbrowser.open("https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiQrszE2oD-AhXBRysKHdQSCK4YABABGgJzZg&ae=2&ohost=www.google.com&cid=CAESa-D2zX20c1wpmx2mlRuwvN87Jfz4CPBSUueM2VN2h70ur2xko7xzflN7I9P7QIvfcSWKn47t3rnVsx0gcM95NnvbdBeZ7cCJCaRvU3DNe9dYN1XEzgiqi59XFPTTgXivXVco6Q9H5OazTBHQ&sig=AOD64_01MCwPTvsATKVRcL6oZSnnE2PNsQ&q&adurl&ved=2ahUKEwiV28XE2oD-AhVZSmwGHQsCDjoQ0Qx6BAgLEAE")
    
    def gotocdbaby(self):
        webbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjdlJrx2YD-AhWHTmwGHSwqCMMQFnoECBYQAQ&url=https%3A%2F%2Fcdbaby.com%2F&usg=AOvVaw3yrCqSksbNS7YOGk6C4qvM")

    def gotosett(self):
        win2 = settings()
        widget.addWidget(win2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotohome(self):
        widget.addWidget(win)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotomusic(self):
        win3 = music()
        widget.addWidget(win3)
        widget.setCurrentIndex(widget.currentIndex()+1)

class settings(QDialog):
    def __init__(self):
        super(settings, self).__init__()
        loadUi("ui_files/New_app_settings.ui", self)
        self.Settings.clicked.connect(self.gotosett)   # type: ignore
        self.Home.clicked.connect(self.gotohome)  #type: ignore
        self.listtomus.clicked.connect(self.gotomusic)  #type: ignore
        self.gotoweb.clicked.connect(self.goingtoweb) #type: ignore
        #self.download.clicked.connect(self.downloadupdate) #type: ignore
        self.readme.clicked.connect(self.openreadme) #type:ignore

    def openreadme(self):
        os.system("open README.txt")
    
    def downloadupdate(self):
        webbrowser.open("")

    def goingtoweb(self):
        webbrowser.open("https://sunnycreations.netlify.app")

    def gotosett(self):
        win2 = settings()
        widget.addWidget(win2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotohome(self):
        widget.addWidget(win)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotomusic(self):
        win3 = music()
        widget.addWidget(win3)
        widget.setCurrentIndex(widget.currentIndex()+1)

class music(QDialog):
    def __init__(self):
        super(music, self).__init__()
        loadUi("ui_files/New_app_music.ui", self)
        self.Settings.clicked.connect(self.gotosett)   # type: ignore
        self.Home.clicked.connect(self.gotohome)  #type: ignore
        self.listtomus.clicked.connect(self.gotomusic)  #type: ignore
        self.spotify.clicked.connect(self.gotospotify) #type: ignore
        self.applemusic.clicked.connect(self.gotoapplemusic) #type: ignore
        self.wynkmusic.clicked.connect(self.gotowynk) #type: ignore
        self.soundcloud.clicked.connect(self.gotocloud) #type: ignore
        self.play.clicked.connect(self.playsong) #type: ignore
        self.pause.clicked.connect(self.pausesong) #type: ignore
        self.resume.clicked.connect(self.resumesong) #type: ignore
        self.stop.clicked.connect(self.stopsong) #type: ignore

    def resumesong(self):
        pygame.mixer.music.unpause()

    def stopsong(self):
        pygame.mixer.music.stop()

    def pausesong(self):
        pygame.mixer.music.pause()

    def playsong(self):
        pygame.mixer.music.load("Naatu_Naatu.mp3")
        pygame.mixer.music.play(loops=0)

    def gotocloud(self):
        webbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjf_fKC7v79AhViSGwGHZ_1BLQQFnoECBYQAQ&url=https%3A%2F%2Fsoundcloud.com%2F&usg=AOvVaw0RlACYKHs09PlpF_cS2U96")

    def gotowynk(self):
        webbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwj-wq_s7f79AhWWUGwGHfntCAYQFnoECA4QAQ&url=https%3A%2F%2Fwynk.in%2Fmusic&usg=AOvVaw3YBj8P8VNJxzxsquFnmbNn")

    def gotoapplemusic(self):
        webbrowser.open("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiyzN3J7f79AhUyTmwGHe70DvgQFnoECCQQAQ&url=https%3A%2F%2Fmusic.apple.com%2Fus%2Fbrowse&usg=AOvVaw2A2i_8kt3IkaFWvHo-4y_L")

    def gotospotify(self):
        webbrowser.open("https://open.spotify.com/?")

    def gotosett(self):
        win2 = settings()
        widget.addWidget(win2)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotohome(self):
        widget.addWidget(win)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotomusic(self):
        win3 = music()
        widget.addWidget(win3)
        widget.setCurrentIndex(widget.currentIndex()+1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = main()
    widget = QStackedWidget()
    widget.addWidget(win)
    widget.setWindowTitle("MeMusic")
    widget.setWindowIcon(QIcon("images/icon.png"))
    widget.setFixedHeight(362)
    widget.setFixedWidth(652)
    widget.show()
    sys.exit(app.exec())