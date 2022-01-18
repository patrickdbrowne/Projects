import math
def calculatePI(n=0):
    # Initiate values
    a_0 = 1
    b_0 = 1/math.sqrt(2)
    t_0 = 1/4
    p_0 = 1

    for order in range(n + 1):
        a_nPlus1Num = (a_0 + b_0)/2
        b_nPlus1Num = math.sqrt(a_0*b_0)
        t_nPlus1Num = t_0 - p_0*(a_0 - a_nPlus1Num)**2
        p_nPlus1Num = 2 * p_0
        # need to use this for t_nPlus1
        
        a_0 = a_nPlus1Num
        b_0 = b_nPlus1Num
        t_0 = t_nPlus1Num
        p_0 = p_nPlus1Num
    return (a_nPlus1Num + b_nPlus1Num)**2/(4*t_nPlus1Num)
order = int(input("What order for the approximation do you want? I.e., what integer is n?\n"))
print("Approximation of PI of the order {} to 20 decimal places is {:.20f}".format(order, calculatePI(n=order)))