from PyQt5 import QtCore,QtGui,QtWidgets
Koi=super
KoC=str
KoS=print
KoD=len
KoO=int
KoR=False
Keo=range
KeF=True
Koh=QtWidgets.QApplication
KoJ=QtWidgets.QTableWidgetItem
Koc=QtWidgets.QAbstractItemView
Kow=QtWidgets.QListWidget
KoG=QtWidgets.QLineEdit
Kox=QtWidgets.QComboBox
Kov=QtWidgets.QPushButton
KoT=QtWidgets.QTableWidget
Kou=QtWidgets.QLabel
KoW=QtWidgets.QMainWindow
KoA=QtCore.Qt
KoU=QtCore.QCoreApplication
Kos=QtCore.QMetaObject
Kor=QtCore.QRect
wek=QtWidgets.QMessageBox
import sys
Kot=sys.exit
KoV=sys.argv
import pymysql
KoB=pymysql.connect
import FormMain
Koy='db_cbr_python'
Kol=''
Koa='root'
Kog='127.0.0.1'
class KreOeYu(KoW):
 def __init__(KoF):
  super().__init__()
  KoF.Kok(KoF)
 def Kok(KoF,KreOeYu):
  KreOeYu.setObjectName("KreOeYu")
  KreOeYu.resize(444,361)
  KoF.IUekJEDF=Kou(KreOeYu)
  KoF.IUekJEDF.setGeometry(Kor(20,80,121,16))
  KoF.IUekJEDF.setObjectName("IUekJEDF")
  KoF.UjUrjdi=Kou(KreOeYu)
  KoF.UjUrjdi.setGeometry(Kor(20,50,121,16))
  KoF.UjUrjdi.setObjectName("UjUrjdi")
  KoF.jJJerWT=KoT(KreOeYu)
  KoF.jJJerWT.setGeometry(Kor(20,190,401,121))
  KoF.jJJerWT.setObjectName("jJJerWT")
  KoF.jJJerWT.setColumnCount(0)
  KoF.jJJerWT.setRowCount(0)
  KoF.LOkDeerR=Kov(KreOeYu)
  KoF.LOkDeerR.setGeometry(Kor(20,320,75,23))
  KoF.LOkDeerR.setObjectName("LOkDeerR")
  KoF.yyULMqZ=Kov(KreOeYu)
  KoF.yyULMqZ.setGeometry(Kor(100,320,75,23))
  KoF.yyULMqZ.setObjectName("yyULMqZ")
  KoF.gGRhHFE=Kov(KreOeYu)
  KoF.gGRhHFE.setGeometry(Kor(180,320,75,23))
  KoF.gGRhHFE.setObjectName("gGRhHFE")
  KoF.JkALXRT=Kov(KreOeYu)
  KoF.JkALXRT.setGeometry(Kor(350,320,75,23))
  KoF.JkALXRT.setObjectName("JkALXRT")
  KoF.URYjdkED=Kox(KreOeYu)
  KoF.URYjdkED.setGeometry(Kor(160,50,261,22))
  KoF.URYjdkED.setObjectName("URYjdkED")
  KoF.URYjdkED.addItem("")
  KoF.URYjdkED.setItemText(0,"")
  KoF.jkruEEkd=Kou(KreOeYu)
  KoF.jkruEEkd.setGeometry(Kor(20,20,121,16))
  KoF.jkruEEkd.setObjectName("jkruEEkd")
  KoF.uUUjrfERQ=KoG(KreOeYu)
  KoF.uUUjrfERQ.setGeometry(Kor(160,20,261,20))
  KoF.uUUjrfERQ.setObjectName("uUUjrfERQ")
  KoF.GhgrEErT=Kow(KreOeYu)
  KoF.GhgrEErT.setGeometry(Kor(160,80,261,101))
  KoF.GhgrEErT.setSelectionMode(Koc.MultiSelection)
  KoF.GhgrEErT.setObjectName("GhgrEErT")
  KoF.Kof(KreOeYu)
  KoF.LOkDeerR.clicked.connect(KoF.KoY)
  KoF.yyULMqZ.clicked.connect(KoF.KoP)
  KoF.JkALXRT.clicked.connect(KoF.Koj)
  KoF.gGRhHFE.clicked.connect(KoF.Kop)
  Kos.connectSlotsByName(KreOeYu)
 def Kof(KoF,KreOeYu):
  Kon=KoU.translate
  KreOeYu.setWindowTitle(Kon("KreOeYu","Data Basis Kasus"))
  KoF.IUekJEDF.setText(Kon("KreOeYu","Gejala"))
  KoF.UjUrjdi.setText(Kon("KreOeYu","Penyakit"))
  KoF.LOkDeerR.setText(Kon("KreOeYu","Insert"))
  KoF.yyULMqZ.setText(Kon("KreOeYu","Update"))
  KoF.gGRhHFE.setText(Kon("KreOeYu","Clear"))
  KoF.JkALXRT.setText(Kon("KreOeYu","Delete"))
  KoF.jkruEEkd.setText(Kon("KreOeYu","Nomor Kasus"))
  KoF.show()
  KoF.KoI()
  KoF.KoX()
  KoF.KoN()
  KoF.show()
 def KoI(KoF):
  db=KoB(Kog,Koa,Kol,Koy)
  Kod=db.cursor()
  KoM="SELECT * FROM penyakit"
  KoF.list_id_penyakit=[]
  KoF.URYjdkED.clear()
  try:
   Kod.execute(KoM)
   Koq=Kod.fetchall()
   i=0
   for KoE in Koq:
    KoF.list_id_penyakit.append(KoC(KoE[0]))
    KoF.URYjdkED.addItem(KoE[1])
    i=i+1
  except:
   KoS("Error: unable to fetch data")
  db.close()
 def KoX(KoF):
  db=KoB(Kog,Koa,Kol,Koy)
  Kod=db.cursor()
  KoM="SELECT * FROM gejala"
  KoF.list_id_gejala=[]
  KoF.GhgrEErT.clear()
  try:
   Kod.execute(KoM)
   Koq=Kod.fetchall()
   i=0
   for KoE in Koq:
    KoF.list_id_gejala.append(KoC(KoE[0]))
    KoF.GhgrEErT.addItem(KoE[1])
    i=i+1
  except:
   KoS("Error: unable to fetch data")
  db.close()
 def KoN(KoF):
  db=KoB(Kog,Koa,Kol,Koy)
  Kod=db.cursor()
  KoM="SELECT basis_kasus.*, penyakit.nama_penyakit, gejala.nama_gejala FROM basis_kasus LEFT JOIN penyakit ON penyakit.id_penyakit = basis_kasus.id_penyakit LEFT JOIN gejala ON basis_kasus.id_gejala = gejala.id_gejala"
  KoF.list_no_basis_kasus=[]
  KoF.list_id_penyakit_basis_kasus=[]
  KoF.list_id_gejala_basis_kasus=[]
  try:
   Kod.execute(KoM)
   Koq=Kod.fetchall()
   KoF.jJJerWT.setColumnCount(4)
   KoF.jJJerWT.setRowCount(KoD(Koq)) 
   KoF.jJJerWT.setHorizontalHeaderLabels(('Id','No Basis Kasus','Penyakit','Gejala'))
   i=0
   KoF.vheader=[]
   for KoE in Koq:
    KoF.vheader.append('')
    KoF.list_no_basis_kasus.append(KoC(KoE[1]))
    KoF.list_id_penyakit_basis_kasus.append(KoC(KoE[2]))
    KoF.list_id_gejala_basis_kasus.append(KoC(KoE[3]))
    KoF.jJJerWT.setItem(i,0,KoJ(KoC(KoE[0])))
    KoF.jJJerWT.setItem(i,1,KoJ(KoC(KoE[1])))
    KoF.jJJerWT.setItem(i,2,KoJ(KoE[4]))
    KoF.jJJerWT.setItem(i,3,KoJ(KoE[5]))
    i=i+1
   KoF.id_basis_kasus=""
   KoF.jJJerWT.setVerticalHeaderLabels(KoF.vheader)
   KoF.jJJerWT.cellClicked.connect(KoF.KoL)
  except:
   KoS("Error: unable to fetch data")
  db.close()
 def KoL(KoF,KoE,column):
  KoF.id_basis_kasus=KoF.jJJerWT.item(KoO(KoE),0).text()
  KoF.uUUjrfERQ.setText(KoF.jJJerWT.item(KoO(KoE),1).text())
  Koz=KoF.URYjdkED.findText(KoF.jJJerWT.item(KoO(KoE),2).text(),KoA.MatchFixedString)
  if Koz>=0:
   KoF.URYjdkED.setCurrentIndex(Koz)
  z=0
  for Kom in KoF.list_id_gejala:
   KoF.GhgrEErT.item(z).setSelected(KoR)
   z=z+1
  for j in Keo(KoF.jJJerWT.rowCount()):
   if(KoF.list_id_penyakit_basis_kasus[KoO(KoE)]==KoF.list_id_penyakit_basis_kasus[j]):
    for k in Keo(KoD(KoF.list_id_gejala)):
     if(KoF.list_id_gejala_basis_kasus[j]==KoF.list_id_gejala[k]):
      KoF.GhgrEErT.item(k).setSelected(KeF)
     z=z+1
 def KoY(KoF):
  KoQ=KoF.GhgrEErT.selectedIndexes()
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
 def KoP(KoF):
  KoQ=KoF.GhgrEErT.selectedIndexes()
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
 def Koj(KoF):
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
  KoF.Kop()
  KoF.KoN()
 def Kop(KoF):
  KoF.id_basis_kasus="0"
  KoF.uUUjrfERQ.setText("")
  KoF.URYjdkED.setCurrentIndex(-1)
  z=0
  for Kom in KoF.list_id_gejala:
   KoF.GhgrEErT.item(z).setSelected(KoR)
   z=z+1
if __name__=='__main__':
 KoH=Koh(KoV)
 ex=KreOeYu()
 Kot(KoH.exec())
