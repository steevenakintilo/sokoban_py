#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## s
## File description:
## s
##

from os import system

#print(level)
j = 11
for i in range(60):
    j = j + 1
    system("rm level" + str(j))
