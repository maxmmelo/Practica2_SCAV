#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import os
import sys
import subprocess

n = 0
print("Exercici 1")
while(n == 1):
	print("Diga'm quants segons vols tallar el vídeo")
	n = int(input())
	subprocess.call(['ffmpeg', '-i', 'BBB.mp4', '-t', str(n), 'tall.mp4'])
	print("prèmer 1 si vols tornar a tallar el vídeo, qualsevol altre nombre per continuar")
	n = int(input())

print("Exercici 2")
n = 0
while(n == 0):
	subprocess.call(['ffplay', 'BBB.mp4', '-vf', "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay"])
	print("prèmer 0 si vols tornar a veure l'histograma, qualsevol altre nombre per continuar")
	n = int(input())

print("Exercici 3")
n = 0
while(n==0):
	print("Diga'm a quina resolució vols canviar el vídeo")
	print("Opció 1: 720p")
	print("Opció 2: 480p")
	print("Opció 3: 360x240")
	print("Opció 4: 160x120")
	n = int(input())
	if(n==1):
		subprocess.call(['ffmpeg', '-i', 'BBB.mp4', "-filter:v", "scale=1280:720", '-c:a', 'copy', '720p.mp4'])
	elif(n==2):
		subprocess.call(['ffmpeg', '-i', 'BBB.mp4', "-filter:v", "scale=640:480", '-c:a', 'copy', '480p.mp4'])
	elif(n==3):
		subprocess.call(['ffmpeg', '-i', 'BBB.mp4', "-filter:v", "scale=360:240", '-c:a', 'copy', '360x240.mp4'])
	elif(n==4):
		subprocess.call(['ffmpeg', '-i', 'BBB.mp4', "-filter:v", "scale=160:1200", '-c:a', 'copy', '160x120.mp4'])
	else:
		print("opció incorrecta")
	print("prèmer 0 si vols tornar a canviar la resolució, qualsevol altre nombre per continuar")
	n = int(input())
	
print("Exercici 4")
n=0
while(n==0):
	print("Diga'm a quina opció vols canviar l'àudio del vídeo")
	print("Opció 1: mono")
	print("Opció 2: 5.1")

	n = int(input())
	if(n==1):
		subprocess.call(['ffmpeg', '-i', 'BBB.mp4', '-ac', '1', 'mono.mp4'])
	elif(n==2):
		subprocess.call(['ffmpeg', '-i', 'BBB.mp4', '-filter_complex', "[0:a]pan=5.1(side)|FL=FL|FR=FR|LFE<FL+FR|SL=FL|SR=FR[a]", '-map', '0', '-map', '-0:a', '-map', "[a]", '-c', 'copy', '-c:a', 'flac', '-strict', '-2', '5_1.mp4'])
	else:
		print("opció incorrecta")
	print("prèmer 0 si vols tornar a canviar el format de l'àudio, qualsevol altre nombre per sortir")
	n = int(input())
	
print("adeu")
print("maxmmelo")

