# Create a list of services using Python. IE: S3, Lambda, EC2, ect.

# The list should be empty initially

aws_services = [] 

# Populate the list using append or insert

aws_services.append('Ec2')
aws_services.append('Lamdba')
aws_services.append('awsRDS')
aws_services.append('dynamodb')
aws_services.append('S3')

print('aws_services')
len('aws_services')

# Remove two specific services for the list by name of by index

aws_services.remove('Ec2')
aws_services.remove('Lamdba')

# Print the new list and the new length of the list

print('aws_services')
len('aws_services')

# Push your code to Github and include the link in your Linkedin write up
