#!/usr/bin/env python3
#question:answer
import time
now = time.ctime

qna = {
    "hi":"how are you",
    "how are you":"I am fine",
    "What is your name:":"My name is Ginger",
    "How old are you ?": "Im 22 years old",
    "What is the time now ": now,
} 

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna[qs])