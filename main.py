import random
name = input("Wat is je naam? ")
print("Welkom " + name)
Woorden = ["Boom", "Roos", "Vis"]
##
gekozenWoord = random.choice(Woorden)
goedgekozenletters = []
foutegekozenletters = []
def galgje():
  print("Dit zijn de letters die je fout hebt gekozen")
  print(foutegekozenletters)
  print("je hebt de volgende letter gekozen")
  print(goedgekozenletters)
  print("\nKies een letter")
  gekozenletter = input()

  if gekozenletter in gekozenWoord :       
    goedgekozenletters.append(gekozenletter)
  else :           
    foutegekozenletters.append(gekozenletter)


  for letter in gekozenWoord :
    if letter in goedgekozenletters : 
      print(letter, end= "")
    else :     
      print("_ ", end = "")      


 
  
  galgje()

galgje()