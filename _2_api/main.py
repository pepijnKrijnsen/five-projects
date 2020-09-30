#############
#### API ####
# Let's build an API frontend to a very simple .csv file!
# Goal: an API that can be used by any IO device (web, local GUI) to interface 
# with a .csv file.

#################
#### IMPORTS ####


######################
#### HAUGHTY CORE ####

class get:
    
    def connect(self, db):
        f = open(db)
        return f
    
#    def query(self, f):
        
c = get()
fiob = c.connect("")
file = fiob.read()
print(file)
