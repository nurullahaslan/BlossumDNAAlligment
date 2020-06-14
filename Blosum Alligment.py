#Hata vermesi durumunda 'pip install biopython' komutunu giriniz.
from Bio.SubsMat import MatrixInfo

#Indisleri yollanan elamanlara karşılık gelen sayısal değeri döndürür.
def score_match(pair, matrix):
    if pair not in matrix:
        return matrix[(tuple(reversed(pair)))]
    else:
        return matrix[pair]
#Verilen dizilimlerin başına tire atmaya yarayan fonksiyon
#Tire boşluğu temsil etmektedir gap anlamında değildir 
#Kaydırma işlemini yapmak için kullanılmıştır.
def str_append(s, n):
    output = '-'
    i = 0
    while i < n:
        output += s
        i = i + 1
    return output
#Son durumda tire yerine boşluk eklemek için kullanılacak
def str_append2(s, n):
    output = ' '
    i = 0
    while i < n:
        output += s
        i = i + 1
    return output
#dizilimleri ve blosam matrisini yollayarak skor hesabı yapan fonk.    
def score_global(seq1, seq2, matrix):
    score = 0
    tempScore=0
    tempSeq=''
    connection=''
    for i in range(len(seq1)):
        #seq1 in uzunluğu kadar başına dire ekler. 
        #Amaç her iki dizilimin elmanlarını karşılarştırmak burda.
    	seq1=str_append(seq1,1)
    #seq2 nin uzunluğu daha kısa olduğu durumlarda hata veriyordu
    #uzunlukları eşitlemek için seq2'nin başına tire ekler.
    if len(seq1) > len(seq2):
        lenght=len(seq1) - len(seq2)
        for i in range(lenght):
        	seq2 +='-'
    #Her eşleşme için hesaplamanın yapıldığı döngü.
    #Dögünün sonucunda en yüksek skor ve dizilim tempte tutulur.  
    for j in range(len(seq1)):
        tempScore=0
        #O ani şleşme için puan hesabı yapan döngü
        for i in range(len(seq1)):
            pair = (seq1[i], seq2[i])
            
            #Tireler skoru etkilemiyor.
            #Toplam skor eşleşen çiftlere göre 
            #hesaplama fonksiyonuyla hesaplanır.
            if '-' in pair:
                tempScore+=0
            else:
                tempScore += score_match(pair, matrix)
        #Yeni bir yüksek skor bulunursa güncel skorlar tempte tutulur. 
        if tempScore>score:
           score=tempScore
           tempSeq=seq2
        #dongünü sonraki adımında kaydırma yapmak için
        #dizilimin başına tire eklenir.          
        seq2=str_append(seq2,1 )
    #Her Dizilime kaydırmadan dolayı eklenen fazladan eklenen
    #tireleri kaldırmak için tire sayısı hesaplanır.
    len1 =len(seq1) -len(seq1.lstrip('-'))
    len2= len(tempSeq) - len(tempSeq.lstrip('-'))
    #Başta bulunun bütün tireler silinir. 
    seq1 = seq1.lstrip('-')
    tempSeq=tempSeq.lstrip('-')
    #Hesaplama işleminde ne kadar kaydırdığımızı hesaplamak 
    #için kullanılan tire iktarlarının farkını alarak hesaplıyoruz
    #Çıkan sonuca göre kayan başa boşluk ekliyoruz.
    if len1>len2:
    	blanklen=len1-len2
    	for i in range(blanklen):
    		seq1=str_append2(seq1,1)
    else: 
    	blanklen=len2-len1
    	for i in range(blanklen):
    		tempSeq=str_append2(tempSeq,1)
    #uzunluğu eşitlemek için eklediğimiz tireleri siler.
    seq2=tempSeq.rstrip('-')
    for i in range(len(seq2)):
        if seq1[i] == seq2[i]:
            connection+='|'
        else:
            connection+=' '
        
    #Dizilimleri ekrana yazdırır.
    print('En iyi dizilim:')
    print()	
    print(seq1)
    print(connection)
    print(seq2)
    return score
#Kullanacağımız dizilimler.
seq1= 'GMIDLITARCAYPSWTGH'
seq2= 'IEVRTAKCAYPGWSGH'

#Bio kütüphanesinden blosum62 marisi çaığırılır
blosum = MatrixInfo.blosum62
#Skor hesaplanması için fonksiyona yollanır.
score = score_global(seq1, seq2, blosum)
#skoru ekraana yazdırır.
print()
print('Skor = '+ str(score))

