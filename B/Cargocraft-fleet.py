import sys

# Function to calculate minimum and maximum possible number of crafts in the fleet.
def calculate_min_and_max_fleet(n: int) -> int | tuple[int, int]:
    """
    Calculates the minimum and maximum possible number of crafts (x, y)
    given the total propulsion units n. Returns -1 on error, or a tuple (x, y) on success.
    """
    # Step 1: Check if n is even or less than 4 (the minimum required units).
    if n % 2 != 0 or n < 4:
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
        # N is odd, b must be at least 1 because b=0 will make N even (N = 2*a + 3*1)
        a_max_crafts = (N - 3) // 2

    b_max_crafts = (N - 2 * a_max_crafts) // 3
    y = a_max_crafts + b_max_crafts

    # Returns a tuple of two integers on success
    return x, y 


def solve_final():
    """
    Reads t, then reads t lines of n, processes all, and prints all output 
    together. Includes robust error handling for input.
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
    for _ in range(t):
        try:
            print("Enter the number of propulsion units:")
            n_line = read_line().strip()
            # Stop if input stream ends early or line is empty
            if not n_line:
                break
                
            # n can be a very large number (up to 10^18), int() handles this.
            n = int(n_line)
            
        except ValueError:
            # If a line contains non-integer characters, treat it as an error case 
            # and continue to the next iteration.
            result_string = -1
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
    print("Output:")
    sys.stdout.write('\n'.join(output) + '\n')
    

if __name__ == "__main__":
    solve_final()