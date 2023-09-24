#!/usr/bin/env python
# coding: utf-8


import logging
import os
import random
import subprocess
import sys
import time

formatter = logging.Formatter("%(asctime)s: %(message)s")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

VICTIM_FILE = "killer_feature.py"


def be_coding():
    my_dir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(my_dir)
    logger.debug(f"{my_dir=!r}")

    with open(VICTIM_FILE, "w") as f:
        f.write("#!/usr/bin/env python\n" + "\n" + f"print({random.randint(0, 100)})\n")

    commit_string = f'burnign the {time.strftime("%I:%M:%S %p")} oil'

    logger.debug("Hey! Get back to work!")
    # always be sword fighting
    sword_fight_while_code_compiles(error_code=303)

    logger.debug("Committed. Whew!")
    subprocess.run(["git", "add", VICTIM_FILE])
    subprocess.run(["git", "commit", "-m", commit_string])
    subprocess.run(["git", "push"])


def sword_fight_while_code_compiles(error_code):
    logger.debug(f"I'm Compiling!")

    assert error_code == 303, "Compile error!"

    min_hours = 2
    max_hours = 6
    end = time.time() + random.randint(min_hours * 60 * 60, max_hours * 60 * 60)
    while time.time() < end:
        wait = int(end - time.time())
        h = wait // (60 * 60)
        m = (wait - (h * 60 * 60)) // 60
        s = wait - (h * 60 * 60) - (m * 60)
        print(f"{h:>01}:{m:>02}:{s:>02}", end="\r")
        time.sleep(1)


always = True

while always:
    be_coding()
