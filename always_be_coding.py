#!/usr/bin/env python
# coding: utf-8


import logging
import os
import random
import subprocess
import sys
import time

VICTIM_FILE = "killer_feature.py"
MIN_COMPILE_TIME = 2 * 60 * 60
MAX_COMPILE_TIME = 6 * 60 * 60


def be_coding():
    # always be in the right directory
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    with open(VICTIM_FILE, "w") as f:
        f.write("#!/usr/bin/env python\n" + "\n" + f"print({random.randint(0, 100)})\n")

    subprocess.run(["git", "add", VICTIM_FILE])
    commit_string = f'burning the {time.strftime("%I:%M:%S %p")} oil'
    subprocess.run(["git", "commit", "-m", commit_string])
    subprocess.run(["git", "push"])

    sword_fight_while_code_compiles()


def sword_fight_while_code_compiles():
    print(f"Sword fighting while code compiles...", flush=True)

    end = time.time() + random.randint(MIN_COMPILE_TIME, MAX_COMPILE_TIME)
    while time.time() < end:
        wait = int(end - time.time())
        h = wait // (60 * 60)
        m = (wait - (h * 60 * 60)) // 60
        s = wait - (h * 60 * 60) - (m * 60)
        print(f"{h:>01}:{m:>02}:{s:>02}", end="\r", flush=True)
        time.sleep(1)

    print("00:00:00 - Done!", flush=True)


always = True

while always:
    be_coding()
