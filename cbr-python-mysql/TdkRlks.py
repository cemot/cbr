from PyQt5 import QtCore,QtGui,QtWidgets
soU=super
soC=len
soK=str
soM=print
soR=int
soT=QtWidgets.QApplication
soi=QtWidgets.QTableWidgetItem
sor=QtWidgets.QPushButton
soj=QtWidgets.QTableWidget
sok=QtWidgets.QLabel
soG=QtWidgets.QLineEdit
soS=QtWidgets.QMainWindow
soV=QtCore.QCoreApplication
sog=QtCore.QMetaObject
sox=QtCore.QRect
wek=QtWidgets.QMessageBox
import sys
soJ=sys.exit
sot=sys.argv
import pymysql
som=pymysql.connect
import FormMain
soI='db_cbr_python'
soX=''
soY='root'
soE='127.0.0.1'
class TdkRlks(soS):
 def __init__(soO):
  super().__init__()
  soO.sop(soO)
 def sop(soO,TdkRlks):
  TdkRlks.setObjectName("TdkRlks")
  TdkRlks.resize(444,290)
  soO.textNamaPenyakit=soG(TdkRlks)
  soO.textNamaPenyakit.setGeometry(sox(160,20,261,20))
  soO.textNamaPenyakit.setObjectName("textNamaPenyakit")
  soO.label=sok(TdkRlks)
  soO.label.setGeometry(sox(20,20,121,16))
  soO.label.setObjectName("label")
  soO.tablePenyakit=soj(TdkRlks)
  soO.tablePenyakit.setGeometry(sox(20,60,401,181))
  soO.tablePenyakit.setObjectName("tablePenyakit")
  soO.tablePenyakit.setColumnCount(0)
  soO.tablePenyakit.setRowCount(0)
  soO.buttonInsert=sor(TdkRlks)
  soO.buttonInsert.setGeometry(sox(20,250,75,23))
  soO.buttonInsert.setObjectName("buttonInsert")
  soO.buttonUpdate=sor(TdkRlks)
  soO.buttonUpdate.setGeometry(sox(100,250,75,23))
  soO.buttonUpdate.setObjectName("buttonUpdate")
  soO.buttonClear=sor(TdkRlks)
  soO.buttonClear.setGeometry(sox(180,250,75,23))
  soO.buttonClear.setObjectName("buttonClear")
  soO.buttonDelete=sor(TdkRlks)
  soO.buttonDelete.setGeometry(sox(350,250,75,23))
  soO.buttonDelete.setObjectName("buttonDelete")
  soO.soW(TdkRlks)
  soO.buttonInsert.clicked.connect(soO.soN)
  soO.buttonUpdate.clicked.connect(soO.soq)
  soO.buttonDelete.clicked.connect(soO.sol)
  soO.buttonClear.clicked.connect(soO.soB)
  sog.connectSlotsByName(TdkRlks)
 def soW(soO,TdkRlks):
  soc=soV.translate
  TdkRlks.setWindowTitle(soc("FormPenyakit","Data Penyakit"))
  soO.label.setText(soc("FormPenyakit","Nama Penyakit"))
  soO.buttonInsert.setText(soc("FormPenyakit","Insert"))
  soO.buttonUpdate.setText(soc("FormPenyakit","Update"))
  soO.buttonClear.setText(soc("FormPenyakit","Clear"))
  soO.buttonDelete.setText(soc("FormPenyakit","Delete"))
  soO.soe()
  soO.show()
 def soe(soO):
  db=som(soE,soY,soX,soI)
  sob=db.cursor()
  soP="SELECT * FROM penyakit" 
  try:
   sob.execute(soP)
   soy=sob.fetchall()
   soO.tablePenyakit.setColumnCount(2)
   soO.tablePenyakit.setRowCount(soC(soy))
   soO.tablePenyakit.setHorizontalHeaderLabels(('Id Penyakit','Nama Penyakit'))
   i=0
   soO.vheader=[]
   for sof in soy:
    soO.vheader.append('')
    soO.tablePenyakit.setItem(i,0,soi(soK(sof[0])))
    soO.tablePenyakit.setItem(i,1,soi(sof[1]))
    i=i+1
   soO.id_penyakit=""
   soO.tablePenyakit.setVerticalHeaderLabels(soO.vheader)
   soO.tablePenyakit.cellClicked.connect(soO.sow)
  except:
   soM("Error: unable to fetch data")
  db.close()
 def sow(soO,sof,column):
  soO.id_penyakit=soO.tablePenyakit.item(soR(sof),0).text()
  soO.textNamaPenyakit.setText(soO.tablePenyakit.item(soR(sof),1).text())
 def soN(soO):
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
  soO.soB()
  soO.soe()
 def soq(soO):
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
  soO.soB()
  soO.soe()
 def sol(soO):
  weN = wek()
  weN.setIcon(wek.Information)
  weN.setText("Demo Version, Tidak Bisa Insert, Update, Delete")
  weN.setWindowTitle("Peringatan")
  weN.setStandardButtons(wek.Ok)
  wer = weN.exec_()
  soO.soB()
  soO.soe()
 def soB(soO):
  soO.textNamaPenyakit.setText("")
if __name__=='__main__':
 soh=soT(sot)
 ex=TdkRlks()
 soJ(soh.exec())
