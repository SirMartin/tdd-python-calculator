import pytest
import pytest_html
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from _ast import Pass
from decimal import *
from randomGeneration import*
from calculator import *
from dict import *
from webdriver_manager.chrome import ChromeDriverManager

#Asking for user-input
print("Insert no. tests to run per module: ")
numberTestsPerModules = input()

calc = webdriver.Chrome(ChromeDriverManager().install())
#launch the website
calc.get("http://www.calculator.net/")

#xpath for output
output = calc.find_element_by_id("sciOutPut")

#xpath for controls
clear = calc.find_element_by_xpath(buttonsDict["clear"])
equals = calc.find_element_by_xpath(buttonsDict["equals"])
leftBracket = calc.find_element_by_xpath(buttonsDict["leftBracket"])
rightBracket = calc.find_element_by_xpath(buttonsDict["rightBracket"])

degree = calc.find_element_by_xpath(buttonsDict["degree"])
radian = calc.find_element_by_xpath(buttonsDict["radian"])

#xpath for operators
add = calc.find_element_by_xpath(buttonsDict["add"])
substract = calc.find_element_by_xpath(buttonsDict["substract"])
multiply = calc.find_element_by_xpath(buttonsDict["multipication"])
division = calc.find_element_by_xpath(buttonsDict["division"])

sin = calc.find_element_by_xpath(buttonsDict["sin"])
asin = calc.find_element_by_xpath(buttonsDict["asin"])
cos = calc.find_element_by_xpath(buttonsDict["cos"])
acos = calc.find_element_by_xpath(buttonsDict["acos"])
tan = calc.find_element_by_xpath(buttonsDict["tan"])
atan = calc.find_element_by_xpath(buttonsDict["atan"])

log =  calc.find_element_by_xpath(buttonsDict["log"])
ln = calc.find_element_by_xpath(buttonsDict["ln"])
factorial = calc.find_element_by_xpath(buttonsDict["factorial"])

ten_exp = calc.find_element_by_xpath(buttonsDict["10exp"])
expotent = calc.find_element_by_xpath(buttonsDict["expotent"])
xSquared = calc.find_element_by_xpath(buttonsDict["xSquared"])
xCubed = calc.find_element_by_xpath(buttonsDict["xCubed"])
xPowY = calc.find_element_by_xpath(buttonsDict["xPowY"])

squaredRoot = calc.find_element_by_xpath(buttonsDict["squaredRoot"])
cubeRoot = calc.find_element_by_xpath(buttonsDict["cubeRoot"])
yRootX = calc.find_element_by_xpath(buttonsDict["yRootX"])


#bad input modules
def test_bad_input_decimal_mark():
    for i in range(0, int(numberTestsPerModules)):
        print("Treating an initial press of the decimal mark as 0.")
        clear.click()

        rand1 = generatePositiveInt()
        decimal = calc.find_element_by_xpath(buttonsDict['.'])
        decimal.click()
        
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        zero = 0
        expected = str(zero) + "." + str(rand1[0])
        result = output.text

        assert float(result) == float(expected) 

def test_bad_input_multiple_zeros():
    for i in range(0, int(numberTestsPerModules)):
        print("Multiple zeros as input equalling zero")
        clear.click()

        zeroInput = calc.find_element_by_xpath(buttonsDict['0'])
        zeroInput.click()
        zeroInput.click()
        zeroInput.click()
        zeroInput.click()
        zeroInput.click()
    
        result = output.text
        zero = 0
        assert int(result) == zero

def test_bad_input_with_multiple_zeros_with_decimal_mark():
    for i in range(0, int(numberTestsPerModules)):
        print("Multiple zeros as input before decimal mark")
        clear.click()

        zeroInput = calc.find_element_by_xpath(buttonsDict['0'])
        for i in range(0, 10):
            zeroInput.click()
        
        decimal = calc.find_element_by_xpath(buttonsDict['.'])
        decimal.click()

        rand1 = generatePositiveInt()
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        assert result == result

def test_bad_input_zero_before_integer(): 
    for i in range(0, int(numberTestsPerModules)):
        print("Testing input for Input zero before integer")
        clear.click()

        zeroInput = calc.find_element_by_xpath(buttonsDict['0'])
        zeroInput.click()

        rand1 = generatePositiveInt()
        
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        assert int(result) == rand1[0]

def test_bad_input_zero_before_another_operand(): 
    for i in range(0, int(numberTestsPerModules)):
        print("Testing input for inputting a zero before another digit of input for a second operand")
        clear.click()

        rand1 = generatePositiveInt()
        rand2 = generatePositiveInt()
        zeroInput = calc.find_element_by_xpath(buttonsDict['0'])
        zeroInput.click()
        
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        result = output.text
        assert int(result) == rand1[0]
        multiply.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        
