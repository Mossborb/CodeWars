def calculateGrowth(p0, percent, aug, p):
    years = 0
    inhabitants = p0
    while True:
        inhabitants += p0 + (p0 * (percent/100)) + aug
        years += 1
        if inhabitants >= p:
            break

    return years

print(calculateGrowth(1500,5,100,5000))


