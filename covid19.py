#covid-19 dcoder kodlama platformunda @zclaster1234 isimli üyenin kodlaması @siberavci tarafından Türkçeleştirilmiştir.
print("Dikkat!! bu test sonuçları bağlayıcı değildir kendi kendinizi basitçe anket yapmak için yazılmıştır Lütfen herhangi bir rahatsızlığınız var ise alanında uzman kişilerden destek alınız ve 112 yi arayarak tıbbi yardım isteyiniz!!!")

isim = input('Adınız: ')

yas = int(input('Yaşınız: '))

print('\nBu belirtilerden herhangi birine sahip misiniz?')

ates = int(input('Ateş (0= hayır, 1= evet): '))

oksuruk = int(input('Öksürük (0= hayır, 1= evet): '))

nefes = int(input('Nefes Darlığı (0= hayır, 1= evet): '))

agriakinti = int(input('Boğaz ağrısı veya burun akıntısı (0= hayır, 1= evet): '))

kusma = int(input('Bulantı/Kusma (0= hayır, 1= evet): '))

hastalik = int(input('Diyabet, Böbrek veya Kalp Hastalığı (0= hayır, 1= evet): '))

salgin = int(input('Son 14 gündür salgın olan bölgede veya salgından etkilenen biriyle temasta bulundunuz mu? (0= hayır, 1= evet): '))

risk = ates*2 + oksuruk*2 + nefes*2 + agriakinti + kusma + hastalik

print('\nTamamdır, Merhaba', isim)

if salgin ==0:

    if risk > 4: print("Yüksek COVID-19 riskiniz bulunmuyor, muhtemelen gripsiniz,")

    else: print("COVID-19 Enfeksiyonu riskiniz var,")

if salgin ==1:

    if risk > 4: print('Enfeksiyon riski veya şüpheniz var ise, cerrahi maske takmalısınız ve çevre/insanlardan izole olarak en yakın sağlık kuruluşunda testlerinizi yaptırmalısınız!')

    else: print("COVID-19 belirtiniz yok fakat salgın bölgede olduğunuzu söylediğiniz için riskiniz bulunmaktadır, ")

if -1<yas<41: oran = "0.2 %"
if 40<yas<51: oran = "0.4 %"
if 50<yas<61: oran = '1.3 %'
if 60<yas<71: oran = "3.6 %"
if 70<yas<81: oran = '8 %'
if 80<yas: oran = '14.8 %'
print('sadece yaş kriterine bağlı olarak, eğer enfekte olduysanız, ölüm oranınız:', oran)
print("Dikkat!! bu test sonuçları bağlayıcı değildir kendi kendinizi basitçe anket yapmak için yazılmıştır Lütfen herhangi bir rahatsızlığınız var ise alanında uzman kişilerden destek alınız ve 112 yi arayarak tıbbi yardım isteyiniz!!!")
input()