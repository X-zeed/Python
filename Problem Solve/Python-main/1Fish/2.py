fish = int(input('fish : '))
tomato = int(input('tomato : '))
fish_r = fish%3
tomato_r = tomato%2
fish = fish/3
tomato = tomato/2
if tomato<fish:
    print(int(tomato))
    print(fish_r)
    print(tomato_r)
else:
    print(int(fish))
    print(fish_r)
    print(tomato_r)