from PyQt5 import QtCore,QtGui,QtWidgets
hcx=super
hcF=None
hcI=False
hcM=True
hcV=print
hcd=QtWidgets.QApplication
hcf=QtWidgets.QMessageBox
hcj=QtWidgets.QPushButton
hcN=QtWidgets.QLabel
hcP=QtWidgets.QLineEdit
hcH=QtWidgets.QMainWindow
hcm=QtCore.QCoreApplication
hcb=QtCore.QMetaObject
hcp=QtCore.QRect
import sys
hcO=sys.exit
hcg=sys.argv
import pymysql
hcu=pymysql.connect
import FormMain
hco='admin'
hcn='db_cbr_python'
hcl=''
hcC='root'
hcE='127.0.0.`'
class DhlkRks(hcH):
 def __init__(hcS):
  super().__init__()
  hcS.hcz(hcS)
  hcS.fMain=hcF
 def hcz(hcS,DhlkRks):
  DhlkRks.setObjectName("DhlkRks")
  DhlkRks.resize(293,130)
  hcS.KJOIWeed=hcP(DhlkRks)
  hcS.KJOIWeed.setGeometry(hcp(90,20,181,20))
  hcS.KJOIWeed.setObjectName("KJOIWeed")
  hcS.kjKJDPAX=hcN(DhlkRks)
  hcS.kjKJDPAX.setGeometry(hcp(20,20,61,16))
  hcS.kjKJDPAX.setObjectName("kjKJDPAX")
  hcS.jksJRkjs=hcN(DhlkRks)
  hcS.jksJRkjs.setGeometry(hcp(20,50,47,13))
  hcS.jksJRkjs.setObjectName("jksJRkjs")
  hcS.jkksdrE=hcj(DhlkRks)
  hcS.jkksdrE.setGeometry(hcp(20,80,75,23))
  hcS.jkksdrE.setObjectName("jkksdrE")
  hcS.qeertsdf=hcj(DhlkRks)
  hcS.qeertsdf.setGeometry(hcp(200,80,75,23))
  hcS.qeertsdf.setObjectName("qeertsdf")
  hcS.KJjKJSDF=hcP(DhlkRks)
  hcS.KJjKJSDF.setGeometry(hcp(90,50,181,20))
  hcS.KJjKJSDF.setInputMask("")
  hcS.KJjKJSDF.setObjectName("KJjKJSDF")
  hcS.KJdskKJD=hcN(DhlkRks)
  hcS.KJdskKJD.setGeometry(hcp(20,110,251,16))
  hcS.KJdskKJD.setText("")
  hcS.KJdskKJD.setObjectName("KJdskKJD")
  hcS.jkksdrE.clicked.connect(hcS.hcY)
  hcS.qeertsdf.clicked.connect(hcS.hcK)
  hcS.hcq(DhlkRks)
  hcb.connectSlotsByName(DhlkRks)
 def hcq(hcS,DhlkRks):
  hcv=hcm.translate
  DhlkRks.setWindowTitle(hcv("DhlkRks","Login"))
  hcS.kjKJDPAX.setText(hcv("DhlkRks","Username"))
  hcS.jksJRkjs.setText(hcv("DhlkRks","Password"))
  hcS.jkksdrE.setText(hcv("DhlkRks","Login"))
  hcS.qeertsdf.setText(hcv("DhlkRks","Exit"))
  hcS.show()
 def hcY(hcS):
  print('yeah')
  db=pymysql.connect('127.0.0.1', 'root', '', 'db_cbr_python')
  hcw=db.cursor()
  hcQ="SELECT * FROM `login` WHERE `username` = '%s' AND `password` = '%s'"%(hcS.KJOIWeed.text(),hcS.KJjKJSDF.text())
  hcw.execute(hcQ)
  hcG=hcw.fetchall()
  if hcG:
   print('ok')
   hco=hcG[0][0]
   hcS.fMain.kjdKJSKJd.setEnabled(False)
   hcS.fMain.XccSxnDf.setEnabled(True)
   hcS.fMain.ccMMssDF.setEnabled(True)
   hcS.fMain.dskKJDff.setEnabled(True)
   hcS.fMain.uuUkejsE.setEnabled(True)
   hcS.fMain.ooOweasd.setEnabled(True)
   hcS.close()
  else:
   print('not ok')
   hcJ=hcf()
   hcJ.setIcon(hcf.Information)
   hcJ.setText("Login Gagal")
   hcJ.setWindowTitle("Peringatan")
   hcJ.setStandardButtons(hcf.Ok)
   hcD=hcJ.exec_()
   hcV("gagal")
  db.close()
 def hcK(hcS):
  hcS.close()
if __name__=='__main__':
 hcT=hcd(hcg)
 ex=DhlkRks()
 hcO(hcT.exec())
