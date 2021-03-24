def czynniki(czynniki,plik1,plik2,plik3,plik4,plik5, plik6,plik7,plik8,plik9,plik10):
	s={}
	p=open(czynniki,'r')
	o=open("zliczone_czynniki.csv",'w')
	o.write("gene_name"+',')
	for line in p:
		tab=line.split()
		s[tab[1]]=0
		o.write(tab[1]+',')
	o.write('\n')
	p.close()
	s1=przypisz(plik1,s.copy())
	s2=przypisz(plik2,s.copy())
	s3=przypisz(plik3,s.copy())
	s4=przypisz(plik4,s.copy())
	s5=przypisz(plik5,s.copy())
	s6=przypisz(plik6,s.copy())
	s7=przypisz(plik7,s.copy())
	s8=przypisz(plik8,s.copy())
	s9=przypisz(plik9,s.copy())
	s10=przypisz(plik10,s.copy())
	output(plik1,s1,o)
	output(plik2,s2,o)
	output(plik3,s3,o)
	output(plik4,s4,o)
	output(plik5,s5,o)
	output(plik1,s6,o)
	output(plik2,s7,o)
	output(plik3,s8,o)
	output(plik4,s9,o)
	output(plik5,s10,o)
	o.close()
	
def przypisz(plik,s):
	p=open(plik,'r')
	for line in p:
		tab=line.split()
		#print(tab)
		if tab[0] in s.keys():
			s[tab[0]]+=1
		#else:
			#print("whoa!"+tab[0])
	p.close()
	return s

def output(plik,s,o):
	n=nazwa(plik)
	o.write('gene_'+n)
	for k in s.keys():
		o.write(','+str(s[k]))
	o.write('\n')

def nazwa(s):
	n=''
	for i in s:
		if i != '.':
			n+=i
		else:
			break
	return n

czynniki("tfbs_lista.txt","AT1G30070.txt","AT1G66080.txt","AT2G20560.txt","AT2G20940.txt","AT3G04010.txt","AT3G07150.txt","AT3G12050.txt","AT4G23493.txt","AT5G10695.txt","AT5G35320.txt")

