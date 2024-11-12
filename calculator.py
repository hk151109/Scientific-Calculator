from tkinter import *
import math
import numpy as np


'''
Functions
'''
def button_click(char):
    global calc_operator
    calc_operator += str(char)
    text_input.set(calc_operator)

def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")

def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global calc_operator
    result = str(factorial(int(calc_operator)))
    calc_operator = result
    text_input.set(result)

def trig_sin():
    global calc_operator
    result = str(math.sin(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cos():
    global calc_operator
    result = str(math.cos(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_tan():
    global calc_operator
    result = str(math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def trig_cot():
    global calc_operator
    result = str(1/math.tan(math.radians(int(calc_operator))))
    calc_operator = result
    text_input.set(result)

def square_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/2)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def third_root():
    global calc_operator
    if int(calc_operator)>=0:
        temp = str(eval(calc_operator+'**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)

def sign_change():
    global calc_operator
    if calc_operator[0]=='-':
        temp = calc_operator[1:]
    else:
        temp = '-'+calc_operator
    calc_operator = temp
    text_input.set(temp)    

def percent():
    global calc_operator
    temp = str(eval(calc_operator+'/100'))
    calc_operator = temp
    text_input.set(temp)

def button_equal():
    global calc_operator
    temp_op = str(eval(calc_operator))
    text_input.set(temp_op)
    calc_operator = temp_op

'''
Variables
'''
sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
e = math.exp
p = math.pi
E = '*10**'

tk_calc = Tk()
tk_calc.configure(bg="#282c34")
tk_calc.title("Scientific Calculator")

calc_operator = ""
text_input = StringVar()

text_display = Entry(
    tk_calc,
    font=('Helvetica', 24, 'bold'),
    textvariable=text_input,
    bd=0,
    insertwidth=4,
    bg='#1c1f26',        
    fg='#61dafb',        
    justify='right',
    relief=FLAT,
    highlightthickness=2,
    highlightbackground="#61dafb",  
    highlightcolor="#61dafb",
    insertbackground="#61dafb",     
)
text_display.grid(columnspan=5, padx=15, pady=20, ipady=15, sticky="nsew")


button_params = {'bd': 4, 'fg': '#61dafb', 'bg': '#3a3f4b', 'font': ('Arial', 18, 'bold'), 'relief': FLAT}
button_params_main = {'bd': 4, 'fg': '#ffffff', 'bg': '#61dafb', 'font': ('Arial', 18, 'bold'), 'relief': FLAT}

'''
Buttons
'''
# 1st row
abs_value = Button(tk_calc, button_params, text='|x|', command=lambda: button_click('abs(')).grid(row=1, column=0, padx=8, pady=8, sticky="nsew")
modulo = Button(tk_calc, button_params, text='mod', command=lambda: button_click('%')).grid(row=1, column=1, padx=8, pady=8, sticky="nsew")
int_div = Button(tk_calc, button_params, text='div', command=lambda: button_click('//')).grid(row=1, column=2, padx=8, pady=8, sticky="nsew")
factorial_button = Button(tk_calc, button_params, text='x!', command=fact_func).grid(row=1, column=3, padx=8, pady=8, sticky="nsew")
eulers_num = Button(tk_calc, button_params, text='e', command=lambda: button_click(str(math.exp(1)))).grid(row=1, column=4, padx=8, pady=8, sticky="nsew")

# 2nd row
sine = Button(tk_calc, button_params, text='sin', command=trig_sin).grid(row=2, column=0, padx=8, pady=8, sticky="nsew")
cosine = Button(tk_calc, button_params, text='cos', command=trig_cos).grid(row=2, column=1, padx=8, pady=8, sticky="nsew")
tangent = Button(tk_calc, button_params, text='tan', command=trig_tan).grid(row=2, column=2, padx=8, pady=8, sticky="nsew")
cotangent = Button(tk_calc, button_params, text='cot', command=trig_cot).grid(row=2, column=3, padx=8, pady=8, sticky="nsew")
pi_num = Button(tk_calc, button_params, text='π', command=lambda: button_click(str(math.pi))).grid(row=2, column=4, padx=8, pady=8, sticky="nsew")

# 3rd row
second_power = Button(tk_calc, button_params, text='x²', command=lambda: button_click('**2')).grid(row=3, column=0, padx=8, pady=8, sticky="nsew")
third_power = Button(tk_calc, button_params, text='x³', command=lambda: button_click('**3')).grid(row=3, column=1, padx=8, pady=8, sticky="nsew")
nth_power = Button(tk_calc, button_params, text='x^n', command=lambda: button_click('**')).grid(row=3, column=2, padx=8, pady=8, sticky="nsew")
inv_power = Button(tk_calc, button_params, text='x⁻¹', command=lambda: button_click('**(-1)')).grid(row=3, column=3, padx=8, pady=8, sticky="nsew")
tens_powers = Button(tk_calc, button_params, text='10^x', font=('Arial', 16, 'bold'), command=lambda: button_click('10**')).grid(row=3, column=4, padx=8, pady=8, sticky="nsew")

# 4th row
square_root_btn = Button(tk_calc, button_params, text='√', command=square_root).grid(row=4, column=0, padx=8, pady=8, sticky="nsew")
third_root = Button(tk_calc, button_params, text='∛', command=third_root).grid(row=4, column=1, padx=8, pady=8, sticky="nsew")
nth_root = Button(tk_calc, button_params, text='ⁿ√', command=lambda: button_click('**(1/')).grid(row=4, column=2, padx=8, pady=8, sticky="nsew")
log_base10 = Button(tk_calc, button_params, text='log₁₀', font=('Arial', 16, 'bold'), command=lambda: button_click('log(')).grid(row=4, column=3, padx=8, pady=8, sticky="nsew")
log_basee = Button(tk_calc, button_params, text='ln', command=lambda: button_click('ln(')).grid(row=4, column=4, padx=8, pady=8, sticky="nsew")

# 5th row
left_par = Button(tk_calc, button_params, text='(', command=lambda: button_click('(')).grid(row=5, column=0, padx=8, pady=8, sticky="nsew")
right_par = Button(tk_calc, button_params, text=')', command=lambda: button_click(')')).grid(row=5, column=1, padx=8, pady=8, sticky="nsew")
signs = Button(tk_calc, button_params, text='±', command=sign_change).grid(row=5, column=2, padx=8, pady=8, sticky="nsew")
percentage = Button(tk_calc, button_params, text='%', command=percent).grid(row=5, column=3, padx=8, pady=8, sticky="nsew")
ex = Button(tk_calc, button_params, text='e^x', command=lambda: button_click('e(')).grid(row=5, column=4, padx=8, pady=8, sticky="nsew")

# 6th row
button_7 = Button(tk_calc, button_params_main, text='7', command=lambda: button_click('7')).grid(row=6, column=0, padx=8, pady=8, sticky="nsew")
button_8 = Button(tk_calc, button_params_main, text='8', command=lambda: button_click('8')).grid(row=6, column=1, padx=8, pady=8, sticky="nsew")
button_9 = Button(tk_calc, button_params_main, text='9', command=lambda: button_click('9')).grid(row=6, column=2, padx=8, pady=8, sticky="nsew")
delete_one = Button(tk_calc, bd=4, fg='#ffffff', font=('Arial', 18, 'bold'), text='DEL', command=button_delete, bg='#db4437', relief=FLAT).grid(row=6, column=3, padx=8, pady=8, sticky="nsew")
delete_all = Button(tk_calc, bd=4, fg='#ffffff', font=('Arial', 18, 'bold'), text='AC', command=button_clear_all, bg='#db4437', relief=FLAT).grid(row=6, column=4, padx=8, pady=8, sticky="nsew")

# 7th row
button_4 = Button(tk_calc, button_params_main, text='4', command=lambda: button_click('4')).grid(row=7, column=0, padx=8, pady=8, sticky="nsew")
button_5 = Button(tk_calc, button_params_main, text='5', command=lambda: button_click('5')).grid(row=7, column=1, padx=8, pady=8, sticky="nsew")
button_6 = Button(tk_calc, button_params_main, text='6', command=lambda: button_click('6')).grid(row=7, column=2, padx=8, pady=8, sticky="nsew")
mul = Button(tk_calc, button_params_main, text='*', command=lambda: button_click('*')).grid(row=7, column=3, padx=8, pady=8, sticky="nsew")
div = Button(tk_calc, button_params_main, text='/', command=lambda: button_click('/')).grid(row=7, column=4, padx=8, pady=8, sticky="nsew")

# 8th row
button_1 = Button(tk_calc, button_params_main, text='1', command=lambda: button_click('1')).grid(row=8, column=0, padx=8, pady=8, sticky="nsew")
button_2 = Button(tk_calc, button_params_main, text='2', command=lambda: button_click('2')).grid(row=8, column=1, padx=8, pady=8, sticky="nsew")
button_3 = Button(tk_calc, button_params_main, text='3', command=lambda: button_click('3')).grid(row=8, column=2, padx=8, pady=8, sticky="nsew")
add = Button(tk_calc, button_params_main, text='+', command=lambda: button_click('+')).grid(row=8, column=3, padx=8, pady=8, sticky="nsew")
sub = Button(tk_calc, button_params_main, text='-', command=lambda: button_click('-')).grid(row=8, column=4, padx=8, pady=8, sticky="nsew")

# 9th row
button_0 = Button(tk_calc, button_params_main, text='0', command=lambda: button_click('0')).grid(row=9, column=0, padx=8, pady=8, sticky="nsew")
point = Button(tk_calc, button_params_main, text='.', command=lambda: button_click('.')).grid(row=9, column=1, padx=8, pady=8, sticky="nsew")
exp = Button(tk_calc, button_params_main, text='EXP', font=('Arial', 16, 'bold'), command=lambda: button_click(E)).grid(row=9, column=2, padx=8, pady=8, sticky="nsew")
equal = Button(tk_calc, button_params_main, text='=', command=button_equal, bg='#34a853', fg='#ffffff', relief=FLAT).grid(row=9, columnspan=2, column=3, padx=8, pady=8, sticky="nsew")

tk_calc.mainloop()
