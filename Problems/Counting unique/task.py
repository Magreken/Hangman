# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'

total_set = set(Belov)
total_set.update(set(Smith))
total_set.update(set(Sarada))

print(len(total_set))
