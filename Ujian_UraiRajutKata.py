# Mengurai dan Merajut Kata

class uraiRajutKata():
    def urai (self, kataUrai):
        hasil = ''
        for row in range (len(kataUrai)):
            for col in range (row + 1):
                hasil += kataUrai[col]
                hasil += ""
        hasil += ""
        return hasil
    def rajut (self, kataRajut):
        syarat = [1]
        awal = 1
        for i in range (2, len(kataRajut)):
            awal += i
            syarat.append(awal)
        panjang = syarat.index (len(kataRajut)) + 1
        panjang *= -1
        hasil2 = kataRajut [panjang: len(kataRajut)]
        return hasil2

x = uraiRajutKata()

print(x.urai('Code'))
print(x.urai('Python'))
print(x.urai('Purwadhika'))

print(x.rajut('CCoCodCode'))
print(x.rajut('PPyPytPythPythoPython'))
print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))