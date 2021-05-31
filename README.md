<!-- ![cmd-vs-powershell](https://github.com/Chauster/CSIT314-Project/blob/main/cmd-vs-powershell.png) -->

![powershell](https://github.com/Chauster/CSIT314-Project/blob/main/transparent-powershell.PNG)

# Official Code Repository for Automated Scientific Calculator Testing
(CSIT314 Part 2)

### Features

- running autonomous testing for scientific calculator functions
  - addition
  - subtraction
  - multiplication
  - division
  - scientific functions
    - sin
      - sinh (asin)
    - cos
      - cosh (acos)
    - tan
      - tanh (atan)
    - exponents
    - radial and degree
  - invalid inputs

- testing concepts
  - prompt user to enter the number of iterations to run
  - checking invalid inputs
  - floats and integers
    - using large integers
    - using large floats
  - negative and positive inputs
    - negation of operands (plus and minus)
  - checking null inputs
  - zero as input
  - calculation using previous results

---

### Source Code Access

- to view source code (open these files):
  - `calculator.py` - defines general calculator functions (checks the expected results)
  - `dict.py` - accesses the calculator buttons from the calculator app (from calculator.net)
  - `test_calculator.py` - defines all the tests to be carried out - work in progress
  - `randomGeneration.py` - random value generation based on specific tests
  - ~~`driver_file_test.py` - carries out autonomous testing (based on user input) - work in progress~~
  - `test_calculator_report.py` - log file to record all test outcomes (PASS and FAIL)

---

### Execution Instructions

##### Windows

- download and install python to your local machine
  - https://www.python.org/downloads/
  - check version
    - `python --version`
- download python-pip
- download python-pytest
  - `pip install -U pytest`
- download python-pytest-html
  - `pip install pytest-html`
- install selenium (chrome webdriver)
  - `pip install -U selenium`
- execution
  - run `py.test.exe --capture=tee-sys --verbose --html=test_calculator_report.html test_calculator.py`

##### Linux (python3)

- `sudo apt-get update`
- `sudo apt-get install python3.8`
- `python3 --version`
- more steps to be added
