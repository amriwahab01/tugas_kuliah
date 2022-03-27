brg = []

perintah = 0

while perintah != 7:
	print('''1.menambah
	2.menghapus
	3.mengedit
	4.menampilkan
	5.cari barang
	6.cari index
	7.keluar''')
	perintah = int(input("masukkan perintah yang di cari:"))
	if perintah == 1:
		while True:
			msk = input("masukkan barang:")
			brg.append(msk)
			print("barang masuk:",brg)
			stop = input("jika y maka berhenti,selain itu lanjut:")
			if stop == 'y':
				break
				
	elif perintah == 2:
		while True:
			msk = input("masukkan barang ingin di hapus : ")
			brg.remove(msk)
			print("barang masuk:",brg)
			stop = input("jika y maka berhenti,selain itu lanjut:")
			if stop == 'y':
				break
				
	elif perintah == 3:
		while True:
			msk = int(input("masukkan index yang ingin di edit:"))
			brg [msk] = input("masukkan barang yang di edit:")
			print("barang masuk:",brg)
			stop = input("jika y maka berhenti,selain itu lanjut:")
			if stop == 'y':
				break
	elif perintah == 4:
			for i in range(len(brg)):
				print(brg[i])
	elif perintah == 5:
			cari = input("masukkan barang yang di cari:")
			for i in range(len(brg)):
				if brg [i] == cari:
					print("barang yang di cari ada dlm list: ")
	
	elif perintah == 6:
			cari = input("masukkan barang yang ingin dibcari indexnya:")
			print(brg.index(cari))
			
			
	
			
print(brg)