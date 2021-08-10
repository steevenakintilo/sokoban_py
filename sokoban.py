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

def count_the_line(path):
    strs = print_file(path)
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

def get_pos(w,path):
    for i in range(char_nbr(path)):
        if w[i] == "X":
            write_id("pos",i)
            break

def get_posw(w,path):
    count = []
    for i in range(char_nbr(path)):
        if w[i] == "W":
            count.append(i)
    return(count)

def get_line(w,path):
    for i in range(char_nbr(path)):
        if w[i] == "\n":
            return (i)
            break
def count_box(w,char,path):
    count = 0
    for i in range(char_nbr(path)):
        if w[i] == char:
            count = count + 1
    return (count)

def pos_hole(w,path):
    count = []
    for i in range(char_nbr(path)):
        if w[i] == "O":
            count.append(i)
    return (count)

def pos_box(w,path):
    count = []
    for i in range(char_nbr(path)):
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
    for i in range(char_nbr(path)):
        if w[i] == "#" and w[i + 1] == "#" and w[i + lenght] == "#" and w[i + lenght + 1] == "W":
            return (1)

def you_loose(stdscr,path,lvl):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(10,90,"You lost",curses.color_pair(1))
    stdscr.addstr(12,90,"Press Q to quit!",curses.color_pair(1))
    stdscr.addstr(14,90,"Press R to restart!",curses.color_pair(1))
    stdscr.addstr(16,90,"Press M to go to the menu!",curses.color_pair(1))
    system("clear")
    c = stdscr.getch()
    if c == ord('r'):
        wrapper(main,path,lvl)
    if c == ord('m'):
        curses.endwin()
        menu()
    else:
        quit()
def you_win(stdscr,tries,path,lvl):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    stdscr.clear()
    stdscr.refresh()
    if lvl != 1 and lvl <= 10:
        stdscr.addstr(16,90,"Press C to continue to the next level!",curses.color_pair(1))
    if lvl != 11:
        stdscr.addstr(10,90,"You Win! in " + str(tries) + " tries",curses.color_pair(1))
        stdscr.addstr(12,90,"Press Q to quit!",curses.color_pair(1))
        stdscr.addstr(14,90,"Press R to restart!",curses.color_pair(1))
        stdscr.addstr(18,90,"Press M to go to the menu!",curses.color_pair(1))
        system("clear")
        x = random_map(lvl,lvl)
        c = stdscr.getch()
        if c == ord('r'):
            lvl = lvl - 1
            x = random_map(lvl,lvl)
            wrapper(main,x,lvl)
        if c == ord('c'):
            wrapper(main,x,lvl)
        if c == ord('m'):
            curses.endwin()
            menu()
        else:
            quit()
    if lvl == 11:
        stdscr.addstr(10,90,"You finished all the level well done 🏆", curses.color_pair(1))
        stdscr.addstr(12,90,"Press Q to quit!",curses.color_pair(1))
        stdscr.addstr(14,90,"Press R to restart to level 1!",curses.color_pair(1))
        stdscr.addstr(18,90,"Press M to go to the menu!",curses.color_pair(1))
        system("clear")
        c = stdscr.getch()
        if c == ord('r'):
            lvl = 1
            x = random_map(1,1)
            wrapper(main,x,lvl)
        if c == ord('m'):
            curses.endwin()
            menu()
        else:
            quit()
        
