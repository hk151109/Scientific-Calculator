# Scientific Calculator using Python's Tkinter Library

This is a scientific calculator application built using Python's Tkinter library. It provides a modern interface and supports a wide range of mathematical operations, from basic arithmetic to advanced scientific calculations. This project was created as part of learning Python basics.

!(gui.png)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Function Explanations](#function-explanations)
- [Button Explanations](#button-explanations)
  - [1st Row](#1st-row)
  - [2nd Row](#2nd-row)
  - [3rd Row](#3rd-row)
  - [4th Row](#4th-row)
  - [5th Row](#5th-row)
  - [6th to 9th Rows](#6th-to-9th-rows)
- [Extending the Calculator](#extending-the-calculator)
- [Acknowledgments](#acknowledgments)

## Introduction
This scientific calculator application allows users to perform a variety of mathematical operations using a graphical user interface (GUI). It leverages Python's Tkinter library for the GUI and includes functions for arithmetic calculations, trigonometry, logarithms, exponentials, and more.

## Features
- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division.
- **Advanced Mathematical Functions**: Trigonometric functions, logarithms, exponentials, roots, powers.
- **Special Functions**: Factorial, absolute value, percentage calculations.
- **Constants**: Pi (π), Euler's number (e).
- **User-Friendly Interface**: Modern design with a dark theme for enhanced readability.

## Prerequisites
- **Python 3.x** installed on your machine.
- **Required Libraries**:
  - `tkinter` (usually included with Python).
  - `numpy`
  - `math` (standard library module)

## Setup Instructions
1. **Clone or Download the Repository**:

   Save the provided Python script (e.g., `calculator.py`) to a directory on your local machine.

2. **Install Required Libraries**:

   Open your command prompt or terminal and run the following command to install numpy:
   ```bash
   pip install numpy
   ```
   Note: `tkinter` and `math` are typically included with Python installations. If `tkinter` is not installed, you may need to install it separately depending on your operating system.

3. **Run the Application**:

   Navigate to the directory containing the script and execute:
   ```bash
   python calculator.py
   ```
   This will launch the calculator application.

## Usage
### Inputting Numbers and Operations
Click on the buttons to input numbers and select operations. The input will be displayed in the entry field at the top of the calculator.

### Calculating Results
After entering your desired expression, click the `=` button to compute the result, which will be displayed in the entry field.

### Clearing Input
- Use the `DEL` button to delete the last character.
- Use the `AC` button to clear the entire input.

### Special Functions
Utilize the scientific function buttons to perform advanced calculations like trigonometric functions, logarithms, exponentials, etc.

## Function Explanations
Below is an explanation of each function defined in the script and how to use them:
- **`button_click(char)`**: Appends the character `char` to the current input expression.
- **`button_clear_all()`**: Clears the entire input expression.
- **`button_delete()`**: Deletes the last character from the current input expression.
- **`factorial(n)`**: Recursively calculates the factorial of a non-negative integer `n`.
- **`fact_func()`**: Calculates the factorial of the current input number.
- **Trigonometric Functions**: `trig_sin()`, `trig_cos()`, `trig_tan()`, `trig_cot()` for sine, cosine, tangent, and cotangent respectively.
- **Root Functions**: `square_root()`, `third_root()` for square root and cube root calculations.
- **`sign_change()`**: Changes the sign of the current input number.
- **`percent()`**: Calculates the percentage of the current input number.
- **`button_equal()`**: Evaluates the current input expression and displays the result.

## Button Explanations
### 1st Row
- **`abs`**: The absolute value of a number. Example: `abs(-5) = 5`.
- **`mod`**: Modulo operation; finds the remainder of division. Example: `5 % 2 = 1`.
- **`div`**: Floor division; division rounded down. Example: `8 // 3 = 2`.
- **`x!`**: Factorial of a number. Example: `4! = 24`.
- **`e`**: Euler's number. Example: `e ≈ 2.71828`.

### 2nd Row
- **`sin`**: Sine of an angle in degrees. Example: `sin(90) = 1`.
- **`cos`**: Cosine of an angle in degrees. Example: `cos(180) = -1`.
- **`tan`**: Tangent of an angle in degrees. Example: `tan(45) = 1`.
- **`cot`**: Cotangent of an angle in degrees. Example: `cot(45) = 1`.
- **`π`**: Pi. Example: `π ≈ 3.14159`.

### 3rd Row
- **`x²`**: x raised to the power of 2. Example: `4² = 16`.
- **`x³`**: x raised to the power of 3. Example: `5³ = 125`.
- **`xⁿ`**: x raised to any power n. Example: `2⁴ = 16`.
- **`x⁻¹`**: Reciprocal of x. Example: `2⁻¹ = 0.5`.
- **`10ˣ`**: 10 raised to the power of x. Example: `10³ = 1000`.

### 4th Row
- **`√`**: Square root of a number. Example: `√144 = 12`.
- **`∛`**: Cube root of a number. Example: `∛8 = 2`.
- **`ⁿ√`**: Nth root of a number. Example: `⁴√16 = 2`.
- **`log₁₀`**: Logarithm base 10. Example: `log₁₀(1000) = 3`.
- **`ln`**: Natural logarithm. Example: `ln(e) = 1`.

### 5th Row
- **`(`**: Left parenthesis for grouping expressions.
- **`)`**: Right parenthesis for grouping expressions.
- **`±`**: Changes the sign of the current input number.
- **`%`**: Calculates the percentage. Example: `5% = 0.05`.
- **`eˣ`**: Exponential function with base e. Example: `e² ≈ 7.389`.

### 6th to 9th Rows
- **Number Buttons (0 to 9)**: Input digits for constructing numbers.
- **Basic Math Operators**: `+`, `-`, `*`, `/` for addition, subtraction, multiplication, and division.
- **Special Buttons**: `.` (decimal point), `=` (equal sign), `DEL` (delete last character), `AC` (clear all), `EXP` (exponential notation).

## Extending the Calculator
To enhance the calculator's functionality, consider adding the following features:
- **Additional Mathematical Functions**: Hyperbolic functions, inverse trigonometric functions, statistical functions.
- **Memory Functions**: Store and recall values, memory addition, and subtraction.
- **Error Handling**: Improved handling of invalid inputs, user-friendly error messages.
- **GUI Enhancements**: Responsive design for different screen sizes, theme customization options.

## Acknowledgments
This project was developed as part of learning Python basics, focusing on:
- **Python Programming**: Understanding functions, variables, and control structures.
- **GUI Development with Tkinter**: Designing and arranging widgets, styling the interface.
- **Mathematical Computations**: Implementing mathematical operations and functions.

Feel free to use, modify, and extend this calculator as you continue your journey in learning Python!
