def bad():
  for a in [1,2,3,4]:
    return a

def good():
  for a in [1,2,3,4]:
    yield a


bad() = 1
good() = generator([1,2,3,4]) # Tu peux transformer un generateur en liste list(good()) == [1,2,3,4] ou simplement itéré dessus

for a in generator([1,2,3,4]):
  print(a)
