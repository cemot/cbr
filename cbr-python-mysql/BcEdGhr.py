from PyQt5 import QtCore,QtGui,QtWidgets
suN=super
suS=str
sut=print
sun=len
suz=max
suW=range
suQ=round
suM=QtWidgets.QApplication
suK=QtWidgets.QTableWidgetItem
suA=QtWidgets.QAbstractItemView
sue=QtWidgets.QListWidget
suD=QtWidgets.QLabel
suX=QtWidgets.QPushButton
suR=QtWidgets.QTableWidget
suj=QtWidgets.QMainWindow
suT=QtCore.QCoreApplication
suh=QtCore.QMetaObject
sud=QtCore.QRect
import sys
sur=sys.exit
sui=sys.argv
import pymysql
suC=pymysql.connect
import FormMain
suw='db_cbr_python'
suU=''
sug='root'
suI='127.0.0.1'
class BcEdGhr(suj):
 def __init__(sua):
  super().__init__()
  sua.suk(sua)
 def suk(sua,BcEdGhr):
  BcEdGhr.setObjectName("BcEdGhr")
  BcEdGhr.resize(872,520)
  sua.tableHasilAkhir=suR(BcEdGhr)
  sua.tableHasilAkhir.setGeometry(sud(20,270,401,201))
  sua.tableHasilAkhir.setObjectName("tableHasilAkhir")
  sua.tableHasilAkhir.setColumnCount(0)
  sua.tableHasilAkhir.setRowCount(0)
  sua.buttonPerhitungan=suX(BcEdGhr)
  sua.buttonPerhitungan.setGeometry(sud(350,210,75,23))
  sua.buttonPerhitungan.setObjectName("buttonPerhitungan")
  sua.label=suD(BcEdGhr)
  sua.label.setGeometry(sud(20,10,161,16))
  sua.label.setObjectName("label")
  sua.label_2=suD(BcEdGhr)
  sua.label_2.setGeometry(sud(20,250,161,16))
  sua.label_2.setObjectName("label_2")
  sua.tablePerhitungan=suR(BcEdGhr)
  sua.tablePerhitungan.setGeometry(sud(450,270,401,201))
  sua.tablePerhitungan.setObjectName("tablePerhitungan")
  sua.tablePerhitungan.setColumnCount(0)
  sua.tablePerhitungan.setRowCount(0)
  sua.label_6=suD(BcEdGhr)
  sua.label_6.setGeometry(sud(450,250,161,16))
  sua.label_6.setObjectName("label_6")
  sua.label_8=suD(BcEdGhr)
  sua.label_8.setGeometry(sud(450,10,161,16))
  sua.label_8.setObjectName("label_8")
  sua.tableBasisKasus=suR(BcEdGhr)
  sua.tableBasisKasus.setGeometry(sud(450,30,401,211))
  sua.tableBasisKasus.setObjectName("tableBasisKasus")
  sua.tableBasisKasus.setColumnCount(0)
  sua.tableBasisKasus.setRowCount(0)
  sua.listGejala=sue(BcEdGhr)
  sua.listGejala.setGeometry(sud(20,30,401,171))
  sua.listGejala.setSelectionMode(suA.MultiSelection)
  sua.listGejala.setObjectName("listGejala")
  sua.buttonProses=suX(BcEdGhr)
  sua.buttonProses.setGeometry(sud(20,210,75,23))
  sua.buttonProses.setObjectName("buttonProses")
  sua.labelHasil=suD(BcEdGhr)
  sua.labelHasil.setGeometry(sud(20,480,401,31))
  sua.labelHasil.setObjectName("labelHasil")
  sua.label.raise_()
  sua.tableHasilAkhir.raise_()
  sua.buttonPerhitungan.raise_()
  sua.label_2.raise_()
  sua.tablePerhitungan.raise_()
  sua.label_6.raise_()
  sua.label_8.raise_()
  sua.tableBasisKasus.raise_()
  sua.listGejala.raise_()
  sua.buttonProses.raise_()
  sua.labelHasil.raise_()
  sua.suV(BcEdGhr)
  sua.buttonProses.clicked.connect(sua.suB)
  sua.buttonPerhitungan.clicked.connect(sua.suL)
  suh.connectSlotsByName(BcEdGhr)
 def suV(sua,BcEdGhr):
  suJ=suT.translate
  BcEdGhr.setWindowTitle(suJ("FormKonsultasiCBR","Sistem Pakar Metode Case Based Reasoning (CBR) - http://contohprogram.com"))
  sua.buttonPerhitungan.setText(suJ("FormKonsultasiCBR","Perhitungan"))
  sua.label.setText(suJ("FormKonsultasiCBR","Pilih Gejala"))
  sua.label_2.setText(suJ("FormKonsultasiCBR","<html><head/><body><p>Hasil Akhir</p></body></html>"))
  sua.label_6.setText(suJ("FormKonsultasiCBR","Perhitungan"))
  sua.label_8.setText(suJ("FormKonsultasiCBR","Basis Kasus"))
  sua.buttonProses.setText(suJ("FormKonsultasiCBR","Proses"))
  sua.labelHasil.setText(suJ("FormKonsultasiCBR","-"))
  sua.suq()
  sua.sul()
  BcEdGhr.resize(445,250)
  sua.show()
 def suq(sua):
  db=suC(suI,sug,suU,suw)
  suY=db.cursor()
  suF="SELECT * FROM gejala"
  sua.list_id_gejala=[]
  sua.listGejala.clear()
  try:
   suY.execute(suF)
   suc=suY.fetchall()
   i=0
   for sup in suc:
    sua.list_id_gejala.append(suS(sup[0]))
    sua.listGejala.addItem(sup[1])
    i=i+1
  except:
   sut("Error: unable to fetch data")
  db.close()
 def sul(sua):
  db=suC(suI,sug,suU,suw)
  suY=db.cursor()
  suF="SELECT basis_kasus.*, penyakit.nama_penyakit, gejala.nama_gejala FROM basis_kasus LEFT JOIN penyakit ON penyakit.id_penyakit = basis_kasus.id_penyakit LEFT JOIN gejala ON basis_kasus.id_gejala = gejala.id_gejala"
  sua.list_no_basis_kasus=[]
  sua.list_id_penyakit_basis_kasus=[]
  sua.list_id_gejala_basis_kasus=[]
  try:
   suY.execute(suF)
   suc=suY.fetchall()
   sua.tableBasisKasus.setColumnCount(4)
   sua.tableBasisKasus.setRowCount(sun(suc)) 
   sua.tableBasisKasus.setHorizontalHeaderLabels(('Id','No Basis Kasus','Penyakit','Gejala'))
   i=0
   sua.vheader=[]
   for sup in suc:
    sua.vheader.append('')
    sua.list_no_basis_kasus.append(suS(sup[1]))
    sua.list_id_penyakit_basis_kasus.append(suS(sup[2]))
    sua.list_id_gejala_basis_kasus.append(suS(sup[3]))
    sua.tableBasisKasus.setItem(i,0,suK(suS(sup[0])))
    sua.tableBasisKasus.setItem(i,1,suK(suS(sup[1])))
    sua.tableBasisKasus.setItem(i,2,suK(sup[4]))
    sua.tableBasisKasus.setItem(i,3,suK(sup[5]))
    i=i+1
   sua.id_basis_kasus=""
   sua.tableBasisKasus.setVerticalHeaderLabels(sua.vheader)
  except:
   sut("Error: unable to fetch data")
  db.close()
 def suB(sua):
  sua.list_id_gejala_terpilih=[]
  sua.list_nama_gejala_terpilih=[]
  suf=sua.listGejala.selectedIndexes()
  suP=sua.listGejala.selectedItems()
  i=0
  for sup in suf:
   sua.list_id_gejala_terpilih.append(suS(sua.list_id_gejala[suf[i].row()]))
   sua.list_nama_gejala_terpilih.append(suP[i].text())
   i=i+1
  db=suC(suI,sug,suU,suw)
  suY=db.cursor()
  suF="SELECT basis_kasus.*, penyakit.nama_penyakit, gejala.nama_gejala FROM basis_kasus LEFT JOIN penyakit ON penyakit.id_penyakit = basis_kasus.id_penyakit LEFT JOIN gejala ON basis_kasus.id_gejala = gejala.id_gejala ORDER BY no_kasus ASC, basis_kasus.id_penyakit ASC, basis_kasus.id_gejala"
  sua.list_no_basis_kasus=[]
  sua.list_id_penyakit_basis_kasus=[]
  sua.list_nama_penyakit_basis_kasus=[]
  sua.list_jml_gejala_cocok=[]
  sua.list_jml_gejala_kasus=[]
  sua.list_jml_gejala_dipilih=[]
  sua.list_pembagi=[]
  sua.list_nilai_hasil=[]
  sub=""
  try:
   suY.execute(suF)
   suc=suY.fetchall()
   i=-1
   for sup in suc:
    if(sub!=suS(sup[1])):
     i=i+1
     sua.list_no_basis_kasus.append(suS(sup[1]))
     sua.list_id_penyakit_basis_kasus.append(sup[2])
     sua.list_nama_penyakit_basis_kasus.append(suS(sup[4]))
     sua.list_jml_gejala_cocok.append(0)
     sua.list_jml_gejala_kasus.append(0)
     sua.list_jml_gejala_dipilih.append(sun(sua.list_id_gejala_terpilih))
     sua.list_pembagi.append(0)
     sua.list_nilai_hasil.append(0)
    sua.list_jml_gejala_kasus[i]=sua.list_jml_gejala_kasus[i]+1
    for suy in sua.list_id_gejala_terpilih:
     if(suy==suS(sup[3])):
      sua.list_jml_gejala_cocok[i]=sua.list_jml_gejala_cocok[i]+1
    sub=suS(sup[1])
   i=0
   for sup in sua.list_no_basis_kasus:
    sua.list_pembagi[i]=suz(sua.list_jml_gejala_kasus[i],sua.list_jml_gejala_dipilih[i]);
    if(sua.list_pembagi[i]>0):
     sua.list_nilai_hasil[i]=sua.list_jml_gejala_cocok[i]/sua.list_pembagi[i]
    i=i+1
  except:
   sut("Error: unable to fetch data")
  db.close()
  sua.tablePerhitungan.setColumnCount(6)
  sua.tablePerhitungan.setRowCount(sun(sua.list_no_basis_kasus))
  sua.tablePerhitungan.setHorizontalHeaderLabels(('Kasus','Jml Gejala Cocok','Jml Gejala Kasus','Jml Gejala Dipilih','Pembagi','Nilai Hasil'))
  sua.vheader=[]
  i=0
  for sup in sua.list_no_basis_kasus:
   sua.vheader.append('')
   sua.tablePerhitungan.setItem(i,0,suK(sua.list_no_basis_kasus[i]))
   sua.tablePerhitungan.setItem(i,1,suK(suS(sua.list_jml_gejala_cocok[i])))
   sua.tablePerhitungan.setItem(i,2,suK(suS(sua.list_jml_gejala_kasus[i])))
   sua.tablePerhitungan.setItem(i,3,suK(suS(sua.list_jml_gejala_dipilih[i])))
   sua.tablePerhitungan.setItem(i,4,suK(suS(sua.list_pembagi[i])))
   sua.tablePerhitungan.setItem(i,5,suK(suS(sua.list_nilai_hasil[i])))
   i=i+1
  sua.tablePerhitungan.setVerticalHeaderLabels(sua.vheader)
  sua.rangking_no_basis_kasus=[]
  sua.rangking_id_penyakit_basis_kasus=[]
  sua.rangking_nama_penyakit_basis_kasus=[]
  sua.rangking_nilai_hasil=[]
  i=0
  for sup in sua.list_no_basis_kasus:
   sua.rangking_no_basis_kasus.append(sua.list_no_basis_kasus[i])
   sua.rangking_id_penyakit_basis_kasus.append(sua.list_id_penyakit_basis_kasus[i])
   sua.rangking_nama_penyakit_basis_kasus.append(sua.list_nama_penyakit_basis_kasus[i])
   sua.rangking_nilai_hasil.append(sua.list_nilai_hasil[i])
   i=i+1
  for i in suW(sun(sua.rangking_no_basis_kasus)):
   for j in suW(sun(sua.rangking_no_basis_kasus)):
    if j>i:
     if sua.rangking_nilai_hasil[j]>sua.rangking_nilai_hasil[i]:
      suH=sua.rangking_no_basis_kasus[i]
      suO=sua.rangking_id_penyakit_basis_kasus[i]
      suo=sua.rangking_nama_penyakit_basis_kasus[i]
      sux=sua.rangking_nilai_hasil[i]
      sua.rangking_no_basis_kasus[i]=sua.rangking_no_basis_kasus[j]
      sua.rangking_id_penyakit_basis_kasus[i]=sua.rangking_id_penyakit_basis_kasus[j]
      sua.rangking_nama_penyakit_basis_kasus[i]=sua.rangking_nama_penyakit_basis_kasus[j]
      sua.rangking_nilai_hasil[i]=sua.rangking_nilai_hasil[j]
      sua.rangking_no_basis_kasus[j]=suH
      sua.rangking_id_penyakit_basis_kasus[j]=suO
      sua.rangking_nama_penyakit_basis_kasus[j]=suo
      sua.rangking_nilai_hasil[j]=sux
  sua.tableHasilAkhir.setColumnCount(4)
  sua.tableHasilAkhir.setRowCount(sun(sua.rangking_no_basis_kasus))
  sua.tableHasilAkhir.setHorizontalHeaderLabels(('Rangking','Kasus','Penyakit','Nilai Hasil'))
  sua.vheader=[]
  i=0
  for sup in sua.rangking_no_basis_kasus:
   sua.vheader.append('')
   sua.tableHasilAkhir.setItem(i,0,suK(suS(i+1)))
   sua.tableHasilAkhir.setItem(i,1,suK(sua.rangking_no_basis_kasus[i]))
   sua.tableHasilAkhir.setItem(i,2,suK(sua.rangking_nama_penyakit_basis_kasus[i]))
   sua.tableHasilAkhir.setItem(i,3,suK(suS(suQ(sua.rangking_nilai_hasil[i],2))))
   i=i+1
  sua.tableHasilAkhir.setVerticalHeaderLabels(sua.vheader)
  sua.labelHasil.setText("Penyakit Terbesar "+suS(sua.rangking_id_penyakit_basis_kasus[0])+"."+sua.rangking_nama_penyakit_basis_kasus[0]+" pada Kasus No."+suS(sua.rangking_no_basis_kasus[0])+" dengan Hasil Nilai "+suS(suQ(sua.rangking_nilai_hasil[0],2)))
  sua.resize(445,520)
 def suL(sua):
  sut("ok")
  sua.resize(872,520)
if __name__=='__main__':
 suv=suM(sui)
 ex=BcEdGhr()
 sur(suv.exec())
# Created by pyminifier (https://github.com/liftoff/pyminifier)
