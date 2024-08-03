# TODO: Declare any necessary variables here. 
      
      
# TODO: Read a file name from the user and read the tsv file here. 
   
   
# TODO: Compute student grades and exam averages, then output results to a text file here. 
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # Prompt for input file name
    file_name = input().strip()
    
    # Initialize lists for storing student data and exam scores
    students = []
    midterm1_scores = []
    midterm2_scores = []
    final_scores = []
    
    # Read the TSV file
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Split the line by tabs and strip whitespace
                parts = line.strip().split('\t')
                last_name = parts[0]
                first_name = parts[1]
                midterm1 = int(parts[2])
                midterm2 = int(parts[3])
                final = int(parts[4])
                
                # Calculate average score
                average_score = (midterm1 + midterm2 + final) / 3.0
                
                # Calculate letter grade
                letter_grade = calculate_grade(average_score)
                
                # Append student data to the list
                students.append((last_name, first_name, midterm1, midterm2, final, letter_grade))
                midterm1_scores.append(midterm1)
                midterm2_scores.append(midterm2)
                final_scores.append(final)
            
            # Calculate exam averages
            avg_midterm1 = sum(midterm1_scores) / len(midterm1_scores)
            avg_midterm2 = sum(midterm2_scores) / len(midterm2_scores)
            avg_final = sum(final_scores) / len(final_scores)
            
            # Open the report file to write
            with open('report.txt', 'w') as report_file:
                # Write student information to the report file
                for student in students:
                    report_file.write('\t'.join(map(str, student)) + '\n')
                
                # Write exam averages to the report file
                report_file.write(f"\nAverages: midterm1 {avg_midterm1:.2f}, midterm2 {avg_midterm2:.2f}, final {avg_final:.2f}\n")
                
            print("Report generated successfully.")
            
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except IndexError:
        print(f"Error: Invalid format in '{file_name}'.")

if __name__ == "__main__":
    main()