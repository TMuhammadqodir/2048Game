import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from pyqtdesign import*
from random import randint
import PyQt5.QtCore 

class Game(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("2048 Game")
        self.alt=0
        self.count=0
        self.k1=self.k2=self.k3=self.k4=0
        self.ui.label.setAlignment(QtCore.Qt.AlignRight)
        self.ui.label.setText(str(self.count))
        self.ui.label.setStyleSheet("font-size: 30px; color: white; font: bold")
        self.ui.label_2.setText("")
        self.ui.label_2.setStyleSheet("font-size: 30px; color: white; font: bold")
        
        self.lis=[[self.ui.pushButton, self.ui.pushButton_2, self.ui.pushButton_3, self.ui.pushButton_4],
                  [self.ui.pushButton_5, self.ui.pushButton_6, self.ui.pushButton_7, self.ui.pushButton_8],
                  [self.ui.pushButton_9, self.ui.pushButton_10, self.ui.pushButton_11, self.ui.pushButton_12],
                  [self.ui.pushButton_13, self.ui.pushButton_14, self.ui.pushButton_15, self.ui.pushButton_16]]
        
        self.lis2=[([0]*4) for i in range(4)]
        for i in range(4):
            for j in range(4):
                self.lis2[i][j]=self.lis[j][i]
            
        self.lis[randint(0,3)][randint(0,3)].setText('2')
        self.ColorButton(self.lis)
           
    def keyPressEvent(self,event) -> None:
        n=event.key()
        if n==16777234:
            self.k1=self.LRHL_Button(self.lis,1)
            if not self.k1:
                self.k2=self.k3=self.k4=0
        elif n==16777236:
            self.k2=self.LRHL_Button(self.lis,0)
            if not self.k2:
                self.k1=self.k3=self.k4=0
        elif n==16777235:
            self.k3=self.LRHL_Button(self.lis2,1)
            if not self.k3:
                self.k1=self.k2=self.k4=0
        elif n==16777237:  
            self.k4=self.LRHL_Button(self.lis2,0)
            if not self.k4:
                self.k1=self.k2=self.k3=0
                
        self.ui.label.setText(str(self.count))
        self.ColorButton(self.lis)
        if self.k1+self.k2+self.k3+self.k4==4:
            self.ui.label_2.setText(str('GameOver!'))
            
    def LRHL_Button(self,lis,n):
        if n:
            m1,m2,m3=0,4,1
        else:
            m1,m2,m3=3,-1,-1
        answer=1
        check=0
        for i in range(m1,m2,m3):
                if n: j=1
                else: j=2
                while j<4 if n else j>-1:
                    t1=t2=t3=0
                    if lis[i][j].text()!='':
                        k=j
                        while k>0 if n else k<3:
                            if n: k-=1
                            else: k+=1
                            if lis[i][k].text()=='':
                                t1=1
                                break
                            elif lis[i][k].text()==lis[i][j].text() and t3==0:
                                t2=1
                                break
                            elif lis[i][k].text()!='':
                                t3=1    
                    if t1==1:
                        lis[i][k].setText(lis[i][j].text())
                        lis[i][j].setText('')
                        if n: j=k-1
                        else: j=k+1
                        check=1
                        answer=0
                    elif t2==1:
                        self.count+=int(lis[i][j].text())*2
                        lis[i][k].setText(str(int(lis[i][k].text())*2))
                        lis[i][j].setText('')
                        if n: j=k-1
                        else: j=k+1
                        check=1
                        answer=0
                    if n: j+=1
                    else: j-=1
        if check:
            self.RandomLocation()
        return answer
        
    def RandomLocation(self):
        dic=dict()
        k=0
        for i in range(4):
            for j in range(4):
                if self.lis[i][j].text()=='':
                    dic[k]=self.lis[i][j]
                    k+=1
        if len(dic)>0:
            dic[randint(0,k-1)].setText('2')
        
    def ColorButton(self, lis):
        for i in range(4):
            for j in range(4):
                
                if lis[i][j].text()=='2':
                    lis[i][j].setStyleSheet("background: #ACBE00; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='4':
                    lis[i][j].setStyleSheet("background: red; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='8':
                    lis[i][j].setStyleSheet("background: #21B307; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='16':
                    lis[i][j].setStyleSheet("background: #0216B9; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='32':
                    lis[i][j].setStyleSheet("background: #60075A; font-size: 30px; color: white; font: bold")      
                elif lis[i][j].text()=='64':
                    lis[i][j].setStyleSheet("background: #75018E; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='128':
                    lis[i][j].setStyleSheet("background: #00776B; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='256':
                    lis[i][j].setStyleSheet("background: #783100; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='512':
                    lis[i][j].setStyleSheet("background: #32026A; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='1024':
                    lis[i][j].setStyleSheet("background: #1C0D7A; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='2048':
                    lis[i][j].setStyleSheet("background: #ACBE00; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='4096':
                    lis[i][j].setStyleSheet("background: red; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='8192':
                    lis[i][j].setStyleSheet("background: #21B307; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='16384':
                    lis[i][j].setStyleSheet("background: #0216B9; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='32768':
                    lis[i][j].setStyleSheet("background: #60075A; font-size: 30px; color: white; font: bold")      
                elif lis[i][j].text()=='65536':
                    lis[i][j].setStyleSheet("background: #75018E; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='131072':
                    lis[i][j].setStyleSheet("background: #00776B; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='262144':
                    lis[i][j].setStyleSheet("background: #783100; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='524288':
                    lis[i][j].setStyleSheet("background: #32026A; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='1048576':
                    lis[i][j].setStyleSheet("background: #1C0D7A; font-size: 30px; color: white; font: bold")
                elif lis[i][j].text()=='':
                    lis[i][j].setStyleSheet("background: rgb(111, 209, 197); font-size: 30px; color: white; font: bold")
        
                    
app=QApplication([])
win=Game()
win.show()
sys.exit(app.exec_())
    