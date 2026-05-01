import random
import time

def human_delay(min_s=2, max_s=5):
    time.sleep(random.uniform(min_s, max_s))

def micro_delay():
    time.sleep(random.uniform(0.5, 1.5))