# --- Complexity Analysis ---
# Time Complexity: O(T)
# The core function, total_energy(x, n), performs only constant-time arithmetic and comparison
# operations, so its complexity is O(1).
# The solve_updated function iterates exactly T times (T = number of test cases) and calls 
# the O(1) function inside the loop. The input reading and parsing within the loop is also 
# dominated by constant-time operations for splitting a line of two numbers.
# Therefore, the overall time complexity is O(T).

# Space Complexity: O(T)
# The space is dominated by the 'results' list, which stores the integer result of the 
# calculation for each of the T test cases.
# Thus, the space used scales linearly with the number of test cases.
# ---------------------------
# Functin to calculate the total enery 
def total_energy(x,n):
    # Calculate the total energy after n waves
    # If n is 0, total energy is x
    if(n==0):
        return x
    # If n is even total energy is 0
    elif n>0 and n%2==0:
        return 0
    # If n is odd total energy is x
    elif n>0 and n%2!=0:
        return x
    # If n is negative total energy is 0
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


# You would call solve_updated() to run the script.
solve_updated()




