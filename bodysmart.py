#!usr/bin/python


"""
BODY SMART version 1.0.1
date: avril 2017
author: Christophe Desterke
christophe.desterke@gmail.com
python version 3.4
"""

#imports
import os
import time



# obtaining time date
horloge= time.strftime("%a, %d %b %Y %H:%M:%S",time.localtime())

# definition of the variable continuer for exit interaction
continuer = True

while continuer:

	print("	--------------- ")
	print("	BODY CALCULATOR ")
	print("	--------------- ")
	print("\n")
	print(horloge)
	print("\n")

# input variables
	print (" Please enter your identifier: " , end =' ')
	identifier = input ()
	try:
		name = str (identifier)
	except ValueError:
		print('	Please enter an integrer number!')
		continue	
	
	print (" Please enter your weight in kg: " , end =' ')
	kg = input ()
	try:
		poids = float (kg)
	except ValueError:
		print('	Please enter an integrer number!')
		continue
		
	print (" Please enter your size in cm: ", end =' ')
	cm = input ()
	try:
		taille = float (cm)
	except ValueError:
		print('	Please enter an integer number!')
		continue
		
	print (" Please enter your age in years: ", end =' ')
	annees = input ()
	try:
		age = int (annees)
	except ValueError:
		print('	Please enter an integrer number!')
		continue
	
	print (" Please enter your gender (m = man, w = woman): ", end=' ')
	sexe = input ()

	print("\n")
	print("Your Name is: ",name)
	
# pass one line for results	
	print("\n")

# definition of the calculation
# bmi determination
	calbmi = poids / ((taille/100)**2)
	print("Your Body Mass Index is: ",calbmi)
	if sexe == "m" or sexe == "M":
		if calbmi < 20.7:
			print ("Conclusion: You are a man with underweight!","\n")
		elif calbmi < 26.4:
			print ("Conclusion: You are a man with an ideal weight!","\n")
		elif calbmi < 27.8:
			print ("Conclusion: You are a man at the limit of the overweight!","\n")
		elif calbmi < 31.1:
			print ("Conclusion: You are a man with overweight!","\n")
		else:
			print ("Conclusion: You are a man with obesity!","\n")
	elif sexe == "w" or sexe == "W":
		if calbmi < 19.4:
			print ("Conclusion: You are a woman with underweight!","\n")
		elif calbmi < 25.8:
			print ("Conclusion: You are a woman with an ideal weight!","\n")
		elif calbmi < 27.3:
			print ("Conclusion: You are a woman at the limit of the overweight!","\n")
		elif calbmi < 32.3:
			print ("Conclusion: You are a woman with overweight!","\n")
		else:
			print ("Conclusion: You are a woman with obesity!","\n")
	print("\n")



# body surface according to Mosteller
	calscMos = ((taille*poids)/3600)**0.5
	print("Your Body Surface according to Mosteller (1987) is: ",calscMos," m2")

	print("\n")


	
# ideal weight by Lorentz 1929
	if sexe == "m" or sexe == "M":
		lorhom = (taille - 100) - ((taille - 150)/4)
		print("Your ideal weight according to Lorentz (man) is: ",lorhom," kg")
	elif sexe == "w" or sexe == "W":
		lorfem = (taille - 100) - ((taille - 150)/2)
		print("Your ideal weight according to Lorentz (woman) is: ",lorfem," kg")
	print("\n")	


# size conversion in inch
	tailleinch = taille / 2.54


# ideal weight by Devine (1974)
	print("Ideal weight by Devine is usable if you are adult and your size is between 140-220 cm.")
	if sexe == "m" or sexe == "M":
		devman = 50 + (2.3 * (tailleinch - 60))
		print("Your ideal weight according to Devine (man) is:", devman, " kg")
	if sexe == "w" or sexe == "W":
		devwom = 45.5 + (2.3 * (tailleinch - 60))
		print("Your ideal weight according to Devine (woman) is:", devwom, " kg")
	print("\n")

