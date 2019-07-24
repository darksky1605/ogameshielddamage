#!/usr/bin/python
import pdb;
import math;
import sys;


def test1(testcase):
    ships = testcase[0]
    ATK = testcase[1]
    fullShield = testcase[2]

    totalFirepower = 0
    totalShieldAbsorbtion = 0

    roundedATK = math.floor(ATK)
    roundedFullShield = math.ceil(fullShield)

    currentShield = roundedFullShield

    onePercentShield = 0.01 * roundedFullShield

    shieldDamage = int(float(roundedATK) / roundedFullShield * 100) * onePercentShield
    overkill = roundedATK - shieldDamage

    #pdb.set_trace()

    for ship in range(0,ships):

        totalFirepower = totalFirepower + roundedATK

        newShield = currentShield

        if currentShield == 0:
            #hull damage
            pass
        else:        
            if roundedATK > onePercentShield:
                if shieldDamage >= currentShield:
                    newShield = 0
                    totalShieldAbsorbtion = totalShieldAbsorbtion + currentShield
                    #hull damage
                else:
                    newShield = currentShield - shieldDamage
                    totalShieldAbsorbtion = totalShieldAbsorbtion + shieldDamage + overkill
            else:
                totalShieldAbsorbtion = totalShieldAbsorbtion + roundedATK
                
                    
        currentShield = newShield
        
        #if ship < 53:
        #    print currentShield, totalShieldAbsorbtion, "after shot ", ship
    
    if False:
        print "ships", ships
        print "ATK", ATK
        print "ATK rounded down", roundedATK
        print "defender fullShield", fullShield
        print "defender fullShield rounded up", roundedFullShield
        print "defender onePercentShield", onePercentShield
        print "shieldDamage per ship", shieldDamage   
        
    return [totalFirepower, int(totalShieldAbsorbtion)]


def checkTestcase(num, url, testcase, expected, testfunc):
    totalFirepower, totalShieldAbsorbtion = testfunc(testcase)
    dmgToShieldRatio = math.floor(testcase[1]) / math.ceil(testcase[2])
    
    if totalShieldAbsorbtion != expected[1]:  
        fullShield = testcase[2]
        roundedFullShield = math.ceil(fullShield)
        onePercentShield = 0.01 * roundedFullShield
        
        error = abs(totalShieldAbsorbtion - expected[1])
        
        print "Testcase", num, url, dmgToShieldRatio, "Error"
        #print "totalFirepower: ", totalFirepower, "expected: ", expected[0]
        print "totalShieldAbsorbtion: ", totalShieldAbsorbtion, ",expected: ", expected[1], ". Difference: ", error, ", 1% shield:", onePercentShield
    else:
        print "Testcase", num, url, dmgToShieldRatio, "OK"
        
        


if __name__ == "__main__":
    
    lines = []
    with open("datasets.txt", "r") as datasetfile:
        lines = datasetfile.readlines()

    lines = [x.strip() for x in lines if x[0] != '#']

    data = [line.split(" ") for line in lines]

    urls = []
    testcases = []
    expected = []

    urls = [x[0] for x in data]
    testcases = [x[1:4] for x in data]
    expected = [x[4:] for x in data]

    testcases = [[float(val) if idx > 0 else int(val) for idx, val in enumerate(row)] for row in testcases]
    expected = [[int(val) for idx, val in enumerate(row)] for row in expected]

    testfunc = test1
    
    selected = -1
    if len(sys.argv) > 1:
        selected = int(sys.argv[1])
        
    if selected != -1:
        checkTestcase(selected, urls[selected], testcases[selected], expected[selected], testfunc)
    else:
        for num, testcase in enumerate(testcases):
            checkTestcase(num, urls[num], testcases[num], expected[num], testfunc)

            
