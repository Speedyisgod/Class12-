#  A Binary file, CINEMA.DAT has the following structure:
# {MNO:[MNAME, MTYPE]}
# Where 
# MNO – Movie Number
# MNAME – Movie Name
# MTYPE is Movie Type
# Write a user defined function, findType(mtype), that accepts mtype
# as parameter and displays all the records from the binary file
# CINEMA.DAT, that have the value of Movie Type as mtype
## example
{
    101: ["Inception", "Sci-Fi"],
    102: ["The Dark Knight", "Action"],
    103: ["Titanic", "Romance"],
    104: ["Mad Max: Fury Road", "Action"]
}


import pickle

def findType(mtype):
    # Open the binary file for reading
    with open('CINEMA.DAT', 'rb') as file:
        # Load the entire content of the binary file
        cinema_data = pickle.load(file)
        
        # Initialize a flag to check if any record was found
        found = False
        
        # Iterate over the records in the cinema_data dictionary
        for mno, details in cinema_data.items():
            mname, mtype_recorded = details
            
            # If the movie type matches the given mtype, display the record
            if mtype_recorded == mtype:
                print(f"Movie Number: {mno}, Movie Name: {mname}, Movie Type: {mtype_recorded}")
                found = True
        
        if not found:
            print(f"No movies found with Movie Type: {mtype}")

# Example usage
findType('Action')
