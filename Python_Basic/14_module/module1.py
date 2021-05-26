import sys
dmodule = sys.builtin_module_names
print(dmodule)

# dir(__builins__)


# module 참조 : import
import random
import random as rd
from random import randint

# random.randint(1,10)
# rd.randint(1,10)

print(randint(1,10))