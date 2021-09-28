# Please install Octave Symbolic Package Syms and Sympy in your computer to run this file
# Followe these instructions
#{
>> setenv PYTHON python3
>> system ('curl https://bootstrap.pypa.io/get-pip.py | $PYTHON - --user');
>> system ('$PYTHON -m pip install --user sympy==1.5.1');
>> pkg load symbolic
>> syms x   
#}
# Please note, sympy version must be 1.5.1. New versions will not work with this Syms package and Octave
# Check to see if everything works perfectly, run this command- >> sympref diagnose
# If you need to reset everything, run this command- >> sympref reset

# Install package econometrics for pretty print

# 
# Octave 6.2.0
# MacOS 11.3.1

# Modified SEZQR Model
# Calculate inverse of the transition matrix V
# and multiply inv(V) with the infection matrix F
# Part of MS Thesis at Univertität Koblenz-Landau

# Author- Md Tariqul Islam



clc; clear all;
pkg load symbolic
syms beta rho kappa alpha sigma zeta gamma mu omega
syms N


F = [[0, beta*N, 0]; [0, 0, 0]; [0, 0, 0]];
V = [[rho + kappa, 0, 0]; [zeta - rho, alpha*(N^(1+mu)) + sigma*N + zeta, zeta-omega]; [-kappa, -sigma*N, gamma+omega]];



disp("Determinant of matrix V= ")
det(V)

disp(" ")
disp(" ")
disp(" ")
disp(" ")
disp("Adjugate of matrix V= ")
adjugate = det(V)*inv(V)

disp(" ")
disp(" ")
disp(" ")
disp(" ")
disp("Inverse of matrix V= ")
inv(V)

disp(" ")
disp(" ")
disp(" ")
disp(" ")
disp(" ")
disp(" ")
disp("Matrix multiplication F*inverse(V) = ")
result = F*inv(V)