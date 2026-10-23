#literals is a raw data given in a variable or constant. 
# It is a fixed value that is assigned to a variable. 
# In Python, literals can be of different types such as 
# string literals, numeric literals, boolean literals,special literals etc.

#numeric literals are immutable (cannot be altered) and can be of three types: int, float, complex.
#int literals are whole numbers without a decimal point. They can be positive or negative.
#float literals are numbers with a decimal point. They can be positive or negative.
#complex literals are numbers with a real and imaginary part. They can be positive or negative.

a = 100 #decimal literal
b = 0b1100100 #binary literal
c = 0o144 #octal literal
d= 0x64 #hexadecimal literal

float_num1 = 10.5 #float literal
float_num2 = 1.5e2 #150.0 float literal
float_num3 = 1.5e-2 #0.015 float literal

complex_num = 3.14j #complex literal    
print(complex_num.imag,complex_num.real,complex_num.conjugate())

#string literals are immutable (cannot be altered) and can be of three types: single quoted, double quoted, triple quoted.
single_quoted_string = 'Hello, World!' #single quoted string literal
double_quoted_string = "Hello, World!" #double quoted string literal
triple_quoted_string = '''Hello, World!''' #triple quoted string literal
print(single_quoted_string)
print(double_quoted_string)
print(triple_quoted_string)
unicode = u'\u00dcnic\u00f6de' #unicode string literal
print(unicode)
raw_string = r'raw \n string' #raw string literal
print(raw_string)

#boolean literals are immutable (cannot be altered) and can be of two types: True and False.
is_true = True #boolean literal
a = True + 4
print(a)

#special literals are immutable (cannot be altered) and can be of two types: None and Ellipsis.
none_literal = None #None literal
print(none_literal)
#none is a special literal that represents the absence of a value or a null value. It is often used to indicate that a variable has no value or that a function does not return anything.
#variable declared