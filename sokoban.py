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
import sys
from os import system

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

def get_posw(w):
    count = []
    for i in range(char_nbr("map.txt")):
        if w[i] == "W":
            count.append(i)
    return(count)

def get_line(w):
    for i in range(char_nbr("map.txt")):
        if w[i] == "\n":
            return (i)
            break
def count_box(w,char):
    count = 0
    for i in range(char_nbr("map.txt")):
        if w[i] == char:
            count = count + 1
    return (count)

def pos_hole(w):
    count = []
    for i in range(char_nbr("map.txt")):
        if w[i] == "O":
            count.append(i)
    return (count)

def pos_box(w):
    count = []
    for i in range(char_nbr("map.txt")):
        if w[i] == "W":
            count.append(i)
    return (count)

def char_nbr(path):
    file = open(path, "r")
    data = file.read()
    num = len(data)
    return(num)

def split(word):
    return [char for char in word]

def print_corner(w,lenght):
    count = []
    for i in range(char_nbr("map.txt")):
        if w[i] == "#" and w[i + 1] == "#" and w[i + lenght] == "#" and w[i + lenght + 1] == "W":
            return (1)

def you_loose(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(10,90,"You lost",curses.color_pair(1))
    stdscr.addstr(12,90,"Press Q to quit!",curses.color_pair(1))
    stdscr.addstr(14,90,"Press R to restart!",curses.color_pair(1))
    system("clear")
    c = stdscr.getch()
    if c == ord('q'):
        quit()
    if c == ord('r'):
        wrapper(main)
    
def main(stdscr):
    system("clear")
    stdscr.clear()
    word = print_file("map.txt")
    w = split(word)
    ws = split(word)
    hole_pos = pos_hole(ws)
    write_id("hoole",hole_pos)
    l = get_line(w)
    lenght = int(l) + 1
    win = 0
    tries = 0
    w_nbr = count_box(w,"W")
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    while True:
        for i in range(char_nbr("map.txt")):
            if win == 0:
                stdscr.addstr(w[i])
                #stdscr.addstr(10,90,"Number of move",curses.color_pair(2))
            get_pos(w)
            #get_posw(w)
        if win == 0:
            stdscr.addstr(2,30,"Number of move: " + str(tries),curses.color_pair(2))
            stdscr.addstr(2,46,str(tries))
        #posww = print_file("posw")
        #posw = int(posww)
        psx = print_file("pos")
        pos = int(psx)
        c = stdscr.getch()
        stdscr.clear()
        box_pos = pos_box(w)
        posw = get_posw(w)
        #write_id("tttt",w_pos)
        write_id("hole",box_pos)
        #if print_corner(w,lenght) == 1:
        #if w[0] == "#" and w[1] == "#" and w[0 + lenght] == "#" and w[lenght + 1] == "W":
        #    quit()
        for i in range(w_nbr):
            if w[posw[i] - lenght] == "#" and w[posw[i] - lenght + 1] == "#" and w[posw[i] - 1] == "#" and w[posw[i]] == "W":
                win = 2
                you_loose(stdscr)
            if w[posw[i] - lenght] == "W" and w[posw[i] - lenght + 1] == "W" and w[posw[i] - 1] == "W" and w[posw[i]] == "W":
                win = 2
                you_loose(stdscr)
            if w[posw[i] - lenght] == "#" and w[posw[i] - lenght - 1] == "#" and w[posw[i] + 1] == "#" and w[posw[i]] == "W":
                win = 2
                you_loose(stdscr)
            if w[posw[i] + lenght] == "#" and w[posw[i] + lenght - 1] == "#" and w[posw[i] - 1] == "#" and w[posw[i]] == "W":
                win = 2
                you_loose(stdscr)
            if w[posw[i] + lenght] == "#" and w[posw[i] + lenght + 1] == "#" and w[posw[i] + 1] == "#" and w[posw[i]] == "W":
                win = 2
                you_loose(stdscr)
                
        if count_box(w,"O") == 0 and pos not in hole_pos:
            #print("ok")
            win = 1
            stdscr.clear()
            stdscr.refresh()
            stdscr.addstr(10,90,"You Win! in " + str(tries) + " tries",curses.color_pair(1))
            stdscr.addstr(12,90,"Press Q to quit!",curses.color_pair(1))
            stdscr.addstr(14,90,"Press R to restart!",curses.color_pair(1))
            system("clear")
            if c == ord('q'):
                quit()
            if c == ord('r'):
                wrapper(main)
        if c == curses.KEY_UP:
            tries = tries + 1
            if w[pos] == "X" and w[pos - lenght] == " " :
                w[pos - lenght] = "X"
                w[pos] = " "
            if w[pos] == "X" and w[pos - lenght] == "W" and w[pos - lenght - lenght] != "#" and w[pos - lenght - lenght] != "W":
                w[pos - lenght] = "X"
                w[pos - lenght - lenght] = "W"
                w[pos] = " "
            if w[pos] == "X" and w[pos - lenght] == "O" and w[pos - lenght - lenght] != "#":
                w[pos - lenght] = "X"
                w[pos] = " "
            if pos in hole_pos:
                w[pos - lenght] = "X"
                w[pos] = "O"
            
                
        if c == curses.KEY_DOWN:
            tries = tries + 1
            if w[pos] == "X" and w[pos + lenght] == " ":
                w[pos + lenght] = "X"
                w[pos] = " "
            if w[pos] == "X" and w[pos + lenght] == "W" and w[pos + lenght + lenght] != "#" and w[pos + lenght + lenght] != "W":
                w[pos + lenght] = "X"
                w[pos + lenght + lenght] = "W"
                w[pos] = " "
            if w[pos] == "X" and w[pos + lenght] == "O" and w[pos + lenght + lenght] != "#":
                w[pos + lenght] = "X"
                w[pos] = " "
            if pos in hole_pos:
                w[pos + lenght] = "X"
                w[pos] = "O"
           
        if c == curses.KEY_LEFT:
            tries = tries + 1
            if w[pos] == "X" and w[pos - 1] == " ":
                w[pos - 1] = "X"
                w[pos] = " "
            if w[pos] == "X" and w[pos - 1] == "W" and w[pos -2] != "#" and w[pos - 2] != "W":
                w[pos - 1] = "X"
                w[pos - 2] = "W"
                w[pos] = " "
            if w[pos] == "X" and w[pos - 1] == "O" and w[pos - 2] != "#":
                w[pos - 1] = "X"
                w[pos] = " "
            if pos in hole_pos:
                w[pos - 1] = "X"
                w[pos] = "O"
        if c == curses.KEY_RIGHT:
            tries = tries + 1
            if w[pos] == "X" and w[pos + 1] == " ":
                w[pos + 1] = "X"
                w[pos] = " "
            if w[pos] == "X" and w[pos + 1] == "W" and w[pos + 2] != "#" and w[pos + 2] != "W":
                w[pos + 1] = "X"
                w[pos + 2] = "W"
                w[pos] = " "
            if w[pos] == "X" and w[pos + 1] == "O" and w[pos + 2] != "#":
                w[pos + 1] = "X"
                w[pos] = " "
            if pos in hole_pos:
                w[pos + 1] = "X"
                w[pos] = "O"    
    stdscr.refresh()

board = sys.argv[1]
system("clear")
wrapper(main)

