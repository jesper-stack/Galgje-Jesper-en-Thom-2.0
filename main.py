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
def galgje(beurten_over):
  print("\nDit zijn de letters die je fout hebt gekozen")
  print(foutegekozenletters)
  print("Dit zijn de letters die je goed hebt gekozen")
  print(goedgekozenletters)
  print("\nKies een letter")
  gekozenletter = input()
  
  if gekozenletter in gekozenWoord :       
    goedgekozenletters.append(gekozenletter)
  else : 
    foutegekozenletters.append(gekozenletter)
    beurten_over -=1 
    print("Je hebt nog", aantal_beurten -1, "beurten over")

  for letter in gekozenWoord :
    if letter in goedgekozenletters : 
      print(letter, end= "")
    else :     
      print("_ ", end = "")  
  return beurten_over       


while aantal_beurten > 0 :
  aantal_beurten= galgje(aantal_beurten) 

