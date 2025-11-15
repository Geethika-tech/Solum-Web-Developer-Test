# --- Complexity Analysis ---
# Time Complexity: O(1)
# The core logic inside calculate_min_and_max_fleet involves only constant-time arithmetic operations
# (division, modulo, addition, subtraction, assignment), which execute independently of the size of N.
# The overall solve_final function runs in O(T), where T is the number of test cases,
# because the O(1) function is executed T times.

# Space Complexity: O(T)
# The space is dominated by the 'output' list in solve_final, which stores T results (strings).
# Thus, the space used scales linearly with the number of test cases.
# ---------------------------

import sys

# Function to calculate minimum and maximum possible number of crafts in the fleet.
def calculate_min_and_max_fleet(n: int) -> int | tuple[int, int]:
    """
    Calculates the minimum and maximum possible number of crafts (x, y)
    given the total propulsion units n. Returns -1 on error, or a tuple (x, y) on success.
    """
    # Step 1: Check if n is even or less than 4 (the minimum required units).
    # If n is odd or less than 4, teh combination of Type A and Type B crafts cannot be possible.
    if n % 2 != 0 or n < 4:
        # Also handles n=0, n=2, as they are < 4.
        return -1 # Returns an integer for the error case

    # The equation 4a+6b=n is reduced to: 2a + 3b = N where N=n//2
    N = n // 2 
    
    # Step2: Calculate the minimum number of crafts possible (x) 
    # Strategy: Maximise the use of Type B crafts (3 units/craft).
    b_max_potential = N // 3
    
    # Determine the number of B crafts that leaves an even remainder for A crafts (2 units/craft).
    if (N - 3 * b_max_potential) % 2 != 0:
        b_min_crafts = b_max_potential - 1
    else:
        b_min_crafts = b_max_potential
        
    a_min_crafts = (N - 3 * b_min_crafts) // 2
    x = a_min_crafts + b_min_crafts

    # Step 3: Calculate the maximum number of crafts possible (y)
    # Strategy: Maximise the use of Type A crafts (2 units/craft).
    if N % 2 == 0:
        # If N is even, b=0 is possible (N = 2*a)
        a_max_crafts = N // 2
    else:
        # If N is odd, b must be at least 1 because b=0 will make N even (N = 2*a + 3*1)
        a_max_crafts = (N - 3) // 2

    b_max_crafts = (N - 2 * a_max_crafts) // 3
    y = a_max_crafts + b_max_crafts

    # Returns a tuple of two integers on success
    return x, y 


def solve_final():
    """
    Reads t, then reads t lines of n, processes all, and prints all output 
    together. Includes robust error handling for input, treating empty n as 0.
    """
    
    read_line = sys.stdin.readline
    
    output = []
    
    # --- 1. Read t (number of test cases) ---
    try:
        print("Enter the number of test cases:")
        t_line = read_line().strip()
        # Handle empty input gracefully
        if not t_line:
            return
        t = int(t_line)
    except ValueError:
        # Catch non-integer input for t and exit without crashing
        return
    except EOFError:
        # Handle unexpected end of file
        return

    # --- 2. Loop t times to read and process n ---
    for i in range(t):
        try:
            print(f"Enter the number of propulsion units for test case {i+1}:")
            n_line = read_line().strip()
            
            # --- MODIFICATION: Handle empty input for n by setting n=0 ---
            if not n_line:
                n = 0
                print("Empty input detected for n. Treating n as 0.")
            # Stop if input stream ends early (e.g., Ctrl+D/Z)
            elif n_line == '': 
                break # Should be caught by 'if not n_line' above, but kept for robustness
            else:
                # n can be a very large number (up to 10^18), int() handles this.
                n = int(n_line)
                
        except ValueError:
            # If a line contains non-integer characters, treat it as an error case 
            # and continue to the next iteration.
            result_string = "-1"
            output.append(result_string)
            continue
        except EOFError:
            # If EOF occurs during the read loop
            break
        
        # --- 3. Process and store the result ---
        result = calculate_min_and_max_fleet(n)

        
        # Check the type to format the output correctly
        if isinstance(result, int):
            # Error case (result is -1)
            output.append(str(result)) 
        else:
            # Success case (result is the tuple (x, y))
            x, y = result

            output.append(f"{x} {y}")

    # --- 4. Print all results to standard output ---
    print("\nOutput:")
    # Ensure only results for completed test cases are printed, 
    # in case the loop was broken early by EOF.
    sys.stdout.write('\n'.join(output) + '\n')
    

if __name__ == "__main__":
    solve_final()
