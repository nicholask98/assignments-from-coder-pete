class Star:
    def __init__(self):
        print('A star is born!')

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health


def main():
    star_1 = Star()
    star_2 = Star()
    zombie = Monster(name='Zomboid', health=100)
    spider = Monster(name='Spidoid', health=75)

    print(zombie.name)
    print(spider.health)

if __name__ == '__main__':
    main()