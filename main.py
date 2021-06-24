import random
import os
print(" __    __                                                                 ")
print("/  |  /  |                                                                ")
print("$$ |  $$ |  ______   _______    ______   _____  ____    ______   _______  ")
print("$$ |__$$ | /      \ /       \  /      \ /     \/    \  /      \ /       \ ")
print("$$    $$ | $$$$$$  |$$$$$$$  |/$$$$$$  |$$$$$$ $$$$  | $$$$$$  |$$$$$$$  |")
print("$$$$$$$$ | /    $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ | /    $$ |$$ |  $$ |")
print("$$ |  $$ |/$$$$$$$ |$$ |  $$ |$$ \__$$ |$$ | $$ | $$ |/$$$$$$$ |$$ |  $$ |")
print("$$ |  $$ |$$    $$ |$$ |  $$ |$$    $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$ |")
print("$$/   $$/  $$$$$$$/ $$/   $$/  $$$$$$$ |$$/  $$/  $$/  $$$$$$$/ $$/   $$/ ")
print("                              /  \__$$ |                                  ")
print("                              $$    $$/                                   ")
print("                               $$$$$$/                                    ")
print()
print()
print()
print()
print()
print()
print()
print("                 Druk op [ENTER] om het spel te starten")
input()
os.system('clear')

name = input("Wat is je naam? ")
print("Welkom " + name)
print("Je begint met 6 beurten.")
Woorden = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
##
input("druk enter!!!!!!!!!!!!!!")
def galgje():

  gekozenWoord = random.choice(Woorden)
  goedgekozenletters = []
  foutegekozenletters = []
  aantal_beurten = 6 
  while True :
    os.system("clear")
    print("Je hebt nog", aantal_beurten , "beurten over")
    print("\nDit zijn de letters die je fout hebt gekozen")
    print(foutegekozenletters)
    print("Dit zijn de letters die je goed hebt gekozen")
    print(goedgekozenletters)
    gekozenletter = input("\nKies een letter: ")
    
    if gekozenletter in gekozenWoord :       
      goedgekozenletters.append(gekozenletter)
    else : 
      foutegekozenletters.append(gekozenletter)
      aantal_beurten -=1 

    for letter in gekozenWoord :
      if letter in goedgekozenletters : 
        print(letter, end= "")
      else :     
        print("_ ", end = "")  

    if aantal_beurten == 0 : 
      print("\nJammer, je hebt verloren!")
      print("Het woord was", gekozenWoord,".")
      break 
    contains = True
    for letter in gekozenWoord : 
      if not letter in goedgekozenletters :
        contains = False

    if contains == True :
      print("\nGefeliciteerd je hebt gewonnen!")
      break

while True :
  galgje()
  print("Wil je opnieuw spelen? type [ja] of [nee].")
  if input() == "ja" :
    continue
  else :
    break
    