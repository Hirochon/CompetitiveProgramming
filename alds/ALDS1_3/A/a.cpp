#include <iostream>
#include <stack>
#include <string>
using namespace std;

stack<int> S;

int main() {
    string s;
    int num, num1, num2;
    while (cin >> s) {
        if (s[0] == '+') {
            num2 = S.top();
            S.pop();
            num1 = S.top();
            S.pop();
            S.push(num1 + num2);
        }
        else if (s[0] == '-') {
            num2 = S.top();
            S.pop();
            num1 = S.top();
            S.pop();
            S.push(num1 - num2);
        }
        else if (s[0] == '*') {
            num2 = S.top();
            S.pop();
            num1 = S.top();
            S.pop();
            S.push(num1 * num2);
        }
        else {
            num = stoi(s);
            S.push(num);
        }
    }
    cout << S.top() << endl;
    return 0;
}