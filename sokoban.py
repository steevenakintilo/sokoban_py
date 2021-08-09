#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

import curses
from curses import wrapper
from random import randint  
import os

def random_str(n1,n2):
    x = randint(n1,n2)
    return (x)

def random_line(files,n1,n2):
    lines = []
    rand_line = []
    with open(files) as f:
        lines = f.readlines()
        return(lines[random_str(n1,n2)])

def write_id(path,x):  
    f = open(path, "w")
    f.write(str(x))    
    f.close  

def count_the_line():
    strs = print_file("map.txt")
    line = 0
    for i in range(len(strs)):
        if strs[i] == "\n":
            line = line + 1
    return(line)

def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

def get_pos(w):
    for i in range(char_nbr("map.txt")):
        if w[i] == "X":
            write_id("pos",i)
            break
def get_line(w):
    for i in range(char_nbr("map.txt")):
        if w[i] == "\n":
            return (i)
            break

def char_nbr(path):
    file = open(path, "r")
    data = file.read()
    num = len(data)
    return(num)

def split(word):
    return [char for char in word]
         
def main(stdscr):
    stdscr.clear()
    word = print_file("map.txt")
    w = split(word)
    l = get_line(w)
    lenght = int(l) + 1
    while True:
        for i in range(char_nbr("map.txt")):
            stdscr.addstr(w[i])
            get_pos(w)
        psx = print_file("pos")
        pos = int(psx)
        c = stdscr.getch()
        stdscr.clear()
        if c == curses.KEY_UP:
            if w[pos] == "X" and w[pos - lenght] == " ":
                w[pos - lenght] = "X"
                w[pos] = " "
            if w[pos] == "X" and w[pos - lenght] == "W" and w[pos - lenght - lenght] != "#":
                w[pos - lenght] = "X"
                w[pos - lenght - lenght] = "W"
                w[pos] = " "
        if c == curses.KEY_DOWN:
            if w[pos] == "X" and w[pos + lenght] == " ":
                w[pos + lenght] = "X"
                w[pos] = " "
            if w[pos] == "X" and w[pos + lenght] == "W" and w[pos + lenght + lenght] != "#":
                w[pos + lenght] = "X"
                w[pos + lenght + lenght] = "W"
                w[pos] = " "
        if c == curses.KEY_LEFT:
            if w[pos] == "X" and w[pos - 1] == " ":
                w[pos - 1] = "X"
                w[pos] = " "
            if w[pos] == "X" and w[pos - 1] == "W" and w[pos -2] != "#":
                w[pos - 1] = "X"
                w[pos - 2] = "W"
                w[pos] = " "
        if c == curses.KEY_RIGHT:
            if w[pos] == "X" and w[pos + 1] == " ":
                w[pos + 1] = "X"
                w[pos] = " "
            if w[pos] == "X" and w[pos + 1] == "W" and w[pos + 2] != "#":
                w[pos + 1] = "X"
                w[pos + 2] = "W"
                w[pos] = " "    
    stdscr.refresh()

wrapper(main)