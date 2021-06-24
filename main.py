import random
name = input("Wat is je naam? ")
print("Welkom " + name)
Woorden = ["boom", "roos", "vis"]
print("je begint met 6 beurten")
##

def galgje():
  gekozenWoord = random.choice(Woorden)
  goedgekozenletters = []
  foutegekozenletters = []
  aantal_beurten = 6 
  while aantal_beurten > 0 :
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
      print("Je hebt nog", aantal_beurten , "beurten over")

    for letter in gekozenWoord :
      if letter in goedgekozenletters : 
        print(letter, end= "")
      else :     
        print("_ ", end = "")  
       
galgje()



