''' 
Import statements: 
    1. Import the built-in json python package
    2. From employee.py, import the details function and the employee_name, age, title variables
'''
### WRITE IMPORT STATEMENTS HERE


def create_dict(name, age, title):
    """ Creates a dictionary that stores an employee's information

    [IMPLEMENT ME]
        1. Return a dictionary that maps "first_name" to name, "age" to age, and "title" to title

    Args:
        name: Name of employee
        age: Age of employee
        title: Title of employee

    Returns:
        dict - A dictionary that maps "first_name", "age", and "title" to the
               name, age, and title arguments, respectively. Make sure that 
               the values are typecasted correctly (name - string, age - int, 
               title - string)
    """
    ### WRITE SOLUTION HERE
    
    

    
    raise NotImplementedError()

def write_json_to_file(json_obj, output_file):
    """ Write json string to file

    [IMPLEMENT ME]
        1. Open a new file defined by output_file
        2. Write json_obj to the new file

    Args:
        json_obj: json string containing employee information
        output_file: the file the json is being written to
    """
    ### WRITE SOLUTION HERE
    

    raise NotImplementedError()

def main():
    # Print the contents of details() -- This should print the details of an employee
    

    # Create employee dictionary
    

    ''' 
    Use a function called dumps from the json module to convert employee_dict
    into a json string and store it in a variable called json_object.
    '''
    ### WRITE YOUR CODE BY MODIFYING THE LINE BELOW
    # In the line below replace the None keyword with your code. 
    # The format should look like: variable = json.dumps(dict)
    

    # Write out the json object to file
    

if __name__ == "__main__":
    main()