import sys

def calculate_min_and_max_fleet(n: int) -> str:
    """
    Calculates the minimum and maximum possible number of crafts (a+b)
    given the total propulsion units n. Returns the formatted output string
    "x y" or "-1".
    
    This calculation is O(1) (constant time).
    """
    
    # --- 1. IMPOSSIBILITY CHECK ---
    # n must be even, and n must be at least 4.
    if n % 2 != 0 or n < 4:
        return "-1"

    N = n // 2  # Reduced equation: 2a + 3b = N

    # --- 2. CALCULATE C_min (Minimum Crafts) ---
    # Strategy: Maximize the use of 6-unit Type B crafts (b).
    b_max_potential = N // 3
    
    # Check if a = (N - 3*b) / 2 is an integer (i.e., N - 3*b must be even).
    if (N - 3 * b_max_potential) % 2 != 0:
        b_min_crafts = b_max_potential - 1
    else:
        b_min_crafts = b_max_potential
        
    a_min_crafts = (N - 3 * b_min_crafts) // 2
    C_min = a_min_crafts + b_min_crafts

    # --- 3. CALCULATE C_max (Maximum Crafts) ---
    # Strategy: Maximize the use of 4-unit Type A crafts (a).
    
    # Logic based on the parity of N:
    if N % 2 == 0:
        # N is even, max 'a' is N/2
        a_max_crafts = N // 2
    else:
        # N is odd, max 'a' is (N-3)/2
        a_max_crafts = (N - 3) // 2
        
    # b is guaranteed to be an integer now.
    b_max_crafts = (N - 2 * a_max_crafts) // 3
    C_max = a_max_crafts + b_max_crafts

    # Returns space-separated integers as required ("x y")
    return f"{C_min} {C_max}"


def solve_final():
    """
    Reads t, then reads t lines of n, processes all, and prints all output 
    together, while measuring the total execution time.
    """
    start_time = time.perf_counter() # Start high-resolution timer
    
    # Use sys.stdin.readline to read input line by line
    read_line = sys.stdin.readline
    
    # 1. Read t (number of test cases)
    try:
        t_line = read_line().strip()
        if not t_line:
            return
        t = int(t_line)
    except ValueError:
        return

    output = []
    
    # 2. Loop t times to read and process n
    for _ in range(t):
        try:
            n_line = read_line().strip()
            if not n_line:
                break # Stop if input stream ends early
            # n must be read as int to handle numbers up to 10^18
            n = int(n_line) 
        except ValueError:
            continue
        
        # 3. Process and store the result
        result_string = calculate_min_and_max_fleet(n)
        output.append(result_string)

    # 4. Print all results to standard output
    sys.stdout.write('\n'.join(output) + '\n')
    
    # # 5. Calculate and print elapsed time to standard error (sys.stderr)
    # end_time = time.perf_counter()
    # elapsed_time = end_time - start_time
    
    # # This output goes to stderr and does not interfere with the solution's required output
    # sys.stderr.write(f"Execution time for {t} test cases: {elapsed_time:.6f} seconds\n")


if __name__ == "__main__":
    solve_final()