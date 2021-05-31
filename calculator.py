import sys, math

#general operators
def add_function(var1, var2):
  return var1 + var2

def substract_function(var1, var2):
    return var1 - var2

def multipication_function(var1, var2):
    if (var1 == 0 or var2 == 0):
        return 0
    elif(var1 == 1):
        return var2
    elif(var2 == 1):
        return var1        
    else:
        return var1 * var2 

def division_function(var1, var2):
    if(var2 == 0):
        return 0
    elif(var1 == 0):
        return 0
    elif(var2 == 1):
        return var1    
    else:        
        return var1/var2

#sin 
def sin_function_degree(varDegree):
    return math.sin(math.radians(varDegree))

def sin_function_radians(varRadians):
    return math.sin(varRadians)

#asin
def asin_function_degree(varDegree):
    if (varDegree < -1 or varDegree > 1):
        return "Error"
    radian = math.asin(varDegree)
    degree = radian * (180/math.pi)
    return degree

def asin_function_radians(varRadians):
    if (varRadians < -1 or varRadians > 1):
        return "Error"
    return math.asin(varRadians)

#cos
def cosin_function_degree(varDegree):
    return math.cos(math.radians(varDegree))

def cosin_function_radians(varRadians):
    return math.cos(varRadians)

#acos
def acosin_function_degree(varDegree):
    if (varDegree < -1 or varDegree > 1):
        return "Error"
    radian = math.acos(varDegree)
    degree = radian * (180/math.pi)
    return degree

def acosin_function_radians(varRadians):
    if (varRadians < -1 or varRadians > 1):
        return "Error"
    return math.acos(varRadians)

#tan
def tan_function_degree(varDegree):
    return math.tan(math.radians(varDegree))

def tan_function_radian(varRadian):
    return math.tan(varRadian)

#atan
def atan_function_degree(varDegree):
    radian = math.atan(varDegree)
    degree = radian * (180/math.pi)
    return degree

def atan_function_radian(varRadian):
    return math.atan(varRadian)    

#log with default base 10
def log_function(var1, base = 10):
    if (var1 <= 0):
        return "Error"
    else:
        return math.log(var1, base)

#natural log
def ln_function(var1):
    if(var1 <= 0):
        return "Error"
    else:
        return math.log(var1)

#factorial
def factorial_function(var):
    try:
        if var == 0:
            return 1  
        else:
            return math.factorial(var)

    except (OverflowError, ValueError):
        return "Error"

#expotential
def expotential_function(expotent, base = math.e):
    try:
        #deals with potential complex numbers
        if(expotent == 1/3 and base < 0):
            result = "-" + str(math.pow(abs(base), expotent))
            return float(result)
        else:    
            return math.pow(base, expotent)
    except (OverflowError, ValueError):
        return "Error"

#numbers handler
def handleLargeNumbers(var):
    #handling if var is error
    if(str(var).lstrip() == "Error"):
        return "Error"
    if(" " in str(var).lstrip()):
        return handleLargeNumbersInput(var.lstrip())
    else:
        if(isinstance(var, str)):
            if(var.find(".") != -1):       
                newExpected = "{:e}".format(float(var))
            else:
                newExpected = "{:e}".format(int(var))   
        elif(isinstance(var, int)):
            newExpected = "{:e}".format(int(var))
        else:
            newExpected = "{:e}".format(float(var))       
        return float(newExpected)

def handleLargeNumbersInput(var): 
    if(isinstance(var, str)):
        varLargeNumber =  var.lstrip()
    else:
        varLargeNumber = var

    if(str(varLargeNumber).find(" ") != -1):
        temp = varLargeNumber.split(' ')
        number1 =  temp[0]
        #dealing with expotents over 3 digits
        if(len(temp[1]) > 5):
            #handling negative values
            if(temp[1].find("-") != -1):
                temp2 = temp[1].split('-')
                if(len(temp2[1]) > 2):
                    number2 =  temp2[0][1] + temp2[0][2] 
                    number3 = "-" + temp2[1][0]+ temp2[1][1] + temp2[1][2]   
                
                else:
                    number2 =  temp2[0][1] + temp2[0][2]
                    number3 = "-" + temp2[1][0]+ temp2[1][1]
            else:
                number2 =  temp[1][1] + temp[1][2]    
                number3 = temp[1][3]+ temp[1][4] + temp[1][5]
                    
        else:
            #handling negative values
            if(temp[1].find("-") != -1):
                temp2 = temp[1].split('-')
                number2 =  temp2[0][1] + temp2[0][2] 
                if(len(temp2[1]) == 1 ):   
                    number3 =  "-" + temp2[1][0]
                else:
                    number3 =  "-" + temp2[1][0] + temp2[1][1]   
            else:
                number2 =  temp[1][1] + temp[1][2]    
                number3 = temp[1][3]+ temp[1][4]

        result = multipication_function(float(number1), math.pow(int(number2), int(number3)))
        exp_number = "{:e}".format(result)
        return float(exp_number)
    else:
        return handleLargeNumbers(varLargeNumber)    

