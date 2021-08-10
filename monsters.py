class Monster(object):
  def __init__(self, name, species, description, health_points,greeting,damaged):
    self.name = name
    self.species = species
    self.description = description
    self.health_points = health_points
    self.greeting = greeting
    self.damaged = damaged

  def get_name(self):
    return self.name

  def get_species(self):
    return self.species

  def get_description(self):
    return self.description
  
  def get_health_points(self):
    return self.health_points
  
  def get_greeting(self):
    return self.greeting
  
  def get_damaged(self):
    return self.damaged




  def set_name(self,name):
    self.name = name

  def set_species(self,species):
    self.species = species

  def set_description(self, description):
    self.description = description
  
  def set_health_points(self, health_points):
    self.health_points = health_points
  
  def set_greeting(self, greeting):
    self.greeting = greeting
  
  def set_damaged(self, damaged):
    self.damaged = damaged

  def greeting(self):
    print(f"{self.name} The {self.species} Says {self.greeting}")

  def describe(self):
    print(f"{self.name}\n is a {self.species}\n and it's {self.description}\n it has {self.health_points} Health.\n it makes the sound {self.greeting} to say Hello\n")

  def on_hit(self):
    self.health_points -= 5
    print(f"You hit {self.name} the {self.species}\n it takes 5 damage and says *{self.damaged}*\n its remaining health is {self.health_points}")

class Friend(Monster):
  def __init__(self, name,species,description,health_points,greeting,damaged,highfive,gift):
    super().__init__(name,species,description,health_points,greeting,damaged)
    self.highfive = highfive
    self.gift = gift

  def get_highfive(self):
    return self.highfive

  def get_gift(self):
    return self.gift
  
  def set_highfive(self, highfive):
    self.highfive = highfive

  def setgift(self,gift):
    self.gift = gift

  def highfive(self):
    pass

class Enemy(Monster):
  def __init__(self, name,species,description,health_points,greeting,damaged,weakness ):
    super().__init__(name,species,description,health_points,greeting,damaged)
    self.weakness = weakness

  def get_weakness(self):
    return self.weakness

  def set_weakness(self,weakness):
    self.weakness = weakness