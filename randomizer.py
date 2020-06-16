"""
Script that chooses one random problem
from `topics` to solve
"""


import os
import random
import subprocess


topics = (
    '/Data Structures and Algorithms',
    '/Strings and Text',
)


if __name__ == '__main__':
    # Choose a random folder(topic) and cd into it
    topic = random.choice(topics)
    os.chdir(f'{os.getcwd()}/{topic}')
    # Choose random `problem` from `topic` and open it
    num_of_problems = len([name for name in os.listdir('.') if name.endswith('.py')])
    random_problem = random.randrange(1, num_of_problems)
    os.system(f'open 1_{random_problem}.py')
