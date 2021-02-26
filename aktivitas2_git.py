# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 09:24:55 2021

@author: Kichiro
"""

#operator

bil1=int(input("Masukkan angka pertama : "))
bil2=int(input("Masukkan angka kedua   : "))

jumlah=bil1+bil2
kurang=bil1-bil2
kali=bil1*bil2
bagi=bil1/bil2
modulus=bil1%bil2

print("hasi; dari %d + %d = %d " % (bil1, bil2, jumlah ))
print("hasi; dari %d - %d = %d " % (bil1, bil2, kurang ))
print("hasi; dari %d * %d = %d " % (bil1, bil2, kali ))
print("hasi; dari %d / %d = %d " % (bil1, bil2, bagi ))
print("hasi; dari %d mod %d = %d " % (bil1, bil2, modulus ))