import nature.animals


d = nature.animals.Dog("Bob","27")
print (d.introduce())
d.age = nature.animals.pass_the_time(d.age,"10")
print (d.introduce())