def test_bad_input_floating_point_input_with_multiple_digits_before_and_after_decimal_mark(): 
    for i in range(0, int(numberTestsPerModules)):
        print("Testing input for multiple digit floating point")
        clear.click()
        rand1 = generatePositiveInt()
        rand2 = generatePositiveInt()

        decimal = calc.find_element_by_xpath(buttonsDict['.'])

        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        decimal.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        
        expected = str(rand1[0]) + "." + str(rand2[0])
        result = output.text

        assert float(result) == float(expected)

def test_bad_input_floating_point_input_with_multiple_digits_before_and_after_decimal_mark(): 
    for i in range(0, int(numberTestsPerModules)):
        print("Testing input for multiple digit floating point")
        clear.click()
        rand1 = generatePositiveInt()
        rand2 = generatePositiveInt()

        decimal = calc.find_element_by_xpath(buttonsDict['.'])

        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        decimal.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        
        expected = str(rand1[0]) + "." + str(rand2[0])
        result = output.text

        assert float(result) == float(expected)   
        
def test_bad_input_first_decimal_operand_to_display_leading_zero(): 
    for i in range(0, int(numberTestsPerModules)):
        print("Testing input for allowing a first decimal operand to display a leading zero")
        clear.click()
        rand1 = generatePositiveInt()

        decimal = calc.find_element_by_xpath(buttonsDict['.'])
        decimal.click()
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        
        zero = 0
        expected = str(zero) + "." + str(rand1[0])
        result = output.text

        assert float(result) == float(expected)

def test_bad_input_second_decimal_operand_to_display_leading_zero(): 
    for i in range(0, int(numberTestsPerModules)):
        print("Testing input for allowing a second decimal operand to display a leading zero")
        clear.click()
        rand1 = generatePositiveInt()
        rand2 = generatePositiveInt()
        decimal = calc.find_element_by_xpath(buttonsDict['.'])

        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()
        decimal.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
    
        zero = 0
        expected = str(zero) + "." + str(rand2[0])
        result = "." + str(rand2[0])
        
        assert float(result) == float(expected)

def test_bad_input_float_point_input_with_single_digit_before_and_after_decimal_mark(): 
    for i in range(0, int(numberTestsPerModules)):
        print("Testing input for allowing a floating point input with a single digit before and after the decimal mark")
        clear.click()
        rand1 = generatePositiveInt()
        rand2 = generatePositiveInt()
        decimal = calc.find_element_by_xpath(buttonsDict['.'])

        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        decimal.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        expected = str(rand1[0]) + "." + str(rand2[0])
        result = output.text
        assert float(result) == float(expected)

def test_bad_input_count_decimal_mark_against_max_input(): 
    for i in range(0, int(numberTestsPerModules)):
        print("Testing input for not counting a decimal mark against max input")
        clear.click()
        rand1 = generatePositiveInt()
        rand2 = generateLargeInt()

        decimal = calc.find_element_by_xpath(buttonsDict['.'])

        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        decimal.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        
        expected = str(rand1[0]) + "." + str(rand2[0])
        result = output.text
        assert float(result) == float(expected)

def test_bad_input_double_negation(): 
    for i in range(0, int(numberTestsPerModules)):
        print("Testing input to not allow double negation")
        clear.click()
        rand1 = generatePositiveInt()

        substract.click()
        substract.click()
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
    
        expected = "-" + str(rand1[0])
        result = output.text
        assert int(result) == int(expected)

def test_bad_input_double_negation(): 
    for i in range(0, int(numberTestsPerModules)):
        print("Testing input to allow the maximum input when the first digit is zero")
        clear.click()

        rand1 = generateLargeInt()

        zero_input = calc.find_element_by_xpath(buttonsDict['0'])
        zero_input.click()
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        
        expected = (rand1[0])
        result = output.text
        assert int(result) == int(expected)

#clear input
def test_clear_screen_after_negative_floating_number():
    for i in range(0, int(numberTestsPerModules)):
        print("Clearing the screen after inserting a negative floating point number")
        clear.click()
        rand1 = generateNegativeFloat()
        expected = 0
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        clear.click()

        result = output.text

        assert int(result) == expected

def test_clear_screen_after_positive_floating_number():
    for i in range(0, int(numberTestsPerModules)):
        print("Clearing the screen after inserting a positive floating point number")
        clear.click()
        rand1 = generatePositiveFloat()
        expected = 0
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        clear.click()

        result = output.text

        assert int(result) == expected

def test_clear_screen_after_negative_integer():
    for i in range(0, int(numberTestsPerModules)):
        print("Clearing the screen after inserting a negative integer")
        clear.click()
        rand1 = generateNegativeInt()
        expected = 0
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        clear.click()

        result = output.text

        assert int(result) == expected