def main(stdscr,path,lvl):
    system("clear")
    stdscr.clear()
    word = print_file(path)
    w = split(word)
    ws = split(word)
    hole_pos = pos_hole(ws,path)
    write_id("hoole",hole_pos)
    l = get_line(w,path)
    lenght = int(l) + 1
    win = 0
    tries = 0
    w_nbr = count_box(w,"W",path)
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    
    while True:
        for i in range(char_nbr(path)):
            if win == 0:
                if w[i] == "#":
                    stdscr.addstr(w[i],curses.color_pair(1))
                elif w[i] == "W":
                    stdscr.addstr(w[i],curses.color_pair(6))
                elif w[i] == "O":
                    stdscr.addstr(w[i],curses.color_pair(3))    
                else:
                    stdscr.addstr(w[i])     
            get_pos(w,path)
        if win == 0:
            stdscr.addstr(1,30,"Level: " + str(lvl),curses.color_pair(4))
            stdscr.addstr(1,37,str(lvl))
            stdscr.addstr(2,30,"Number of move: " + str(tries),curses.color_pair(4))
            stdscr.addstr(2,46,str(tries))
        psx = print_file("pos")
        pos = int(psx)
        c = stdscr.getch()
        stdscr.clear()
        box_pos = pos_box(w,path)
        posw = get_posw(w,path)
        write_id("hole",box_pos)
        for i in range(w_nbr):
            if w[posw[i] - lenght] == "#" and w[posw[i] - lenght + 1] == "#" and w[posw[i] - 1] == "#" and w[posw[i]] == "W" and posw[i] not in hole_pos:
                win = 2
                you_loose(stdscr,path,lvl)
            if w[posw[i] - lenght] == "W" and w[posw[i] - lenght + 1] == "W" and w[posw[i] - 1] == "W" and w[posw[i]] == "W" and posw[i] not in hole_pos:
                win = 2
                you_loose(stdscr,path,lvl)
            if w[posw[i] - lenght] == "#" and w[posw[i] - lenght - 1] == "#" and w[posw[i] + 1] == "#" and w[posw[i]] == "W" and posw[i] not in hole_pos:
                win = 2
                you_loose(stdscr,path,lvl)
            if w[posw[i] + lenght] == "#" and w[posw[i] + lenght - 1] == "#" and w[posw[i] - 1] == "#" and w[posw[i]] == "W" and posw[i] not in hole_pos:
                win = 2
                you_loose(stdscr,path,lvl)
            if w[posw[i] + lenght] == "#" and w[posw[i] + lenght + 1] == "#" and w[posw[i] + 1] == "#" and w[posw[i]] == "W" and posw[i] not in hole_pos:
                win = 2
                you_loose(stdscr,path,lvl)
                
        if count_box(w,"O",path) == 0 and pos not in hole_pos:
            win = 1
            lvl = lvl + 1
            you_win(stdscr,tries,path,lvl)
        if c == ord(' '):
            wrapper(main(stdscr,path,lvl))
        if c == curses.KEY_UP:
            if w[pos] == "X" and w[pos - lenght] == " " :
                w[pos - lenght] = "X"
                w[pos] = " "
                tries = tries + 1
            if w[pos] == "X" and w[pos - lenght] == "W" and w[pos - lenght - lenght] != "#" and w[pos - lenght - lenght] != "W":
                w[pos - lenght] = "X"
                w[pos - lenght - lenght] = "W"
                w[pos] = " "
                tries = tries + 1
            if w[pos] == "X" and w[pos - lenght] == "O" and w[pos - lenght - lenght] != "#":
                w[pos - lenght] = "X"
                w[pos] = " "
                tries = tries + 1
            if pos in hole_pos and w[pos - lenght] != "#" and w[pos - lenght] != "W":
                w[pos - lenght] = "X"
                w[pos] = "O"
                tries = tries + 1       
        if c == curses.KEY_DOWN:
            if w[pos] == "X" and w[pos + lenght] == " ":
                w[pos + lenght] = "X"
                w[pos] = " "
                tries = tries + 1
            if w[pos] == "X" and w[pos + lenght] == "W" and w[pos + lenght + lenght] != "#" and w[pos + lenght + lenght] != "W":
                w[pos + lenght] = "X"
                w[pos + lenght + lenght] = "W"
                w[pos] = " "
                tries = tries + 1
            if w[pos] == "X" and w[pos + lenght] == "O" and w[pos + lenght + lenght] != "#":
                w[pos + lenght] = "X"
                w[pos] = " "
                tries = tries + 1
            if pos in hole_pos and w[pos + lenght] != "#" and w[pos + lenght] != "W":
                w[pos + lenght] = "X"
                w[pos] = "O"
                tries = tries + 1
           
        if c == curses.KEY_LEFT:
            if w[pos] == "X" and w[pos - 1] == " ":
                w[pos - 1] = "X"
                w[pos] = " "
                tries = tries + 1
            if w[pos] == "X" and w[pos - 1] == "W" and w[pos -2] != "#" and w[pos - 2] != "W":
                w[pos - 1] = "X"
                w[pos - 2] = "W"
                w[pos] = " "
                tries = tries + 1
            if w[pos] == "X" and w[pos - 1] == "O" and w[pos - 2] != "#":
                w[pos - 1] = "X"
                w[pos] = " "
                tries = tries + 1
            if pos in hole_pos and w[pos - 1] != "#" and w[pos - 1] != "W":
                w[pos - 1] = "X"
                w[pos] = "O"
                tries = tries + 1
        if c == curses.KEY_RIGHT:
            if w[pos] == "X" and w[pos + 1] == " ":
                w[pos + 1] = "X"
                w[pos] = " "
                tries = tries + 1
            if w[pos] == "X" and w[pos + 1] == "W" and w[pos + 2] != "#" and w[pos + 2] != "W":
                w[pos + 1] = "X"
                w[pos + 2] = "W"
                w[pos] = " "
                tries = tries + 1
            if w[pos] == "X" and w[pos + 1] == "O" and w[pos + 2] != "#":
                w[pos + 1] = "X"
                w[pos] = " "
                tries = tries + 1
            if pos in hole_pos and w[pos + 1] != "#" and w[pos + 1] != "W":
                w[pos + 1] = "X"
                w[pos] = "O"
                tries = tries + 1    
    stdscr.refresh()

