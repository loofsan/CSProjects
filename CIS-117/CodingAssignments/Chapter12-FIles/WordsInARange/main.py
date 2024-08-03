def main():
    # Prompt for input file name
    file_name = input().strip()
    
    # Prompt for lower and upper bounds
    lower_bound = input().strip()
    upper_bound = input().strip()
    
    try:
        # Read contents of the file
        with open(file_name, 'r') as file:
            lines = file.readlines()
            
            # Strip newline characters and extra whitespace correctly
            strings = [line.strip() for line in lines]
            
            # Output the results
            for string in strings:
                if lower_bound <= string <= upper_bound:
                    print(f"{string} - in range")
                else:
                    print(f"{string} - not in range")
                    
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

if __name__ == 