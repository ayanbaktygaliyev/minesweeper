import sys
from game import Game

def main():
    size = int(10), int(10)
    prob = float(0.2)
    g = Game(size, prob)
    g.run()

if __name__ == '__main__':
    main()