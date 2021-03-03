
# 1) Implement Python's Range() Function.
for i in range(1, 10):
    print("Current value of i is:", i)


# 2) Write the generator Function to print prime Numbers.

def all_primes(N):
    
    primes = []
    for n in range(2, N+1):
        is_n_prime = True
        for p in primes:
            if n%p == 0:
                is_n_prime = False
                break
        if is_n_prime:
            primes.append(n)
            yield n

#3) Use Generators to read the file And Print all the words in a file.

print(" Prin all the words in a file")

file = open("mytxt.txt","r")
def Genfun():
    words = file.readlines()
    for i in words:
        yield i 
y = Genfun()

for i in y:
    print(i)


    




# Decorators Problems:
#  Problem 1:
# You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

# For Henry Davids, the output should be:

# Mr. Henry Davids
# For Mary George, the output should be:

# Ms. Mary George


# Input :

# Mike Thomson 20 M
# Robert Bustle 32 M
# Andria Bustle 30 F

# output:

# Mr. Mike Thomson
# Ms. Andria Bustle
# Mr. Robert Bustle


import operator

def person_lister(f):
    def inner(people):
        
        return map(f, sorted(people, key=lambda x: int(x[2])))
       
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


#     Problem  :2

# Standardize Mobile Number Using Decorators

# You are given  mobile numbers. Sort them in ascending order then print them in the standard format shown below:


# The given mobile numbers may have +91,91,  or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all.

# Input Format

# The first line of input contains an integer N, the number of mobile phone numbers.
#  N lines follow each containing a mobile number.

# Output Format

# Print  N mobile numbers on separate lines in the required format.


# Sample Input


# 07895462130
# 919875641230
# 9195969878
# Sample Output

# +91 78954 62130
# +91 91959 69878
# +91 98756 41230

def wrapper(f):
    def fun(l):

        f(['+91 ' + c[-10:-5] + ' ' + c[-5:] for c in l])
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 