# ideal weight by Peck 
	print("Ideal weight by Peck is usable if you are adult and your size is between 45-220 cm.")
	if sexe == "m" or sexe == "M":
		pecman = -130.736 + 4.064 * tailleinch
		pecmankg = pecman / 2.20462
		print("Your ideal weight according to Peck (man) is:", pecmankg, "kg")
	if sexe == "w" or sexe == "W":
		pecwom = -111.621 + 3.636 * tailleinch
		pecwomkg = pecwom / 2.20462
		print("Your ideal weight according to Peck (woman) is:", pecwomkg, "kg")
	print("\n") 

# print data in txt file my body	
	add =  input('Do you want to add data in the file MY_BODY_DATA (y/n)? ')
	if add == "y" or add == "Y":
		if sexe == "m" or sexe == "M":

# exit variable if sexe is man
			poids = str (poids)
			taille = str (taille)
			age = str (age)		
			horloge = str (horloge)
			calbmi = str (calbmi)
			calscMos = str (calscMos)
			lorhom = str (lorhom)
			devman = str (devman)
			pecmankg = str (pecmankg)

# writing variable if sexe is man			
			mon_fichier = open ("MY_BODY_DATA.txt", "a")
			mon_fichier.write ("\n")
			mon_fichier.write ("#")
			mon_fichier.write ("\n")	
			mon_fichier.write ("DATE: " + "\t" + horloge + "\n")
			mon_fichier.write ("NAME: " + "\t" + name + "\n")
			mon_fichier.write ("SEXE: " + "\t" + sexe + "\n")
			mon_fichier.write ("WEIGHT_KG: " + "\t" + poids + "\n")	
			mon_fichier.write ("SIZE_CM: " + "\t" + taille + "\n")
			mon_fichier.write ("AGE_YEARS: " + "\t" + age + "\n")
			mon_fichier.write ("BODY_MASS_INDEX: " + "\t" + calbmi + "\n")
			mon_fichier.write ("BODY_SURFACE_MOSTELLER_M2: " + "\t" + calscMos + "\n")
			mon_fichier.write ("IDEAL_WEIGHT_LORENTZ_KG: " + "\t" + lorhom + "\n")
			mon_fichier.write ("IDEAL_WEIGHT_DEVINE_KG: " + "\t" + devman + "\n")
			mon_fichier.write ("IDEAL_WEIGHT_PECK_KG: " + "\t" + pecmankg + "\n")

		if sexe == "w" or sexe == "W":

# exit variable if sexe is woman
			poids = str (poids)
			taille = str (taille)
			age = str (age)		
			horloge = str (horloge)
			calbmi = str (calbmi)
			calscMos = str (calscMos)
			lorfem = str (lorfem)
			devwom = str (devwom)
			pecwomkg = str (pecwomkg)

# writing variable if sexe is woman			
			mon_fichier = open ("MY_BODY_DATA.txt", "a")
			mon_fichier.write ("\n")
			mon_fichier.write ("#")
			mon_fichier.write ("\n")	
			mon_fichier.write ("DATE: " + "\t" + horloge + "\n")
			mon_fichier.write ("NAME: " + "\t" + name + "\n")
			mon_fichier.write ("SEXE: " + "\t" + sexe + "\n")
			mon_fichier.write ("WEIGHT_KG: " + "\t" + poids + "\n")	
			mon_fichier.write ("SIZE_CM: " + "\t" + taille + "\n")
			mon_fichier.write ("AGE_YEARS: " + "\t" + age + "\n")
			mon_fichier.write ("BODY_MASS_INDEX: " + "\t" + calbmi + "\n")
			mon_fichier.write ("BODY_SURFACE_MOSTELLER_M2: " + "\t" + calscMos + "\n")
			mon_fichier.write ("IDEAL_WEIGHT_LORENTZ_KG: " + "\t" + lorfem + "\n")
			mon_fichier.write ("IDEAL_WEIGHT_DEVINE_KG: " + "\t" + devwom + "\n")
			mon_fichier.write ("IDEAL_WEIGHT_PECK_KG: " + "\t" + pecwomkg + "\n")

# interaction with exit of the software	
	quitter =  input('Do you want to exit (y/n)? ')
	if quitter == "y" or quitter == "Y":
		continuer = False
os.system("pause")
