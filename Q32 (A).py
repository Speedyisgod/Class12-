##consider a file sport.dat containing records of the fthe structure 
## [sportname,teamname,no_players]
##write a fn copydata() that reads contents of the file sports.dat and copies the record with sport name as basketball to the file name basket.dat.
##the function should return the total number of records copied to file basket.dat

def copydata():
    # Open the source file (sports.dat) and the target file (basket.dat)
    with open('sports.dat', 'r') as infile, open('basket.dat', 'w') as outfile:
        # Initialize the count of records copied
        count = 0
        
        # Read each line in the input file
        for line in infile:
            # Split the line by commas to extract sport name, team name, and number of players
            record = line.strip().split(',')
            
            # If the sport name is 'basketball', write the record to the basket.dat file
            if record[0].strip().lower() == 'basketball':
                outfile.write(line)
                count += 1  # Increment the count of copied records
    
    # Return the total number of records copied
    return count

# Example usage
num_copied = copydata()
print(f"Total records copied: {num_copied}")
