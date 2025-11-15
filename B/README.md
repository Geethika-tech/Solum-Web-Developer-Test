# The goal of this problem is to find the minimum and maximum possible number of crafts (x, y) given the total propulsion units n.
1. Input: The input is a list of t test cases, each test case is a number n.
2. Output: The output is a list of t lines, each line is the minimum and maximum possible number of crafts (x, y) given the total propulsion units n.
3. Constraints: 1 <= t <= 1000, 1<= n <= 10^18
4. For this problem I choose Python as programming language.

# Setup instructions
1. Install Python.
2. Clone the code from github using the command: 
   **git clone https://github.com/Geethika-tech/Solum-Web-Developer-Test.git**
   or download the zip file from github repo and extract files. Then open it in any code editor.
4. Navigate to the project directory using the command: 
   **cd B** (After navigating to Solumn-Web-Developer-Test folder)
# Run the code
1. Run the code using command:
   **python Cargocraft-fleet.py**
2. The code will ask for following inputs:
   - t (number of test cases)
   - n (number of propulsion units)
3. The code will output the minimum and maximum possible number of crafts (x, y) given the total propulsion units n. 

# Problem solving logic
1. The problem is to find the minimum and maximum possible number of crafts (x, y) given the total propulsion units n.
2. The equation 4a+6b=n is reduced to: 2a + 3b = N where N=n//2
3. The minimum number of crafts possible (x) is calculated by maximising the use of Type B crafts (3 units/craft).
4. The maximum number of crafts possible (y) is calculated by maximising the use of Type A crafts (2 units/craft).
5. The code will output the minimum and maximum possible number of crafts (x, y) given the total propulsion units n.

# Note
1. If the value of n is empty or no value is entered, the value is considered 0.
2. 



