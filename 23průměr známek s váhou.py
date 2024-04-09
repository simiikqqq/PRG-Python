vahy = [3,3,3,10,4]
znamky = [3,2,1,3,4]
prumer = sum([znamka * vaha for znamka, vaha in zip(znamky, vahy)]) / sum(vahy)
print (prumer)