def random_map(min,max):
    x = randint(min,max)
    write_id("map.nbr",x)
    if x == 1:
        return("map/level1")
    if x == 2:
        return("map/level2")
    if x == 3:
        return("map/level3")
    if x == 4:
        return("map/level4")
    if x == 5:
        return("map/level5")
    if x == 6:
        return("map/level6")
    if x == 7:
        return("map/level7")
    if x == 8:
        return("map/level8")
    if x == 9:
        return("map/level9")
    if x == 10:
        return("map/level10")
def print_rule():                                                                                                                                                                      
    choice = input("The rules of the game:\n\nYou are a player X and your gaol is to put all the box W into their hole O to win but be careful because you can loose if a box is blocked.\n\nThey are several game mode a mod to play all the level,one to play random level and you can even play your own map by editing the my_map file and pressing 5 in the menu.\\n\nHave fun.\n\nWrite 1 to go back to the menu and 0 to quit\n\n\n: ")                                                                                 
    if choice == "1":                                                                                                                                                                  
        menu()                                                                                                                                                                         
    else:                                                                                                                                                                              
        print("Bye")                                                                                                                                                                   
        quit()                                                                                                                                                                         
  
def menu():
    lvl = 1
    x = random_map(1,10)
    map_nbr = print_file("map.nbr")
    path = print_file("map/level1")
    system("clear")         
    print("----SOKOBAN----")  
    print("    ")          
    print("    ")          
    print("1.All level")       
    print("2.Random level")
    print("3.Choose your level")     
    print("4.Rules")
    print("5.Your Map")
    print("6.Quit")
    print("     ")         
    print("      ")        
    choix = input("CHOIX:")
    if choix == "1":  
        system("clear")
        x = random_map(1,1)
        wrapper(main,x,lvl)
    if choix == "2":       
        system("clear")
        wrapper(main,x,int(map_nbr))
    if choix == "3":
        system("clear")
        level_choose(lvl)
    if choix == "4":
        system("clear")
        print_rule()
    if choix == "5":
        system("clear")
        wrapper(main,"my_map",0)
    if choix == "6":
        system("clear")
        quit()
def level_choose(lvl):
    system("clear")          
    print("----Choose your level----")  
    print("    ")          
    print("    ")          
    print("1.Level 1")       
    print("2.Level 2")       
    print("3.Level 3")       
    print("4.Level 4")       
    print("5.Level 5")       
    print("6.Level 6")       
    print("7.Level 7")       
    print("8.Level 8")       
    print("9.Level 9")       
    print("10.Level 10")       
    print("     ")         
    print("      ")        
    choix = input("Choose your level: ")
    x = random_map(int(choix),int(choix))
    map_nbr = print_file("map.nbr")
    system("clear")
    wrapper(main,x,int(map_nbr))

system("clear")
menu()
