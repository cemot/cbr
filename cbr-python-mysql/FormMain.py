from PyQt5 import QtCore,QtGui,QtWidgets
rkB=super
rkV=True
rkd=False
rku=QtWidgets.QApplication
rkH=QtWidgets.QAction
rkT=QtWidgets.QStatusBar
rkh=QtWidgets.QMenu
rkl=QtWidgets.QMenuBar
rkE=QtWidgets.QWidget
rki=QtWidgets.QMainWindow
rkW=QtCore.QCoreApplication
rkc=QtCore.QMetaObject
rkp=QtCore.QRect
import sys
rkz=sys.exit
rkM=sys.argv
import pymysql
from TdkRlks import*
from Ageltrs import*
from KreOeYu import*
from DhlkRks import*
from UrdhEd import*
from BcEdGhr import*
rkC='127.0.0.1'
rkb='root'
rkG=''
rkw='db_cbr_python'
rkx='admin'
class rkI(rki):
 def __init__(rkt):
  super().__init__()
  rkt.rkm(rkt)
 def rkm(rkt,rkI):
  rkI.setObjectName("FormMain")
  rkI.resize(800,520)
  rkt.centralwidget=rkE(rkI)
  rkt.centralwidget.setObjectName("centralwidget")
  rkI.setCentralWidget(rkt.centralwidget)
  rkt.dfDSdfSSD=rkl(rkI)
  rkt.dfDSdfSSD.setGeometry(rkp(0,0,800,21))
  rkt.dfDSdfSSD.setObjectName("dfDSdfSSD")
  rkt.jdjRTKjsd=rkh(rkt.dfDSdfSSD)
  rkt.jdjRTKjsd.setObjectName("jdjRTKjsd")
  rkt.dSdDfSDF=rkh(rkt.dfDSdfSSD)
  rkt.dSdDfSDF.setObjectName("dSdDfSDF")
  rkt.kjsKJEjsa=rkh(rkt.dfDSdfSSD)
  rkt.kjsKJEjsa.setObjectName("kjsKJEjsa")
  rkt.mmdnSKJdf=rkh(rkt.dfDSdfSSD)
  rkt.mmdnSKJdf.setObjectName("mmdnSKJdf")
  rkI.setMenuBar(rkt.dfDSdfSSD)
  rkt.zzxSdxx=rkT(rkI)
  rkt.zzxSdxx.setObjectName("zzxSdxx")
  rkI.setStatusBar(rkt.zzxSdxx)
  rkt.kjdKJSKJd=rkH(rkI)
  rkt.kjdKJSKJd.setObjectName("kjdKJSKJd")
  rkt.ccMMssDF=rkH(rkI)
  rkt.ccMMssDF.setObjectName("ccMMssDF")
  rkt.XccSxnDf=rkH(rkI)
  rkt.XccSxnDf.setObjectName("XccSxnDf")
  rkt.DnDndDDD=rkH(rkI)
  rkt.DnDndDDD.setObjectName("DnDndDDD")
  rkt.lKSlkdSKD=rkH(rkI)
  rkt.lKSlkdSKD.setObjectName("lKSlkdSKD")
  rkt.dskKJDff=rkH(rkI)
  rkt.dskKJDff.setObjectName("dskKJDff")
  rkt.uuUkejsE=rkH(rkI)
  rkt.uuUkejsE.setObjectName("uuUkejsE")
  rkt.ooOweasd=rkH(rkI)
  rkt.ooOweasd.setObjectName("ooOweasd")
  rkt.uiweJKSD=rkH(rkI)
  rkt.uiweJKSD.setObjectName("uiweJKSD")
  rkt.jdjRTKjsd.addAction(rkt.kjdKJSKJd)
  rkt.jdjRTKjsd.addAction(rkt.ccMMssDF)
  rkt.jdjRTKjsd.addAction(rkt.XccSxnDf)
  rkt.dSdDfSDF.addAction(rkt.dskKJDff)
  rkt.dSdDfSDF.addAction(rkt.uuUkejsE)
  rkt.dSdDfSDF.addAction(rkt.ooOweasd)
  rkt.kjsKJEjsa.addAction(rkt.lKSlkdSKD)
  rkt.mmdnSKJdf.addAction(rkt.uiweJKSD)
  rkt.dfDSdfSSD.addAction(rkt.jdjRTKjsd.menuAction())
  rkt.dfDSdfSSD.addAction(rkt.dSdDfSDF.menuAction())
  rkt.dfDSdfSSD.addAction(rkt.mmdnSKJdf.menuAction())
  rkt.dfDSdfSSD.addAction(rkt.kjsKJEjsa.menuAction())
  rkt.dskKJDff.triggered.connect(rkt.rko)
  rkt.ooOweasd.triggered.connect(rkt.rkK)
  rkt.uuUkejsE.triggered.connect(rkt.rkU)
  rkt.uiweJKSD.triggered.connect(rkt.rkv)
  rkt.kjdKJSKJd.triggered.connect(rkt.rkn)
  rkt.ccMMssDF.triggered.connect(rkt.rkN)
  rkt.XccSxnDf.triggered.connect(rkt.rkA)
  rkt.lKSlkdSKD.triggered.connect(rkt.rky)
  rkt.rka(rkI)
  rkc.connectSlotsByName(rkI)
 def rka(rkt,rkI):
  rks=rkW.translate
  rkI.setWindowTitle(rks("FormMain","Sistem Pakar Metode Case Based Reasoning (CBR) - http://contohprogram.com"))
  rkt.jdjRTKjsd.setTitle(rks("FormMain","Utility"))
  rkt.dSdDfSDF.setTitle(rks("FormMain","Data"))
  rkt.kjsKJEjsa.setTitle(rks("FormMain","Keluar"))
  rkt.mmdnSKJdf.setTitle(rks("FormMain","Sistem Pakar"))
  rkt.kjdKJSKJd.setText(rks("FormMain","Login"))
  rkt.ccMMssDF.setText(rks("FormMain","Logout"))
  rkt.XccSxnDf.setText(rks("FormMain","Ganti Password"))
  rkt.lKSlkdSKD.setText(rks("FormMain","Keluar"))
  rkt.dskKJDff.setText(rks("FormMain","Data Penyakit"))
  rkt.uuUkejsE.setText(rks("FormMain","Data Gejala"))
  rkt.ooOweasd.setText(rks("FormMain","Data Basis Kasus"))
  rkt.uiweJKSD.setText(rks("FormMain","Konsultasi Sistem Pakar CBR"))
  rkt.kjdKJSKJd.setEnabled(rkV)
  rkt.XccSxnDf.setEnabled(rkd)
  rkt.ccMMssDF.setEnabled(rkd)
  rkt.dskKJDff.setEnabled(rkd)
  rkt.uuUkejsE.setEnabled(rkd)
  rkt.ooOweasd.setEnabled(rkd)
  rkt.show()
 def rko(rkt):
  rkt.TdkRlks=TdkRlks()
  rkt.TdkRlks.show()
 def rkU(rkt):
  rkt.Ageltrs=Ageltrs()
  rkt.Ageltrs.show()
 def rkn(rkt):
  rkt.DhlkRks=DhlkRks()
  rkt.DhlkRks.fMain=rkt
  rkt.DhlkRks.show()
  pass
 def rkN(rkt):
  print('ok bos')
  rkI.username_login=''
  #rkx=''
  rkt.kjdKJSKJd.setEnabled(True)
  rkt.XccSxnDf.setEnabled(False)
  rkt.ccMMssDF.setEnabled(False)
  rkt.dskKJDff.setEnabled(False)
  rkt.uuUkejsE.setEnabled(False)
  rkt.ooOweasd.setEnabled(False)
 def rkA(rkt):
  rkt.UrdhEd=UrdhEd()
  rkt.UrdhEd.show()
 def rkK(rkt):
  rkt.KreOeYu=KreOeYu()
  rkt.KreOeYu.show()
 def rkv(rkt):
  rkt.BcEdGhr=BcEdGhr()
  rkt.BcEdGhr.show()
 def rky(rkt):
  rkt.close()
if __name__=='__main__':
 rkj=rku(rkM)
 ex=rkI()
 rkz(rkj.exec())
