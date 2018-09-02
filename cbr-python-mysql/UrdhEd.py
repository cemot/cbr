from PyQt5 import QtCore,QtGui,QtWidgets
vjW=super
vjp=print
vjM=QtWidgets.QApplication
vjP=QtWidgets.QMessageBox
vjE=QtWidgets.QPushButton
vjs=QtWidgets.QLabel
vjf=QtWidgets.QLineEdit
vji=QtWidgets.QMainWindow
vjS=QtCore.QCoreApplication
vjG=QtCore.QMetaObject
vjt=QtCore.QRect
wek=QtWidgets.QMessageBox
import sys
vjz=sys.exit
vjh=sys.argv
import pymysql
vjX=pymysql.connect
import FormMain
vjV='db_cbr_python'
vjQ=''
vjr='root'
vjK='127.0.0.1'
vjO='admin'
class UrdhEd(vji):
 def __init__(vjk):
  super().__init__()
  vjk.vjw(vjk)
 def vjw(vjk,UrdhEd):
  UrdhEd.setObjectName("UrdhEd")
  UrdhEd.resize(293,177)
  vjk.kjdsiwFsd=vjf(UrdhEd)
  vjk.kjdsiwFsd.setGeometry(vjt(130,20,141,20))
  vjk.kjdsiwFsd.setObjectName("kjdsiwFsd")
  vjk.dEkjWEKJ=vjs(UrdhEd)
  vjk.dEkjWEKJ.setGeometry(vjt(20,20,61,16))
  vjk.dEkjWEKJ.setObjectName("dEkjWEKJ")
  vjk.rERfdfDE=vjs(UrdhEd)
  vjk.rERfdfDE.setGeometry(vjt(20,50,91,16))
  vjk.rERfdfDE.setObjectName("rERfdfDE")
  vjk.oiIRjWEt=vjE(UrdhEd)
  vjk.oiIRjWEt.setGeometry(vjt(20,140,75,23))
  vjk.oiIRjWEt.setObjectName("oiIRjWEt")
  vjk.OKEjUHS=vjE(UrdhEd)
  vjk.OKEjUHS.setGeometry(vjt(200,140,75,23))
  vjk.OKEjUHS.setObjectName("OKEjUHS")
  vjk.kJDSDft=vjf(UrdhEd)
  vjk.kJDSDft.setGeometry(vjt(130,50,141,20))
  vjk.kJDSDft.setInputMask("")
  vjk.kJDSDft.setObjectName("kJDSDft")
  vjk.klksdRT=vjs(UrdhEd)
  vjk.klksdRT.setGeometry(vjt(20,110,101,16))
  vjk.klksdRT.setObjectName("klksdRT")
  vjk.ooORkjwes=vjf(UrdhEd)
  vjk.ooORkjwes.setGeometry(vjt(130,80,141,20))
  vjk.ooORkjwes.setObjectName("ooORkjwes")
  vjk.xXALJRD=vjs(UrdhEd)
  vjk.xXALJRD.setGeometry(vjt(20,80,91,16))
  vjk.xXALJRD.setObjectName("xXALJRD")
  vjk.kKRFGwe=vjf(UrdhEd)
  vjk.kKRFGwe.setGeometry(vjt(130,110,141,20))
  vjk.kKRFGwe.setInputMask("")
  vjk.kKRFGwe.setObjectName("kKRFGwe")
  vjk.oiIRjWEt.clicked.connect(vjk.vjN)
  vjk.OKEjUHS.clicked.connect(vjk.vjY)
  vjk.vje(UrdhEd)
  vjG.connectSlotsByName(UrdhEd)
 def vje(vjk,UrdhEd):
  vjg=vjS.translate
  UrdhEd.setWindowTitle(vjg("UrdhEd","Ganti Password"))
  vjk.dEkjWEKJ.setText(vjg("UrdhEd","Username"))
  vjk.rERfdfDE.setText(vjg("UrdhEd","Password Lama"))
  vjk.oiIRjWEt.setText(vjg("UrdhEd","Update"))
  vjk.OKEjUHS.setText(vjg("UrdhEd","Cancel"))
  vjk.klksdRT.setText(vjg("UrdhEd","Konfirmasi Password"))
  vjk.xXALJRD.setText(vjg("UrdhEd","Password Baru"))
  vjk.show()
  vjk.kjdsiwFsd.setText(vjO)
 def vjN(vjk):
  db=vjX(vjK,vjr,vjQ,vjV)
  vjD=db.cursor()
  vjC="SELECT * FROM `login` WHERE `username` = '%s' AND `password` = '%s'"%(vjO,vjk.kJDSDft.text()) 
  vjD.execute(vjC)
  vjo=vjD.fetchall()
  if vjo:
   if vjk.ooORkjwes.text()==vjk.kKRFGwe.text():
    weN = wek()
    weN.setIcon(wek.Information)
    weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
    weN.setWindowTitle("Peringatan")
    weN.setStandardButtons(wek.Ok)
    wer = weN.exec_()
    vjk.close()
   else:
    vjH=vjP()
    vjH.setIcon(vjP.Information)
    vjH.setText("Password Baru Tidak Sama")
    vjH.setWindowTitle("Peringatan")
    vjH.setStandardButtons(vjP.Ok)
    vjb=vjH.exec_()
  else:
   vjH=vjP()
   vjH.setIcon(vjP.Information)
   vjH.setText("Password Lama Salah")
   vjH.setWindowTitle("Peringatan")
   vjH.setStandardButtons(vjP.Ok)
   vjb=vjH.exec_()
   vjp("gagal")
  db.close()
 def vjY(vjk):
  vjk.close()
if __name__=='__main__':
 vjm=vjM(vjh)
 ex=UrdhEd()
 vjz(vjm.exec())
# Created by pyminifier (https://github.com/liftoff/pyminifier)
