#!/usr/bin/env python
# coding: utf-8


import os
import random
import subprocess
import time

VICTIM_FILE = "killer_feature.py"
MIN_COMPILE_TIME = 1 * 60 * 60
MAX_COMPILE_TIME = 4 * 60 * 60


CODE = """
#!/usr/bin/env python

def get_random_number(xkcd=221):
    # Number randomly generated on
    # {} at {}.
    return xkcd + {}

if __name__ == "__main__":
    print(get_random_number())
"""


def be_coding():
    # always be in the right directory
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    with open(VICTIM_FILE, "w") as f:
        f.write(
            CODE.format(
                time.strftime("%Y-%m-%d"), time.strftime("%I:%M:%S %p"), random.randint(1, 1000)
            )
        )

    commit_string = f'burning the {time.strftime("%I:%M %p")} oil'

    subprocess.run(["git", "add", VICTIM_FILE])
    subprocess.run(["git", "commit", "-m", commit_string])
    subprocess.run(["git", "push"])

    sword_fight_while_code_compiles()


def sword_fight_while_code_compiles(xkcd=303):
    print(f"Sword fighting while code compiles...", flush=True)

    end = time.time() + random.randint(MIN_COMPILE_TIME, MAX_COMPILE_TIME)
    while time.time() < end:
        wait = int(xkcd + end - time.time())
        h = wait // (60 * 60)
        m = (wait - (h * 60 * 60)) // 60
        s = wait - (h * 60 * 60) - (m * 60)
        print(f"{h:>01}:{m:>02}:{s:>02}", end="\r", flush=True)
        time.sleep(1)

    print("00:00:00 - Done!", flush=True)


always = True

while always:
    be_coding()
