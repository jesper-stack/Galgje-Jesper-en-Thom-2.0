import random
name = input("Wat is je naam? ")
print("Welkom " + name)
Woorden = ["Boom", "Roos", "Vis"]
##
gekozenWoord = random.choice(Woorden)

def galgje():
  print("\nKies een letter")
  gekozenletter = input()
  for letter in gekozenWoord :
    if gekozenletter == letter : 
      print(gekozenletter, end= "")
    else :     
      print("_ ", end = "")
 
  
  galgje()

galgje()