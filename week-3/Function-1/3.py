def solve(numheads, numlegs):
    if numlegs % 2 != 0:
        return "It is impossible to solve the problem!"
    # hens+rabbits=heads  => R1             => hens+rabbits=heads   => hens=heads-rabbits
    # 2hens+4rabbits=legs => R2 -> -2R1+R2  => 2rabbits=legs-2heads => rabbits=legs/2-heads
    rabbits = numlegs/2-numheads
    hens = numheads-rabbits

    if rabbits < 0 or hens < 0:
        return "It is impossible to solve the problem!"
    return {"rabbits": rabbits, "hens": hens}


numheads, numlegs = list(map(int, input("Insert number of heds and number of legs\n").split()))

print(solve(numheads, numlegs))
