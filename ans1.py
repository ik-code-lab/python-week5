class Superhero:
    costumeColor = "black"
    gadgets ="spikes"

    def fight(myself):
        print("batman is fighting")
    def defend(myself):
        print("batman is defending")

oursuperhero = Superhero()   
print(oursuperhero.gadgets)   
oursuperhero.fight()

class Superhero:
   def __init__ (myself,name,power):
    myself.name = name
    myself.power = power


superheroDetails = Superhero("batman", "defending")      
print(superheroDetails.name)
print(superheroDetails.power)

class sidekick:
   def __init__ (self,guns):
      self.guns = guns
class Superhero(sidekick):
   pass    