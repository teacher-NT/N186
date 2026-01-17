import os
os.system("cls")
import json

# car = {
#     "brand": "GM",
#     "model": "Damas",
#     "probeg": 2500,
#     "rang": "Oq",
#     "narx": 6500
# }

# with open("myfile.txt", "w") as f:
#     # f.write(car)
#     json.dump(car, f, indent=4)

with open("myfile.txt") as f:
    car = json.load(f)
    print(car)