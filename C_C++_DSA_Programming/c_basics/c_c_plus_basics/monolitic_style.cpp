#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int main()
{

    int length = 1, breadth = 1;

    cout << "Enter length: ";
    cin >> length;
    cout << "Enter breadth: ";
    cin >> breadth;

    int area = length * breadth;
    int perimeter = 2 * (length + breadth);

    cout << "Area of Rectangle: " << area << endl;
    cout << "Perimeter of Rectangle: " << perimeter << endl;

    return 0;
}