def test_clear_screen_after_positive_integer():
    for i in range(0, int(numberTestsPerModules)):
        print("Clearing the screen after inserting a positive integer")
        clear.click()
        rand1 = generatePositiveInt()
        expected = 0
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        clear.click()

        result = output.text

        assert int(result) == expected

def test_clear_multiple_times():
    for i in range(0, int(numberTestsPerModules)):
        print("Output is cleared even when pressed multiple times")
        clear.click()
        rand1 = generatePositiveInt()
        expected = 0
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        clear.click()
        clear.click()
        clear.click()
        clear.click()
        clear.click()

        result = output.text

        assert int(result) == expected

def test_clear_many_digit_float_number():
    for i in range(0, int(numberTestsPerModules)):
        print("Clear output after inserting a many digit floating point number")
        clear.click()
        rand1 = generatePositiveInt()
        rand2 = generateVeryLargeInt()
        expected = 0
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        decimal = calc.find_element_by_xpath(buttonsDict['.'])
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        clear.click()

        result = output.text

        assert int(result) == expected

def test_clear_negative_many_digit_float_number():
    for i in range(0, int(numberTestsPerModules)):
        print("Clear output after inserting a negative many digit floating point number")
        clear.click()
        rand1 = generateNegativeInt()
        rand2 = generatePositiveInt()
        expected = 0
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        decimal = calc.find_element_by_xpath(buttonsDict['.'])
        decimal.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        clear.click()

        result = output.text

        assert int(result) == expected

def test_clear_negative_large_integer(): #FIX
    for i in range(0, int(numberTestsPerModules)):
        print("Clear output after inserting a negative large integer")
        clear.click()
        rand1 = generateNegativeLargeInt()
        expected = 0
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        clear.click()

        result = output.text

        assert int(result) == expected

def test_clear_positive_large_integer():
    for i in range(0, int(numberTestsPerModules)):
        print("Clear output after inserting a positive large integer")
        clear.click()
        rand1 = generateLargeInt()
        expected = 0
        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        clear.click()

        result = output.text

        assert int(result) == expected

#addition modules

def test_addition_positive_integers():
    for i in range (0, int(numberTestsPerModules)):
        print("test_addition_positive_integers")
        #CLEAR PREVIOUS INPUTS
        clear.click()

        #generating random numbers
        rand1 = generatePositiveInt()
        rand2 = generatePositiveInt()
        expected = add_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        add.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    

        result = output.text

        assert int(result) == expected 

def test_addition_negative_integers():
    for i in range (0, int(numberTestsPerModules)):
        print("test_addition_negative_integers")
        #CLEAR PREVIOUS INPUTS
        clear.click()
 
        #generating random numbers
        rand1 = generateNegativeInt()
        rand2 = generateNegativeInt()
        expected = add_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        add.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    

        result = output.text

        assert int(result) == expected 

def test_addition_positive_integers_and_negative_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_addition_positive_integers_and_negative_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()

        #generating random numbers
        rand1 = generatePositiveInt()
        rand2 = generateNegativeInt()
        expected = add_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        add.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    

        result = output.text

        assert int(result) == expected

def test_addition_negative_integers_and_positive_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_addition_negative_integers_and_positive_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()

        #generating random numbers
        rand1 = generatePositiveInt()
        rand2 = generateNegativeInt()
        expected = add_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        add.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    

        result = output.text

        assert int(result) == expected 

def test_addition_positive_integer_to_prev_result():
    for i in range(0, int(numberTestsPerModules)):
        print("test_addition_positive_integer_to_prev_result")

        # dont clear previous result
        prev_result = output.text

        rand1 = generatePositiveInt()
        expected = add_function(int(prev_result), rand1[0])

        add.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text

        assert int(result) == expected

def test_addition_negative_integer_to_prev_result():
    for i in range(0, int(numberTestsPerModules)):
        print("test_addition_negative_integer_to_prev_result")

        # dont clear previous result
        prev_result = output.text

        rand1 = generateNegativeInt()
        expected = add_function(int(prev_result), rand1[0])

        add.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text

        assert int(result) == expected  

def test_addition_with_positive_decimal_integers():
    for i in range (0, int(numberTestsPerModules)):
        print("test_addition_positive_decimal_integers")
        clear.click()
        rand1 = generatePositiveFloat()
        rand2 = generatePositiveFloat()
        expected = add_function(rand1[0], rand2[0])
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        add.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)

def test_addition_with_negative_decimal_integers():
    for i in range (0, int(numberTestsPerModules)):
        print("test_addition_negative_decimal_integers")
        clear.click()
        rand1 = generateNegativeFloat()
        rand2 = generateNegativeFloat()
        expected = add_function(rand1[0], rand2[0])
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        add.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()   

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)

