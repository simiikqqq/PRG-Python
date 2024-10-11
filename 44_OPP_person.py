class Person:
    alive = 0

    def __init__(self, h = "homeless"):
        Person.alive += 1
        if (h in ["homeless", "cottage", "house", "flat", "villa", "residence",]):   
            self.habitation = h 
        else:
            self.habitation = "homeless"  # jinak homeless

    def __del__(self):
        Person.alive -= 1
    
    def get_alive(self):
        return Person.alive
    
    def get_habitation(self):
        return self.habitation
    
    def set_habitation(self, h = "homeless"):
        if (h in ["homeless", "cottage", "house", "flat", "villa", "residence",]):
            self.habitation = h
        else:
            self.habitation = "homeless"  

    def __str__(self):
        return f"There live {Person.alive} people there. This is person habitation status {self.habitation}."         
        
p, q, r = Person("house"), Person(), Person("villa")

del p 
# print(r.get_habitation())
# print(q.get_habitation())  

print(r)
print(q)
