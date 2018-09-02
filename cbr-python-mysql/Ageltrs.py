from PyQt5 import QtCore,QtGui,QtWidgets
JlU=super
Jlb=len
JlI=str
Jla=print
JlR=int
Jln=QtWidgets.QApplication
Jly=QtWidgets.QTableWidgetItem
Jls=QtWidgets.QPushButton
JlS=QtWidgets.QTableWidget
JlB=QtWidgets.QLabel
Jlq=QtWidgets.QLineEdit
JlH=QtWidgets.QMainWindow
Jlu=QtCore.QCoreApplication
Jlw=QtCore.QMetaObject
Jlj=QtCore.QRect
wek=QtWidgets.QMessageBox
import sys
Jlz=sys.exit
JlK=sys.argv
import pymysql
Jlh=pymysql.connect
import FormMain
JlY='db_cbr_python'
JlX=''
JlN='root'
Jli='127.0.0.1'
class Ageltrs(JlH):
 def __init__(Jlc):
  super().__init__()
  Jlc.JlP(Jlc)
 def JlP(Jlc,Ageltrs):
  Ageltrs.setObjectName("Ageltrs")
  Ageltrs.resize(444,290)
  Jlc.JkseEr=Jlq(Ageltrs)
  Jlc.JkseEr.setGeometry(Jlj(160,20,261,20))
  Jlc.JkseEr.setObjectName("JkseEr")
  Jlc.SxxDrft=JlB(Ageltrs)
  Jlc.SxxDrft.setGeometry(Jlj(20,20,121,16))
  Jlc.SxxDrft.setObjectName("SxxDrft")
  Jlc.XdkRjd=JlS(Ageltrs)
  Jlc.XdkRjd.setGeometry(Jlj(20,60,401,180))
  Jlc.XdkRjd.setObjectName("XdkRjd")
  Jlc.XdkRjd.setColumnCount(0)
  Jlc.XdkRjd.setRowCount(0)
  Jlc.KlskJrd=Jls(Ageltrs)
  Jlc.KlskJrd.setGeometry(Jlj(20,250,75,23))
  Jlc.KlskJrd.setObjectName("KlskJrd")
  Jlc.iIrtlkw=Jls(Ageltrs)
  Jlc.iIrtlkw.setGeometry(Jlj(100,250,75,23))
  Jlc.iIrtlkw.setObjectName("iIrtlkw")
  Jlc.tRFEtge=Jls(Ageltrs)
  Jlc.tRFEtge.setGeometry(Jlj(180,250,75,23))
  Jlc.tRFEtge.setObjectName("tRFEtge")
  Jlc.RtiijdR=Jls(Ageltrs)
  Jlc.RtiijdR.setGeometry(Jlj(350,250,75,23))
  Jlc.RtiijdR.setObjectName("RtiijdR")
  Jlc.Jlo(Ageltrs)
  Jlc.KlskJrd.clicked.connect(Jlc.JlD)
  Jlc.iIrtlkw.clicked.connect(Jlc.Jlk)
  Jlc.RtiijdR.clicked.connect(Jlc.JlV)
  Jlc.tRFEtge.clicked.connect(Jlc.JlM)
  Jlw.connectSlotsByName(Ageltrs)
 def Jlo(Jlc,Ageltrs):
  Jlt=Jlu.translate
  Ageltrs.setWindowTitle(Jlt("Ageltrs","Data Gejala"))
  Jlc.SxxDrft.setText(Jlt("Ageltrs","Nama Gejala"))
  Jlc.KlskJrd.setText(Jlt("Ageltrs","Insert"))
  Jlc.iIrtlkw.setText(Jlt("Ageltrs","Update"))
  Jlc.tRFEtge.setText(Jlt("Ageltrs","Clear"))
  Jlc.RtiijdR.setText(Jlt("Ageltrs","Delete"))
  Jlc.JlA()
  Jlc.show()
 def JlA(Jlc):
  db=Jlh(Jli,JlN,JlX,JlY)
  Jle=db.cursor()
  Jlm="SELECT * FROM gejala"
  try:
   Jle.execute(Jlm)
   Jlg=Jle.fetchall()
   Jlc.XdkRjd.setColumnCount(2)
   Jlc.XdkRjd.setRowCount(Jlb(Jlg)) 
   Jlc.XdkRjd.setHorizontalHeaderLabels(('Id Gejala','Nama Gejala'))
   i=0
   Jlc.vheader=[]
   for Jlv in Jlg:
    Jlc.vheader.append('')
    Jlc.XdkRjd.setItem(i,0,Jly(JlI(Jlv[0])))
    Jlc.XdkRjd.setItem(i,1,Jly(Jlv[1]))
    i=i+1
   Jlc.id_gejala=""
   Jlc.XdkRjd.setVerticalHeaderLabels(Jlc.vheader)
   Jlc.XdkRjd.cellClicked.connect(Jlc.JlQ)
  except:
   Jla("Error: unable to fetch data")
  db.close()
 def JlQ(Jlc,Jlv,column):
  Jlc.id_gejala=Jlc.XdkRjd.item(JlR(Jlv),0).text()
  Jlc.JkseEr.setText(Jlc.XdkRjd.item(JlR(Jlv),1).text())
 def JlD(Jlc):
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
  Jlc.JlA()
 def Jlk(Jlc):
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
  Jlc.JlM()
  Jlc.JlA()
 def JlV(Jlc):
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
  Jlc.JlM()
  Jlc.JlA()
 def JlM(Jlc):
  Jlc.JkseEr.setText("")
if __name__=='__main__':
 JlW=Jln(JlK)
 ex=Ageltrs()
 Jlz(JlW.exec())
