# Question A:Mystic waves
# Input Parameters: t = Number of test cases(1<=t<=100),
# x = Energy value(x>=1),
# n = Number of waves(n<=10)
# Output: Total energy after n waves which is calculated as sum of sequence of energy values(x,-x,x...) of all waves(n).
#Example
# Input:
# 2
# 1 2
# 2 3
# Output:
# 0 (1+(-1))
# 2 (2+(-2)+2)

#Solution
# Functin to calculate the total enery
def total_energy(x,n):
    if(n==0):
        return x
    elif n>0 and n%2==0:
        return 0
    elif n>0 and n%2!=0:
        return x
    else:
        return 0


def solve_updated():
    try:
        # Read the number of test cases (t)
        t_line = input()
        t = int(t_line)
    except (EOFError, ValueError):
        return

    results = []
    
    # Process exactly 't' number of test cases
    for i in range(t):
        try:
            # Read the line, preserving leading spaces with split(' ')
            line = input().split(' ')
            
            # --- CRITICAL FIX START ---
            
            # 1. Check if X is missing (signified by an empty string at the start)
            if not line or line[0] == '':
                # If the line is empty OR the first element is an empty string, 
                # this means X is missing. We MUST skip the test case calculation.
                
                # Consume remaining items on the line just to keep the input stream clean
                # before moving to the next iteration. (e.g. skip the '3' which was meant to be n)
                print("Since x is missing, skipping this tes case")
                continue
                
            # --- CRITICAL FIX END ---
                
            # 2. Parsing X: If we reach here, line[0] must contain the value for X.
            x = int(line[0]) 
            
            # 3. Parsing N: Find the next non-empty string in the list for n
            n_str = None
            for item in line[1:]:
                if item: # Find the first non-empty string after x
                    n_str = item
                    break
            
            # 4. Convert N
            if n_str:
                n = int(n_str)
            else:
                # Default n to 0 if no second number is found
                print("Since n is missing, defaulting to 0")
                n = 0
    
        except (EOFError):
            # Catches running out of lines
            break
        except ValueError:
            # Catches if x (line[0]) or n (n_str) was not a valid integer.
            # Skip this line as it's invalid, but count the loop iteration
            continue
            
        # Calculate and store the result
        result = total_energy(x, n)
        results.append(result)
        
    # Print all results
    for result in results:
        print(result)
# Example to demonstrate logic:
# if x=25, n=0 -> result = 25
# if x=25, n=4 -> result = 0
# if x=25, n=5 -> result = 25

# You would call solve_updated() to run the script.
solve_updated()




