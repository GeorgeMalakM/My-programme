/*
File: Fraction calculator
Purpose: it calculate fraction operations.
Authors : 
1: Yousef Ehab Mohamed Mohamed ,ID: 20230486 ,Section: S24 .
2: Ali Mahmoud Mohammed Zaki ,ID: 20230627 ,Section: S9.
3: George Malak Magdy Nashed ,ID: 20231042, Section: S27.

Emails :
1:yousefehabel@gmail.com
2:Ali Mahmoud :3lokaweeka2005@gmail.com 
3:georgmalak2004@gmail.com

who did what part:
1: Yousef Ehab Mohamed  :Did the valid input functions, the division function, Main function and contributed in evaluate fraction function.
2: Ali Mahmoud Mohammed :Did the GCF function , the addition and subtraction function and contributed in evaluate fraction function.
3: George Malak Magdy Nashe :Did the simplify function , the multiplication function and contributed in evaluate fraction function.

 Link of algorithm PDF : https://drive.google.com/file/d/1P9NUzHtiJSWeEgNwwLyZ4v0QxHjRqn8h/view?usp=sharing
*/
#include <iostream>
#include <string>
#include <regex>
#include <sstream>
#include <cstdlib>

using namespace std;
//function that make sure input is 2 fractions and an operator only
bool is_valid_input1(string input){
    regex pattern("[+\\-]?[0-9]+/[+\\-]?[0-9]+\\s[+\\-*/]\\s[+\\-]?[0-9]+/[+\\-]?[0-9]+"); //regular expression pattern
    return regex_match(input, pattern);
}
//function that make sure first number is a whole number and second number is a fraction and an operator
bool is_valid_input2(string input){
    regex pattern("[+\\-]?[0-9]+\\s[+\\-*/]\\s[+\\-]?[0-9]+/[+\\-]?[0-9]+"); //regular expression pattern
    return regex_match(input, pattern);
}
// function that make sure first number is a fraction and second number is a whole number
bool is_valid_input3(string input){
    regex pattern("[+\\-]?[0-9]+/[+\\-]?[0-9]+\\s[+\\-*/]\\s[+\\-]?[0-9]+"); //regular expression pattern
    return regex_match(input, pattern);
}
// function that make sure 2 numbers are whole numbers
bool is_valid_input4(string input){
    regex pattern("[+\\-]?[0-9]+\\s[+\\-*/]\\s[+\\-]?[0-9]+");
    return regex_match(input, pattern);
}
// the function gets the greatest common factor between numbers
int GCF(int numb1 , int numb2 ){
    while(numb2!=0){
        int temp = numb1 ;
        numb1 = numb2;
        numb2 = temp % numb2;
    }
    return numb1;
}
// function that divides both numberator and denominator by GCF
void simplify (int &numerator , int &denominator ){
    int common_number = GCF(numerator , denominator);
    numerator /= common_number;
    denominator /= common_number;
}
// function that adds 2 fractions 
void add_fractions(int num1, int den1, int num2, int den2, int &res_num, int &res_den) {
    if ( den1 == 0 || den2 == 0) { // make user denominator is not 0 
        cout << "Error: Division by ZERO" << endl;
        return; 
    }
    res_num = num1 * den2 + num2 * den1;
    res_den = den1 * den2;
    simplify(res_num,res_den);
}
// function that subtract 2 fractions 
void subtract_fractions(int num1, int den1, int num2, int den2, int &res_num, int &res_den) {
    res_num = num1 * den2 - num2 * den1;
    if ( den1 == 0 || den2 == 0) {// make user denominator is not 0 
        cout << "Error: Division by ZERO" << endl;
        return; 
    }
    res_den = den1 * den2;
    simplify(res_num, res_den);
}
// function that multiply 2 fractions 
void multiply_fraction(int num1, int den1, int num2, int den2, int &res_num, int &res_den){
    if ( den1 == 0 || den2 == 0) {// make user denominator is not 0 
        cout << "Error: Division by ZERO" << endl;
        return; 
    }
    res_num = num1 * num2;
    res_den = den1 * den2;
    simplify(res_num, res_den);
}
// function that divides 2 fractions 
void divide_fraction(int num1, int den1, int num2, int den2, int &res_num, int &res_den){
    if (num2 == 0 || den1 == 0 || den2 == 0) {// make user denominator is not 0 
        cout << "Error: Division by ZERO" << endl;
        return; 
    }
    res_num = num1 * den2;
    res_den = den1 * num2;
    simplify(res_num, res_den);
}
// function that evaluate expression using sstream to get each element in the input to its intended variable
void evaluateExpression(const string &expression) {
    stringstream ss(expression);
    char op;
    int num1, den1, num2, den2;
    if (is_valid_input1(expression)){
        ss >> num1;
        ss.ignore(); // Ignore '/'
        ss >> den1;
        ss >> op >> num2;
        ss.ignore(); // Ignore '/'
        ss >> den2;

    }
    else if(is_valid_input2(expression)){
        ss >> num1;
        den1 = 1;
        ss >> op >> num2;
        ss.ignore(); // Ignore '/'
        ss >> den2;
    }
    else if(is_valid_input3(expression)){
        ss >> num1;
        ss.ignore(); // Ignore '/'
        ss >> den1;
        ss >> op >> num2;
        den2 = 1;
    }
    
        else if(is_valid_input4(expression)){
        ss >> num1;
        den1 = 1;
        ss >> op >> num2;
        den2 = 1;
    }

    int res_num, res_den;
    switch(op) { // switch to handle each case 
        case '+':
            add_fractions(num1, den1, num2, den2, res_num, res_den);
            if (res_den == 0){
                return;
            }
            break;
        case '-':
            subtract_fractions(num1, den1, num2, den2, res_num, res_den);
            if (res_den == 0){
                return;
            }
            break;
        case '*':
            multiply_fraction(num1, den1, num2, den2, res_num, res_den);
            if (res_den == 0){
                return;
            }
            break;
        case '/':
            divide_fraction(num1, den1, num2, den2, res_num, res_den);
            if (res_den == 0 || res_num == 0){
                return;
            }
            break;
        default:
            cout << "invalid expression" << endl;
            return;
    }
    if (res_den == 1){
        cout << "Result: " << res_num << endl;
    }
    else{
        cout << "Result: " << res_num << "/" << res_den << endl;

    }
}
// ==========> main function <==========
int main(){
    string input;
    cout << "Welcome to FRACTION Calculator" << endl;
    cout << "Notes: Please don't enter spaces between numbers" << endl;
    cout << "Enter organized fraction like 5/7 + 6/4" << endl;
    cout << "Enter 0 if you don't want to continue" << endl;
    while(true){ //loops till user input 'exit'
        cout << "enter your expression : ";
        getline(cin,input);
        if (input == "0" ){
            cout << "Exiting program " << endl;
            break;
        }
        if (is_valid_input1(input)){

            evaluateExpression(input);
        }
        else if (is_valid_input2(input)){
            evaluateExpression(input);

        }
        else if (is_valid_input3(input)){
            evaluateExpression(input);
        }
        else if (is_valid_input4(input)){
            evaluateExpression(input);
        }
        else {
            cout << "invalid input please try again " << endl;
            continue;
        }
    }
}   