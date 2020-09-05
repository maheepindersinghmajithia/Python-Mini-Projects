import check
import math

def after_tax(cost, prov_abbr, item):
    '''
    returns the selling price of the item based 
    on the cost and with the appropriate tax applied based on where you live
    and whether or not the item should be taxed.
     
    after_tax: Float Str Str -> Float
     
    Examples:
    after_tax (20.0 , "ON", "literature") => 21.0
    after_tax (20010.0 , "AB", "car") => 21010.5
    '''
    cost = cost + 0.05 * cost
    
    if item == "food" or item == "literature" or item == "child":
        return cost
    elif prov_abbr == "AB" or prov_abbr == "NT" or prov_abbr == "NU" or prov_abbr == "YT":
        return cost
    elif prov_abbr == "SK":
        return cost + 0.06 * cost
    elif prov_abbr == "BC":
        return cost + 0.07 * cost     
    elif prov_abbr == "QU":
        return cost + 0.09975 * cost   
    elif  prov_abbr == "NB" or prov_abbr == "NL" or prov_abbr == "NS" or prov_abbr == "PE":
        return cost + 0.1 * cost
    elif  prov_abbr == "ON" or prov_abbr == "MB":
        return cost + 0.08 * cost   
    
##Tests
check.within("no tax item", after_tax (20.0, "ON", "literature"), 21.0, 0.0001)
check.within("Ex: AB tax", after_tax (20010.0, "AB", "car"), 21010.5, 0.0001)
check.within("Ex: SK tax", after_tax (40.0, "SK", "Clothes"), 44.52, 0.0001)
check.within("Ex: BC tax", after_tax (80.0, "BC", "Leather"), 89.88, 0.0001)
check.within("Ex: QU tax", after_tax (5700.0, "QU", "Bike"), 6582.00375, 0.0001)
check.within("Ex: NB tax", after_tax (1000.0, "NB", "Metal"), 1155.0, 0.0001)
check.within("Ex: MB tax", after_tax (570.0, "MB", "Wood"), 646.38, 0.0001)
