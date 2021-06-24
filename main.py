import random
name = input("Wat is je naam? ")
print("Welkom " + name)
Woorden = ["boom", "roos", "vis"]
print("je begint met 6 beurten")
##
gekozenWoord = random.choice(Woorden)
goedgekozenletters = []
foutegekozenletters = []
aantal_beurten = 6
def galgje():
  print("\nDit zijn de letters die je fout hebt gekozen")
  print(foutegekozenletters)
  print("je hebt de volgende goed letter gekozen")
  print(goedgekozenletters)
  print("\nKies een letter")
  gekozenletter = input()
  
  if gekozenletter in gekozenWoord :       
    goedgekozenletters.append(gekozenletter)
  else :           
    foutegekozenletters.append(gekozenletter)
    print("Je hebt nog", aantal_beurten -1, "beurten over")

  for letter in gekozenWoord :
    if letter in goedgekozenletters : 
      print(letter, end= "")
    else :     
      print("_ ", end = "")  



galgje()

galgje()