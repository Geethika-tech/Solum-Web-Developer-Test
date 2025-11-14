
# Goal: The goal of this problem is to find the total energy after n waves which is calculated as sum of sequence of energy values(x,-x,x...) of all waves(n).
# Input: The input is a list of t test cases, each test case is the value of x and n.
# Output: The output is a list of t lines, each line is the total energy after n waves.
# Constraints: 1 <= t <= 100, x>=1, n<=10

# Setup instrcutions
1) Install Python on your system if you haven't already
2) Clone the code from github (if you haven't already) using the command: 
   git clone https://github.com/Geethika-tech/Solum-Web-Developer-Test.git
3) Navigate to the project directory using the command: 
   cd A
# Run the code
1) Run the code using command:
   python mystic-waves.py
2) The code will ask for following inputs:
   - t (number of test cases)
   - x (energy value)
   - n (number of waves)
 
3) The code will output the total energy after n waves for each test case.  

# Problem solving logic
 1) The total energy after n waves is calculated as sum of sequence of energy values(x,-x,x...) of all waves(n).
 2) The calculation is done as follows:
    - If n is 0, the total energy is x.
    - If n is even, the total energy is 0. As each wave has a positive and a negative energy value, they cancel each other out.
    - If n is odd, the total energy is x. As the last wave has a positive energy value, it is not cancelled out.
 3) The code will output the total energy after n waves for each test case.
  

