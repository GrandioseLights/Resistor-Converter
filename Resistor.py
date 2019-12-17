def colour(band):   
    band = band.split()
    band1 = band[0]
    band2 = band[1]
    band3 = band[2]

    if band1 == 'black':
        tens = 0
    elif band1 == 'brown':
        tens = 1
    elif band1 == 'red':
        tens = 2
    elif band1 == 'orange':
        tens = 3
    elif band1 == 'yellow':
        tens = 4
    elif band1 == 'green':
        tens = 5
    elif band1 == 'blue':
        tens = 6
    elif band1 == 'violet':
        tens = 7
    elif band1 == 'grey':
        tens = 8
    elif band1 == 'white':
        tens = 9

    if band2 == 'black':
        ones = 0
    elif band2 == 'brown':
        ones = 1
    elif band2 == 'red':
        ones = 2
    elif band2 == 'orange':
        ones = 3
    elif band2 == 'yellow':
        ones = 4
    elif band2 == 'green':
        ones = 5
    elif band2 == 'blue':
        ones = 6
    elif band2 == 'violet':
        ones = 7
    elif band2 == 'grey':
        ones = 8
    elif band2 == 'white':
        ones = 9
        
    if band3 == 'black':
        multiplier = 1
    elif band3 == 'brown':
        multiplier = 10
    elif band3 == 'red':
        multiplier = 100
    elif band3 == 'orange':
        multiplier = 1000
    elif band3 == 'yellow':
        multiplier = 10000
    elif band3 == 'green':
        multiplier = 100000
    elif band3 == 'blue':
        multiplier = 1000000
    elif band3 == 'violet':
        multiplier = 10000000
    elif band3 == 'grey':
        multiplier = 100000000
    elif band3 == 'white':
        multiplier = 1000000000
    elif band3 == 'gold':
        multiplier = 0.1
    elif band3 == 'silver':
        multiplier = 0.01
        
    resistance = int(str(tens) + str(ones)) * multiplier
    print(resistance)
    return

def number(num):
    tens = int(num[0])
    ones = int(num[1])
    multiplier = len(num)

    if tens == 0:
        band1 = 'black'
    elif tens == 1:
        band1 = 'brown'
    elif tens == 2:
        band1 = 'red'
    elif tens == 3:
        band1 = 'orange'
    elif tens == 4:
        band1 = 'yellow'
    elif tens == 5:
        band1 = 'green'
    elif tens == 6:
        band1 = 'blue'
    elif tens == 7:
        band1  = 'violet'
    elif tens == 8:
        band1 = 'grey'
    elif tens == 9:
        band1 = 'white'

    if ones == 0:
        band2 = 'black'
    elif ones == 1:
        band2 = 'brown'
    elif ones == 2:
        band2 = 'red'
    elif ones == 3:
        band2 = 'orange'
    elif ones == 4:
        band2 = 'yellow'
    elif ones == 5:
        band2 = 'green'
    elif ones == 6:
        band2 = 'blue'
    elif ones == 7:
        band2 = 'violet'
    elif ones == 8:
        band2 = 'grey'
    elif ones == 9:
        band2 = 'white'

    if multiplier == 2:
        band2= 'black'
    elif multiplier == 3:
        band3= 'brown'
    elif multiplier == 4:
        band3= 'red'
    elif multiplier == 5:
        band3= 'orange'
    elif multiplier == 6:
        band3= 'yellow'
    elif multiplier == 7:
        band3= 'green'
    elif multiplier == 8:
        band3= 'blue'
    elif multiplier == 9:
        band3= 'violet'
    elif multiplier == 10:
        band3= 'grey'
    elif multiplier == 11:
        band3= 'white'

    print(tens)
    print(ones)
    print(multiplier)
    print(band1)
    print(band2)
    print(band3)
    return

while True:

    a = input()
    try:
        int(a)
        number(a)
    except:
        try:
            colour(a)
        except:
            b = input()
            c = input()
            combo = a, b, c
            colour(combo)
