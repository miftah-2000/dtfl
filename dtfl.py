import os
import locale
import datetime
import pprint
import subprocess
import re
#locale.setlocale(locale.LC-ALL,'en_US')
class file:
    def __init__(self,gnm):
        self.nfile=gnm
        self.vfile="fin"
        self.dlist=[]
        self.dform=[]
        self.judul=[]
        self.tjml=[]
        self.fjudul=[]
        self.ftjml=[]
        self.jbar=0
        self.jkol=0
        self.lbar=0
        self.lkol=0
    def buka(self):
        self.dlist=[]
        try:
            self.vfile=open(self.nfile,"r+")
            self.ambil()
        except:
            self.vfile=open(self.nfile,"w")
            print ('Data masih kosong....!\nsilahkan isi nama kolom terlebih dahulu\ndengan perintah data.judul("...")')
    def ambil(self):    
        for a in self.vfile:
            line=a.strip().split(',')
            self.dlist.append(line)
        for a in zip(*self.dlist[1:]):
            if a[0].isdigit():
                jml=sum(int(kol) for kol in a)
                jml=f'{jml:,}'
                self.tjml.append(jml)
            else:
                self.tjml.append(">>>")
        self.dlist.insert(1,self.tjml)
        self.jkol=len(self.dlist[0])
        self.jbar=len(self.dlist[2:])
        self.lkol=[max(map(len,kol)) for kol in zip(*self.dlist)]
        self.lbar=sum(self.lkol)+self.jkol-1
        self.judul=self.dlist[0]
        del self.dlist[0:2]
        print ('Record / Field :',self.jbar,'/',self.jkol)
        for a in range(len(self.dlist)):
            frm=[]
            for item,width in zip(self.dlist[a],self.lkol):
                if item.isdigit():
                    ang=f'{int(item):,}'
                    frm.append("%*s" %(width,ang))
                else:
                    frm.append("%-*s" %(width,item))
                self.dform.append(frm)

        for item,width in zip(self.judul,self.lkol):
            if item.isdigit():
                ang=f'{int(item):,}'
                frm="%*s" %(width,ang)
            else:
                frm="%-*s" %(width,item)
            self.fjudul.append(frm)
        for item,width in zip(self.tjml,self.lkol):
            if item.isdigit():
                ang=f'{int(item):,}'
                frm="%*s" %(width,ang)
            else:
                frm="%-*s" %(width,item)
            self.ftjml.append(frm)

