
#FIND OUT WHAT THE INDENTATION HIRARKEY IS WITH Python

#Comments 
    # is how you initiate comments everything after the # will be a comment there is no way to end comment midline with python
    
"""
    This is a way to create comments you can do a multi line comment
    It creates a string element that so its not proper comment but it works
    
"""

print("hello world")
xyz = "This is my practice program"
print(xyz)
print(5+5, "hey this is my faverate number while", 25+6, "is how old I am turning", end="\n")

# Variable
age = 5
print(age)

# Legal Variable names
"""
You can use Underscore _ 
You can start a variable with a Capital letter but you should not

You can not use - 
You can not start variable with a number
you can not use key words like return 

"""
# import math
"""
result = 10/3
print(math.floor(result))
    will print the 3

Print(math.ceil(result))
    will print 4

new_result= math.floor(result)

print(new_result)
    will print 3
"""

#Operators 
"""
///     / --> float division
///    // --> integer division --> (math.floor)
       % -->  mod
            number = 345345
            limit  = 10
            print (number % limit)
                will print 5
        ** how to raise a power
            print(3**5)
                is 3^5
        You can also use
            import math
            result = math.pow(3, 5)
"""

#String
"""
\n = new line
\x = way to print hex character \x41 would print a 
\" will allow you to print a "
\\ allows you to escape the escape character

Single quotes and double quotes work exactly the same way "Hello" = 'Hello'
    you must pay attention to how your quotes are in your statements 
        'Hello I hope you're doing well' 
            This will throw error because we have three ' marks 
Concatenation 
    msg1= "hello "
    msg2= "ray"
    print(msg1 + msg2 + " Thats the way it works")
    will print hello ray Thats the way it works

How to brake up long strings umungs multiple lines
    msg =( "hello this is a long string...."
             "you see like I said its a long string")
"""