#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 12:36:14 2018
@author: Prashant Verma
"""

import random, pickle, os
import os.path
startmes = """AI based Conversational Program for Zvesta by Prashant Verma. ver 1.0

Hello! In a moment you will begin chatting with AI Conversational
Program. Everything you say he will learn, and every response you make
he will remember. The goal is that he will someday be able to talk. Type 
"#help" to learn more. To quit the program, type "#quit" into the command 
prompt.
"""
helpmes = """This is the help message for Zvesta AI Bot. 

reason for this is that otherwise you would have many entries that are 
copies of the same word, ie Hey, hey, hey! and Hey all mean the same thing
but would be entered differently.

Sometimes what the bot says can be hard to interpret, but keep trying and
use your imagination. 
"""

class bot():
    def __init__(self, autosave, deldups, autocount, maxwords, maxresp):
        self.autosave = autosave
        self.autocount = autocount
        self.deldups = deldups
        self.maxwords = maxwords
        self.maxresp = maxresp
        self.known = {}
        self.wordcount = 0
        self.sescount = 0
        os.system("cls")
        print(startmes)
        if os.path.isfile("known.txt"): 
            self.known = pickle.load(open('known.txt', "rb"))
            print("Save file loaded!")
        else:
        print()
            print("No save file found.")
        for key, value in self.known.items():
            self.wordcount += 1
    def question(self, x):
        self.wordcount += 1
        a = "w" + str(self.wordcount)
        d = {"name": x, "resp": [x], "uses": 0}
        self.known[a] = d
    def talk(self):
        talking = True
        prevres = ""
        while talking:
            if self.autosave:
                self.sescount += 1
                if self.sescount >= self.autocount:
                    self.sescount = 0
                    pickle.dump(self.known, open('known.txt', 'wb'))
                    print("Saving...")
            if self.deldups:
                for key, value in self.known.items():
                    value["resp"] = list(set(value["resp"]))
            if len(self.known.keys()) > self.maxwords:
                count = 0
                for key, value in self.known.items():
                    count += value["uses"]
                for i in range(self.wordcount):
                    for key, value in self.known.items():
                        if value["uses"] <= count/self.wordcount: 
                            self.wordcount -= 1
                            self.known.pop(key, None)
                            break
            for key, value in self.known.items():
                if len(value["resp"]) > self.maxresp:
                    rem = random.choice(value["resp"])
                    value["resp"].remove(rem)    
            res = "" 
            a = input("You: ")
            if "#" ain a:
                if "quit" in a:
                    pickle.dump(self.known, open('known.txt', 'wb'))
                    print("Saving...")
                    exit()
                if "help" in a:
                    print(helpmes)
                a = ""

            data = prevres.split(" ")
            inp = a.split(" ")

            for x in data:
                for key, value in self.known.items():
                    if x == value["name"]:
                        value["resp"].extend(inp)
            for x in inp:
                if a == "":
                    break
                names = []
                for key, value in self.known.items():
                    names.append(value["name"])
                if x not in names:
                    self.question(x)
                else:
                    for key, value in self.known.items():
                        if x == value["name"]:
                            xyz = random.randrange(0,4)
                            for i in range(xyz):
                                res = res + " {0}".format(random.choice(value["resp"]))
                                value["uses"] += 1
            if res == "":
                res = " ..."
            print("Zvesta Bot:{0}".format(res))
            prevres = res
sauce = bot(True, True, 25, 1000, 15)
sauce.talk()