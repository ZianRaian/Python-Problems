import sys

def possibleChanges(usernames):
    results = []
    
    for username in usernames:
        found = False
        min_right = username[-1]  # Smallest character encountered from the right
        
        # Traverse from right to left
        for i in range(len(username) - 2, -1, -1):
            if username[i] > min_right:  # If a left character is greater than a right character
                found = True
                break
            min_right = min(min_right, username[i])  # Update the smallest character found
        
        results.append("YES" if found else "NO")
    
    return results

# Fast Input Handling for HackerRank
if __name__ == "__main__":
    input_data = sys.stdin.read().splitlines()  # Read all input at once
    n = int(input_data[0])  # Number of usernames
    usernames = input_data[1:n+1]  # Extract usernames
    
    results = possibleChanges(usernames)
    
    print("\n".join(results))  # Print results efficiently