def test_addition_with_positive_and_negative_decimal_integers():
    for i in range (0, int(numberTestsPerModules)):
        print("test_addition_with_positive_and_negative_decimal_integers")
        clear.click()
        rand1 = generatePositiveFloat()
        rand2 = generateNegativeFloat()
        expected = add_function(rand1[0], rand2[0])
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        add.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()   

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)

def test_addition_with_negative_and_positive_decimal_integers():
    for i in range (0, int(numberTestsPerModules)):
        print("test_addition_with_negative_and_positive_decimal_integers")
        clear.click()
        rand1 = generateNegativeFloat()
        rand2 = generatePositiveFloat()
        expected = add_function(rand1[0], rand2[0])
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        add.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()   

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace) 

def test_addition_positive_decimal_integer_to_prev_result():
    for i in range(0, int(numberTestsPerModules)):
        print("test_addition_positive_decimal_integer_to_prev_result")

        # dont clear previous result
        prev_result = output.text

        rand1 = generatePositiveFloat()
        expected = add_function(float(prev_result), rand1[0])

        add.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert pytest.approx (float(result)) == round(expected, decimalPlace)

def test_addition_negative_decimal_integer_to_prev_result():
    for i in range(0, int(numberTestsPerModules)):
        print("test_addition_negative_decimal_integer_to_prev_result")

        # dont clear previous result
        prev_result = output.text

        rand1 = generateNegativeFloat()
        expected = add_function(float(prev_result), rand1[0])

        add.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert pytest.approx (float(result)) == round(expected, decimalPlace)

def test_addition_with_brackets_using_integer_and_float():
    for i in range(0, int(numberTestsPerModules)):
        print("test_addition_with_brackets_using_integer_and_float")

        clear.click()
     
        rand1 = generatePositiveInt()
        rand2 = generatePositiveFloat()
        left = add_function(rand1[0], rand2[0])
        
        rand3 = generateNegativeFloat()
        rand4 = generatePositiveInt()
        right = add_function(rand3[0], rand4[0])

        expected = add_function(left, right)

        leftBracket.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        add.click()    
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        rightBracket.click()

        add.click()

        leftBracket.click()
        for i in rand3[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        add.click()    
        for i in rand4[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        rightBracket.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert pytest.approx (float(result)) == round(expected, decimalPlace)

#substraction modules
def test_substraction_with_positive_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_substraction_with_positive_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generatePositiveInt()
        rand2 = generatePositiveInt()
        expected = substract_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        substract.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    

        result = output.text

        assert int(result) == expected

def test_substraction_with_negative_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_substraction_with_negative_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generateNegativeInt()
        rand2 = generateNegativeInt()
        expected = substract_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        substract.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    

        result = output.text

        assert int(result) == expected

def test_substraction_with_positive_and_negative_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_substraction_with_positive_and_negative_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generatePositiveInt()
        rand2 = generateNegativeInt()
        expected = substract_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        substract.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    

        result = output.text

        assert int(result) == expected

def test_substraction_with_negative_and_positive_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_substraction_with_negative_and_positive_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generateNegativeInt()
        rand2 = generatePositiveInt()
        expected = substract_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        substract.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    

        result = output.text

        assert int(result) == expected

def test_substraction_positive_integer_to_prev_result():
    for i in range(0, int(numberTestsPerModules)):
        print("test_substract_positive_integer_to_prev_result")

        # dont clear previous result
        prev_result = output.text

        rand1 = generatePositiveInt()
        expected = substract_function(int(prev_result), rand1[0])

        substract.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text

        assert int(result) == expected

def test_substraction_negative_integer_to_prev_result():
    for i in range(0, int(numberTestsPerModules)):
        print("test_substract_negative_integer_to_prev_result")

        # dont clear previous result
        prev_result = output.text

        rand1 = generateNegativeInt()
        expected = substract_function(int(prev_result), rand1[0])

        substract.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text

        assert int(result) == expected        

def test_substraction_with_positive_decimal_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_substraction_with_positive_decimal_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generatePositiveFloat()
        rand2 = generatePositiveFloat()
        expected = substract_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        substract.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)

def test_substraction_with_negative_decimal_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_substraction_with_negative_decimal_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generateNegativeFloat()
        rand2 = generateNegativeFloat()
        expected = substract_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        substract.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
                
        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)

def test_substraction_with_positive_and_negative_decimal_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_substraction_with_positive_and_negative_decimal_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generatePositiveFloat()
        rand2 = generateNegativeFloat()
        expected = substract_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        substract.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
                
        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)

def test_substraction_with_negative_and_positive_decimal_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_substraction_with_negative_and_positive_decimal_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generateNegativeFloat()
        rand2 = generatePositiveFloat()
        expected = substract_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        substract.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
                
        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)

