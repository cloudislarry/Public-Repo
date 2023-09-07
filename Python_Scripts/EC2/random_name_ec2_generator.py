import random

def generate_ec2_names(num_instances, department):
    names = []
    for i in range(num_instances):
        # generate a random string of 5 characters
        rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        # create the unique EC2 name using department name and random string
        name = f"{department}-EC2-{rand_str}"
        names.append(name)
    return names

# department options
department_options = ["Marketing", "Accounting", "FinOps"]

# get user inputs
num_instances = int(input("How many EC2 instances do you want names for? "))
department = input("What is the name of your department? ")

# check if department is valid
if department.capitalize() not in department_options:
    print(f"Sorry, {department} is not a valid department for using this Name Generator.")
else:
    # generate and output unique EC2 names
    ec2_names = generate_ec2_names(num_instances, department)
    print(ec2_names)