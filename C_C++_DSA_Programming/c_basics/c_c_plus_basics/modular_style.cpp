#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int area(int l, int b)
{
    return l * b;
}

int perimeter(int l, int b)
{
    int p = 2 * (l + b);
    return p;
}

int main()
{

    int length = 1, breadth = 1;

    cout << "Enter length: ";
    cin >> length;
    cout << "Enter breadth: ";
    cin >> breadth;

    int a = area(length, breadth);
    int p = perimeter(length, breadth);

    cout << "Area of Rectangle: " << a << endl;
    cout << "Perimeter of Rectangle: " << p << endl;

    return 0;
}