def test_substraction_positive_decimal_integer_to_prev_result():
    for i in range(0, int(numberTestsPerModules)):
        print("test_substract_negative_integer_to_prev_result")

        # dont clear previous result
        prev_result = output.text

        rand1 = generatePositiveFloat()
        expected = substract_function(float(prev_result), rand1[0])

        substract.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert pytest.approx (float(result)) == round(expected, decimalPlace)

def test_substraction_negative_decimal_integer_to_prev_result():
    for i in range(0, int(numberTestsPerModules)):
        print("test_substract_negative_integer_to_prev_result")

        # dont clear previous result
        prev_result = output.text

        rand1 = generateNegativeFloat()
        expected = substract_function(float(prev_result), rand1[0])

        substract.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert pytest.approx (float(result)) == round(expected, decimalPlace)

def test_substraction_with_brackets_using_integer_and_float():
    for i in range(0, int(numberTestsPerModules)):
        print("test_substraction_with_brackets_using_integer_and_float")

        clear.click()
     
        rand1 = generatePositiveInt()
        rand2 = generatePositiveFloat()
        left = substract_function(rand1[0], rand2[0])
        
        rand3 = generateNegativeFloat()
        rand4 = generatePositiveInt()
        right = substract_function(rand3[0], rand4[0])

        expected = substract_function(left, right)

        leftBracket.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        substract.click()    
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        rightBracket.click()

        substract.click()

        leftBracket.click()
        for i in rand3[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        substract.click()    
        for i in rand4[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        rightBracket.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert pytest.approx (float(result)) == round(expected, decimalPlace)

#multipication modules
def test_multiplication_with_two_positive_integers():
    for i in range(0, int(numberTestsPerModules)):
        print("Multiplying two positive integers")
        clear.click()
        rand1 = generatePositiveInt()
        rand2 = generatePositiveInt()
        expected = multipication_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text

        assert int(result) == expected

def test_multiplication_with_float_and_integer():
    for i in range(0, int(numberTestsPerModules)):
        print("Multiplying a floating point multiplicand with an integer multiplier")
        clear.click()
        rand1 = generatePositiveFloat()
        rand2 = generatePositiveInt()
        expected = multipication_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert (float(result)) == round(expected, decimalPlace)

def test_multiplication_with_integer_and_float():
    for i in range(0, int(numberTestsPerModules)):
        print("Multiplying a integer multiplier with an floating point ")
        clear.click()
        rand1 = generatePositiveInt()
        rand2 = generatePositiveFloat()
        expected = multipication_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert (float(result)) == round(expected, decimalPlace)

def test_multiplication_with_float_and_float():
    for i in range(0, int(numberTestsPerModules)):
        print("Multiplying two floating point numbers")
        clear.click()
        rand1 = generatePositiveFloat()
        rand2 = generatePositiveFloat()
        expected = multipication_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)

def test_multiplication_with_integer_and_zero():
    for i in range(0, int(numberTestsPerModules)):
        print("Multiplying an integer with a zero")
        clear.click()
        rand1 = generatePositiveInt()
        rand2 = 0
        expected = multipication_function(rand1[0], rand2)

        for i in rand1[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()
        sInput = calc.find_element_by_xpath(buttonsDict['0'])
        sInput.click()

        result = output.text

        assert int(result) == expected

def test_multiplication_with_negative_and_positive_integer():
    for i in range(0, int(numberTestsPerModules)):
        print("Multiplying a negative integer with a postive integer")
        clear.click()
        rand1 = generateNegativeInt()
        rand2 = generatePositiveInt()
        expected = multipication_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text

        assert int(result) == expected

def test_multiplication_with_negative_float_and_positive_integer():
    for i in range(0, int(numberTestsPerModules)):
        print("Multiplying a negative floating point multiplicand with a positive integer multiplier")
        clear.click()
        rand1 = generateNegativeFloat()
        rand2 = generatePositiveInt()
        expected = multipication_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::1].find('.')
        assert pytest.approx(float(result)) == round(expected, decimalPlace)

def test_multiplication_with_negative_integer_and_positive_float():
    for i in range(0, int(numberTestsPerModules)):
        print("Multiplying a negative integer multiplicand with a positive floating point multiplier")
        clear.click()
        rand1 = generateNegativeInt()
        rand2 = generatePositiveFloat()
        expected = multipication_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()
        for i in rand2[1]:
            sInput = calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        assert pytest.approx (round(float(result))) == round(expected)

def test_multipication_Large_int_prev_result():
    for i in range (0, int(numberTestsPerModules)):
        print("test_multipication_Large_int_prev_result")

        prev_result = output.text
        rand1 = generateLargeInt()

        if prev_result.find(".") != -1:
            #if the previous number is in form " 1.4xxxxx 1025" -> "1.4xxxe25"
            newPrev_result = handleLargeNumbersInput(prev_result.lstrip())
            expected = multipication_function(newPrev_result, rand1[0])
        else:
            newPrev_result = handleLargeNumbers(int(prev_result))
            expected = handleLargeNumbers(multipication_function(int(newPrev_result), rand1[0]))

        equals.click()
        multiply.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        result = output.text

        if result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert pytest.approx (newResult) == expected
        else: 
            newResult = handleLargeNumbers(int(result))   
            assert pytest.approx (newResult) == expected

def test_multipication_with_brackets_using_integer_and_float():
    for i in range(0, int(numberTestsPerModules)):
        print("test_multipication_with_brackets_using_integer_and_float")

        clear.click()
     
        rand1 = generatePositiveInt()
        rand2 = generatePositiveFloat()
        left = multipication_function(rand1[0], rand2[0])
        
        rand3 = generateNegativeFloat()
        rand4 = generatePositiveInt()
        right = multipication_function(rand3[0], rand4[0])

        expected = multipication_function(left, right)

        leftBracket.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()    
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        rightBracket.click()

        leftBracket.click()
        for i in rand3[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        multiply.click()    
        for i in rand4[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        rightBracket.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert pytest.approx (float(result)) == round(expected, decimalPlace)

#division module
def test_division_with_positive_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_division_with_positive_integerr")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generatePositiveInt()
        rand2 = generatePositiveInt()
        expected = division_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        division.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    
        equals.click()
        result = output.text
        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            float(result) == float(expected)

def test_division_with_negative_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_division_with_negative_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generateNegativeInt()
        rand2 = generateNegativeInt()
        expected = division_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        division.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    
        equals.click()
        result = output.text
        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            float(result) == float(expected)   

def test_division_with_positive_and_negative_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_division_with_positive_and_negative_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generatePositiveInt()
        rand2 = generateNegativeInt()
        expected = division_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        division.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    
        equals.click()
        result = output.text
        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            float(result) == float(expected)

def test_division_with_negative_and_positive_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_division_with_negative_and_positive_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generateNegativeInt()
        rand2 = generatePositiveInt()

        expected = division_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        division.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    
        equals.click()
        result = output.text
        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            float(result) == float(expected)

def test_division_with_positive_and_negative_decimal_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_division_with_positive_and_negative_decimal_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generatePositiveFloat()
        rand2 = generateNegativeFloat()
        expected = division_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        division.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    
        equals.click()

        result = output.text
        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert pytest.approx(float(result)) == round(expected, decimalPlace)

def test_division_with_negative_and_positive_decimal_integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_division_with_negative_and_positive_decimal_integer")
        #CLEAR PREVIOUS INPUTS
        clear.click()
        #generating random numbers
        rand1 = generateNegativeFloat()
        rand2 = generatePositiveFloat()
        expected = division_function(rand1[0], rand2[0])

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        division.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()    
        equals.click()

        result = output.text
        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert pytest.approx(float(result)) == round(expected, decimalPlace)

def test_division_with_brackets_using_integer_and_float():
    for i in range(0, int(numberTestsPerModules)):
        print("test_division_with_brackets_using_integer_and_float")

        clear.click()
     
        rand1 = generatePositiveInt()
        rand2 = generatePositiveFloat()
        left = division_function(rand1[0], rand2[0])
        
        rand3 = generateNegativeFloat()
        rand4 = generatePositiveInt()
        right = division_function(rand3[0], rand4[0])

        expected = division_function(left, right)

        leftBracket.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        division.click()    
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        rightBracket.click()

        division.click()

        leftBracket.click()
        for i in rand3[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        division.click()
        for i in rand4[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        rightBracket.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert pytest.approx (float(result)) == round(expected, decimalPlace)     

#sin modules
def test_sin_within_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_sin_within_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generateSmallFloat()
        expected = sin_function_degree(rand1[0])

        degree.click()
        sin.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)

def test_sin_outside_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_sin_outside_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = sin_function_degree(rand1[0])

        degree.click()
        sin.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace) 

def test_sin_within_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_sin_within_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generateSmallFloat()
        expected = sin_function_radians(rand1[0])

        radian.click()
        sin.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)                  

def test_sin_outside_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_sin_outside_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = sin_function_radians(rand1[0])

        radian.click()
        sin.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()

        result = output.text
        decimalPlace = result[::-1].find('.')
        assert float(result) == round(expected, decimalPlace)

#inverse sin modules
def test_asin_within_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_asin_within_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generateSmallFloat()
        expected = asin_function_degree(rand1[0])

        degree.click()
        asin.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_asin_outside_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_asin_outside_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = asin_function_degree(rand1[0])

        degree.click()
        asin.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_asin_within_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_asin_within_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generateSmallFloat()
        expected = asin_function_radians(rand1[0])

        radian.click()
        asin.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_asin_outside_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_asin_outside_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = asin_function_degree(rand1[0])

        radian.click()
        asin.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

#cosine modules
def test_cos_outside_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_cos_outside_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = cosin_function_degree(rand1[0])

        degree.click()
        cos.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_cos_within_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_cos_within_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generateSmallFloat()
        expected = cosin_function_degree(rand1[0])

        degree.click()
        cos.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_cos_outside_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_cos_outside_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = cosin_function_radians(rand1[0])

        radian.click()
        cos.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_cos_within_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_cos_within_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generateSmallFloat()
        expected = cosin_function_radians(rand1[0])

        radian.click()
        cos.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

#inverse cosine modules
def test_acos_within_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_acos_within_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generateSmallFloat()
        expected = acosin_function_degree(rand1[0])

        degree.click()
        acos.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_acos_outside_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_acos_outside_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = acosin_function_degree(rand1[0])

        degree.click()
        acos.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_acos_within_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_acos_within_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generateSmallFloat()
        expected = acosin_function_radians(rand1[0])

        radian.click()
        acos.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_acos_outside_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_acos_outside_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = acosin_function_radians(rand1[0])

        radian.click()
        acos.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

#tan modules
def test_tan_within_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_tan_within_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generateSmallFloat()
        expected = tan_function_degree(rand1[0])

        degree.click()
        tan.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_tan_outside_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_tan_outside_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = tan_function_degree(rand1[0])

        degree.click()
        tan.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_tan_within_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_tan_within_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generateSmallFloat()
        expected = tan_function_radian(rand1[0])

        radian.click()
        tan.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_tan_outside_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_tan_outside_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = tan_function_radian(rand1[0])

        radian.click()
        tan.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

#inverse tan modules
def test_atan_within_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_atan_within_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generateSmallFloat()
        expected = atan_function_degree(rand1[0])

        degree.click()
        atan.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_atan_outside_range_positive_one_to_negative_one_as_degree():
    for i in range (0, int(numberTestsPerModules)):
        print("test_atan_outside_range_positive_one_to_negative_one_as_degree")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = atan_function_degree(rand1[0])

        degree.click()
        atan.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_atan_within_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_atan_within_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generateSmallFloat()
        expected = atan_function_radian(rand1[0])

        radian.click()
        atan.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_atan_outside_range_positive_one_to_negative_one_as_radian():
    for i in range (0, int(numberTestsPerModules)):
        print("test_atan_outside_range_positive_one_to_negative_one_as_radian")
        clear.click()

        rand1 = generatePositiveToNegativeFloat()
        expected = atan_function_radian(rand1[0])

        radian.click()
        atan.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

#log modules
def test_logaritm_with_default_base_10_positive_Integer(): 
    for i in range (0, int(numberTestsPerModules)):
        print("test_logaritm_with_default_base_10_positive_Integer")
        clear.click()

        rand1 = generatePositiveInt()
        expected = log_function(rand1[0])

        log.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        #equals.click()

        result = output.text
        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)  

def test_logaritm_with_default_base_10_negative_Integer(): 
    for i in range (0, int(numberTestsPerModules)):
        print("test_logaritm_with_default_base_10_negative_Integer")
        clear.click()

        rand1 = generateNegativeInt()
        expected = log_function(rand1[0])

        log.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()

        result = output.text
        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

#natural log modules
def test_natural_logaritm_with_positive_Integer(): 
    for i in range (0, int(numberTestsPerModules)):
        print("test_natural_logaritm_with_positive_Integer")
        clear.click()

        rand1 = generatePositiveInt()
        expected = ln_function(rand1[0])

        ln.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()

        result = output.text
        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

def test_natural_logaritm_with_Negative_Integer(): 
    for i in range (0, int(numberTestsPerModules)):
        print("test_natural_logaritm_with_Negative_Integer")
        clear.click()

        rand1 = generatePositiveInt()
        expected = ln_function(rand1[0])

        ln.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()

        result = output.text
        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        else:   
            decimalPlace = result[::-1].find('.')
            assert float(result) == round(expected, decimalPlace)

#factorial modules
def test_factorial_with_positive_Integer(): 
    for i in range (0, int(numberTestsPerModules)):
        print("test_factorial_with_positive_Integer")
        clear.click()

        rand1 = generatePositiveInt()
        expected = handleLargeNumbers(factorial_function(rand1[0]))

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        factorial.click()
        equals.click()
        
        result = output.text
        if result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert pytest.approx (newResult) == expected
        else:
            newResult = handleLargeNumbers(int(result))    
            assert pytest.approx(newResult) == expected

def test_factorial_with_negative_Integer(): 
    for i in range (0, int(numberTestsPerModules)):
        print("test_factorial_with_negative_Integer")
        clear.click()

        rand1 = generateNegativeInt()
        expected = handleLargeNumbers(factorial_function(rand1[0]))

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        factorial.click()
        equals.click()
        
        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        elif result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert pytest.approx (newResult) == expected
        else:
            newResult = handleLargeNumbers(int(result))    
            assert pytest.approx(newResult) == expected

#expotential modules
def test_ten_expotential_with_Positive_and_negative_Integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_ten_expotential_with_Positive_and_negative_Integer")
        clear.click()

        rand1 = generatePositiveToNegativeInt()
        defaultBase = 10
        expected = handleLargeNumbers(expotential_function(rand1[0], defaultBase))

        ten_exp.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()

        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        elif result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert pytest.approx (newResult) == expected

        else:
            newResult = handleLargeNumbers(result)    
            assert pytest.approx(newResult) == expected

def test_expotential_with_Positive_and_negative_Integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_expotential_with_Positive_and_negative_Integer")
        clear.click()

        rand1 = generatePositiveToNegativeInt()
        #default base e
        expected = handleLargeNumbersInput(expotential_function(rand1[0]))

        expotent.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()

        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        elif result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert pytest.approx (newResult) == expected

        else:
            newResult = handleLargeNumbers(result)    
            assert pytest.approx(newResult) == expected

def test_x_Squared_with_Positive_and_negative_Integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_x_Squared_with_Positive_and_negative_Integer")
        clear.click()

        rand1 = generatePositiveToNegativeInt()
        #default expotent 2
        expected = handleLargeNumbers(expotential_function(2, rand1[0]))

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()  
        xSquared.click()
        equals.click()

        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        elif result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert pytest.approx (newResult) == expected

        else:
            newResult = handleLargeNumbers(result)    
            assert pytest.approx(newResult) == expected

def test_x_Cubed_with_Positive_and_negative_Integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_x_Cubed_with_Positive_and_negative_Integer")
        clear.click()

        rand1 = generatePositiveToNegativeInt()
        #default expotent 3
        expected = handleLargeNumbers(expotential_function(3, rand1[0]))

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        xCubed.click()
        equals.click()

        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        elif result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert pytest.approx (newResult) == expected

        else:
            newResult = handleLargeNumbers(result)    
            assert pytest.approx(newResult) == expected

def test_x_Pow_y_with_Positive_and_negative_Integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_x_Pow_y_with_Positive_and_negative_Integer")
        clear.click()

        rand1 = generatePositiveToNegativeInt()
        rand2 = generatePositiveToNegativeInt()

        expected = handleLargeNumbers(expotential_function(rand1[0], rand2[0]))

        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        xPowY.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()

        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        elif result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert (newResult) == pytest.approx(expected)

        else:
            newResult = handleLargeNumbersInput(result)
            assert  newResult == pytest.approx(expected)

#root modules
def test_squared_root_with_Positive_Integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_squared_root_with_Positive_and_negative_Integer")
        clear.click()

        rand1 = generatePositiveInt()
        expotent = 1/2
        #deafault expotent 1/2
        expected = handleLargeNumbers(expotential_function(expotent, rand1[0]))

        squaredRoot.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()

        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        elif result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert pytest.approx (newResult) == expected

        else:
            newResult = handleLargeNumbers(result)    
            assert pytest.approx(newResult) == expected

def test_cube_root_with_Positive_and_negative_Integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_cube_root_with_Positive_and_negative_Integer")
        clear.click()

        rand1 = generatePositiveToNegativeInt()
        expotent = 1/3
        expected = handleLargeNumbers(expotential_function(expotent, rand1[0]))

        cubeRoot.click()
        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()

        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        elif result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert pytest.approx (float(newResult)) == float(expected)

        else:
            newResult = handleLargeNumbers(result)    
            assert pytest.approx (float(newResult)) == float(expected)

def test_y_root_x_with_Positive_and_negative_Integer():
    for i in range (0, int(numberTestsPerModules)):
        print("test_y_root_x_with_Positive_and_negative_Integer")
        clear.click()

        rand1 = generatePositiveInt()
        rand2 = generatePositiveToNegativeInt()
        expected = handleLargeNumbers(expotential_function((division_function(1, rand2[0])), rand1[0]))

        for i in rand1[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        yRootX.click()
        for i in rand2[1]:
            sInput =  calc.find_element_by_xpath(buttonsDict[i])
            sInput.click()
        equals.click()

        result = output.text

        if(isinstance(expected, str)):
           assert result.lstrip() == expected
        elif result.find(".") != -1:
            #" 1.4xxxxx x1025" -> "1.4xxxe25"
            newResult = handleLargeNumbersInput(result.lstrip())
            assert pytest.approx (abs(newResult)) == abs(expected)

        else:
            newResult = handleLargeNumbers(result)    
            assert pytest.approx (abs(float(newResult))) == abs(float(expected))


    calc.quit()