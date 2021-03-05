# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 08:54:54 2021

@author: Kichiro
"""

class student:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_student = 0

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        student.jumlah_student = 1

    def tampilkan_jumlah(self):
        print("Total student:", student.jumlah_student)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Umur :", self.umur)


student1 = student("FAIRUZ", 20)


student1.tampilkan_profil()
print("Total Student :", student.jumlah_student)