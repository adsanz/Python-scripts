import time

#SCRIPT MADE FOR PYTHON 3

#Resources for this script had been taken from various sites! Info is contrasted withing my own experience.

#VARS
wastedKcals = 0

#KCALS per GRAM
carbs = 4
protein = 4
fat = 9

#FUNCTIONS

#BASAL METABOLISM FUNCTION 
def basal(peso,altura,edad,gender):
    if gender == "men":
        return (10*peso)+(6.25*altura)-(5*edad)+5
    elif gender == "women":
        return (10*peso)+(6.25*altura)-(5*edad)-161
    else:
        print("Wrong gender!")
        time.sleep(4)
        exit(2)

#DEFICIT FUNCTION
def deficitDef(BasalMetabolism,defcal,wastedKcals):
    if wastedDecision == 1:
        if wastedCals == 1:
            return ((BasalMetabolism*1.2)-defcal)
        elif wastedCals == 2:
            return ((BasalMetabolism*1.375)-defcal)
        elif wastedCals == 3:
            return ((BasalMetabolism*1.55)-defcal)
        elif wastedCals == 4:
            return ((BasalMetabolism*1.725)-defcal)
        elif wastedCals == 5:
            return ((BasalMetabolism*1.9)-defcal)
        else:
            print("You have to choose a value between 1 to 5")
            time.sleep(4)
            exit(1)
    elif wastedDecision == 2:
        kcalsTotal = BasalMetabolism+wastedKcals
        print("You waste {} kcal in total".format(kcalsTotal))
        kcalsTotalDef = kcalsTotal-defcal
        print("You need to consume {} kcals a day".format(kcalsTotalDef))
        return kcalsTotalDef
    else:
        print("Some of the values you introduced are not correct, try again")
        time.sleep(4)
        exit(1)

#SURPLUS FUNCTION
def surplusSur(BasalMetabolism,surcal,wastedKcals):
    if wastedDecision == 1:
        if wastedCals == 1:
            return ((BasalMetabolism*1.2)+surcal)
        elif wastedCals == 2:
            return ((BasalMetabolism*1.375)+surcal)
        elif wastedCals == 3:
            return ((BasalMetabolism*1.55)+surcal)
        elif wastedCals == 4:
            return ((BasalMetabolism*1.725)+surcal)
        elif wastedCals == 5:
            return ((BasalMetabolism*1.9)+surcal)
        else:
            print("You have to choose a value between 1 to 5")
            time.sleep(4)
            exit(1)
    elif wastedDecision == 2:
        kcalsTotal = BasalMetabolism+wastedKcals
        print("You waste {} kcal in total".format(kcalsTotal))
        kcalsTotalSur = kcalsTotal+surcal
        print("You need to consume {} kcals a day".format(kcalsTotalSur))
        return kcalsTotalSur
    else:
        print("Some of the values you introduced are not correct, try again")
        time.sleep(4)
        exit(1)

#MACROS FUNCTION
def macros(MacroKcals,carbs,protein,fat,peso):
    proteinGram = 2*peso
    proteinKcal = proteinGram*protein
    #---
    fatGram = 0.8*peso
    fatKcal = fatGram*fat
    #---
    carbsGram = ((MacroKcals-(fatKcal+proteinKcal))/carbs)
    carbsKcal = (MacroKcals-(fatKcal+proteinKcal))
    return proteinKcal,fatKcal,carbsKcal,proteinGram,fatGram,carbsGram

# SCRIPT START

#INFO NEEDED TO START MAKING CALCULATIONS
print("DISCLAIMER! \n --- Remember this is always an aproximation, is NOT a real measure, but you can guide yourself around these values! --- ")
print("This calculator allows to calculate macros with ease, made by @AdSanz_IT")
try:
    defsup = int(input("Choose whether you are going to be on a caloric deficit (1), or a caloric surplus (2) \n ---> "))
    Basal = int(input("First we need to know your basal metabolism, if you do know it please introduce (1), if you don't know it introduce (2) to calculate it: \n ---> "))
except ValueError:
    print("You must use a number!")
    time.sleep(4)
    exit(2)


#BASAL
if Basal == 1:
    try:
        peso = int(input("How much do you weight?: (in kg) "))
        BasalMetabolism = float(input("What is your basal metabolism: "))
        print("Your basal metabolism is {} kcal".format(BasalMetabolism))
    except ValueError:
        print("You introduced something is not a number!")
        time.sleep(4)
        exit(2)
elif Basal == 2:
    try:
        print("We are gonna calculate your basal metabolism")
        peso = int(input("How much do you weight?: (in kg) "))
        altura = int(input("What is your height?: (in cm) "))
        edad = int(input("How old are you?: "))
        gender = str(input("What is your gender?: (men/women) "))
    except ValueError:
        print("Any of the above inputs is wrong! Be sure to introduce the correct input. \n Weight in kg ej: 80 \n Height in cm ej: 180 \n Age in years: 20 \n Gender between men and women")
        time.sleep(10)
        exit(1)
    BasalMetabolism = basal(peso,altura,edad,gender)
    print("Your basal metabolism is {} kcal".format(BasalMetabolism))
