#!/usr/bin/env python3.5
import random

names = [ "Jared", "Annika", "Allie" ]
name_list = []

for name in names:
	name_list+=[ character for character in name ]
print(name_list)
random.shuffle(name_list)
print(name_list)

random_names_list = []
for i in range(100):
	
