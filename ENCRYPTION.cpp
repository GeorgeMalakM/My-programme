#include <iostream>
#include <string>
#include <cctype>
using namespace std ;
//function one to encryption and decode 
string one(const string& mess) {
    string final_message = "";
    string code_one = "zyxwvutsrqponmlkjihgfedcba";
    for (char i : mess) {
        i = tolower(i);
        if (isalpha(i)) {
            char you_message = code_one[i - 'a'];
            final_message += you_message;
        }
    }
    return final_message;
}
//second function with different method with the same approch
string two(const string& mess) {
    string code_two = "mlkjihgfedcbazyxwvutsrqpon";
    string final_message = "";
    for (char i : mess) {
        i = tolower(i);
        if (isalpha(i)) {
            char you_message = code_two[i - 'a'];
            final_message += you_message;
        }
    }
    return final_message;
}
//***************main programme***************
int main() {
    cout << "Hello to Atabsh Cipher" << endl; //Welcome message 
    cout << "You should enter your message with shift you want 1 or 2" << endl; //note for coreect shift
    while (true) {
        cout << "You can encrypt and decode in one time." << endl;//another note
        string message;
        cout << "Enter your message: ";
        getline(cin, message);
        int shift;
        cout << "Please enter your shift from 1 to 2: ";
        cin >> shift;
        //check if shift is coreect choose
        while (shift < 1 || shift > 2) {
            cout << "Please enter correct shift from 1 to 2: ";
            cin >> shift;
        }
        //generate the message
        cin.ignore(); 
        if (shift == 1) {
            string en_message = one(message);
            cout << "Your message is: " << en_message << endl;
        } else if (shift == 2) {
            string en_message = two(message);
            cout << "Your message is: " << en_message << endl;
        }
        break;
    }
    return 0;
}