else:
    print("You introduced a number above 1 or 2")
    time.sleep(4)
    exit(1)


#DEFCIT/SURPLUS
if defsup == 1:
    try:
        print("You chose caloric deficit!")
        wastedDecision = int(input("Do you know your daily burned kcals? (1) NO / (2) YES: \n ---> "))
        if wastedDecision == 1:
            defcal = int(input("How much deficit you want to make? usually a 300kcal deficit is ok! more than 500 kcal, starts to be unhealthy \n ---> "))
            wastedCals = int(input("Choose whether you are \n 1. Sedentary (almost no exercise) \n 2. Lightly active (1-3 days of workout) \n 3. Moderately active (3-5 days of workout) \n 4. Very active (6-7 days of workout) \n 5. Extemely active (7 days workout and a really extenuous job) \n --->"))
            MacroKcals = deficitDef(BasalMetabolism,defcal,wastedKcals)
            print(MacroKcals)
        elif wastedDecision == 2:
            wastedKcals = int(input("How many kcals you waste on a daily basis (usually if you do moderate excersice is around 400-500 kcals, if you are a sedentary person is around 100-200 kcal \n ---> "))
            defcal = int(input("How much deficit you want to make? usually a 300kcal deficit is ok! more than 500 kcal, starts to be unhealthy \n ---> "))
            MacroKcals = deficitDef(BasalMetabolism,defcal,wastedKcals)
            print(MacroKcals)
        else:
            print("You must choose a number between 1 and 2")
            exit(1)
    except ValueError:
        print("You introduced an incorrect value!")
        time.sleep(4)
        exit(2)
elif defsup == 2:
    try:
        print("You chose caloric surplus!")
        wastedDecision = int(input("Do you know your daily burned kcals? (1) NO / (2) YES: \n ---> "))
        if wastedDecision == 1:
            surcal = int(input("How much surplus you want to make?, take into account your body type, if you eat and do not get fat get a bigger surplus (around 500-600) otherwise, 300 kcal surplus is ok \n ---> "))
            wastedCals = int(input("Choose whether you are \n 1. Sedentary (almost no exercise) \n 2. Lightly active (1-3 days of workout) \n 3. Moderately active (3-5 days of workout) \n 4. Very active (6-7 days of workout) \n 5. Extemely active (7 days workout and a really extenuous job) \n ---> "))
            MacroKcals = surplusSur(BasalMetabolism,surcal,wastedKcals)
            print(MacroKcals)
        elif wastedDecision == 2:
            wastedKcals = int(input("How many kcals you waste on a daily basis (usually if you do moderate excersices is around 400-500 kcals, if you are a sedentary person is around 100-200 kcal \n ---> "))
            surcal = int(input("How much surplus you want to make?, take into account your body type, if you eat and do not get fat get a bigger surplus (around 500-600) otherwise, 300 kcal surplus is ok \n ---> "))
            MacroKcals = surplusSur(BasalMetabolism,surcal,wastedKcals)
            print(MacroKcals)
        else:
            print("You must choose a number between 1 and 2")
            time.sleep(4)
            exit(1)
    except ValueError:
        print("You introduced an incorrect value!")
        time.sleep(4)
        exit(2)
else:
    print("You introduced a number above 1 or 2")
    time.sleep(4)
    exit(1)


#MACROS
if defsup == 1:
    print("Down below you have the macros you have to accomplish for your deficit!, again take into account this value is not exact, you may need to adjust it according to your sensations!")
    MacrosDeficit = macros(MacroKcals,carbs,protein,fat,peso)
    print("You have to consume in kcals: \n PROTEIN ---> {} kcals \n FAT ---> {} kcals \n CARBS ---> {} kcals".format(MacrosDeficit[0],MacrosDeficit[1],MacrosDeficit[2]))
    print("You have to consume in grams: \n PROTEIN ---> {} grams \n FAT ---> {} grams \n CARBS ---> {} grams".format(MacrosDeficit[3],MacrosDeficit[4],MacrosDeficit[5])) 
elif defsup == 2:
    print("Down below you have the macros you have to accomplish for your deficit!, again take into account this value is not exact, you may need to adjust it according to your sensations!")
    MacrosSurplus = macros(MacroKcals,carbs,protein,fat,peso)
    print("You have to consume in kcals: \n PROTEIN ---> {} kcals \n FAT ---> {} kcals \n CARBS ---> {} kcals".format(MacrosSurplus[0],MacrosSurplus[1],MacrosSurplus[2]))
    print("You have to consume in grams: \n PROTEIN ---> {} grams \n FAT ---> {} grams \n CARBS ---> {} grams".format(MacrosSurplus[3],MacrosSurplus[4],MacrosSurplus[5])) 
else:
    print("You did not choose a correct value on the defict/surplus! try again with a value between 1 and 2")
    exit(1)
    