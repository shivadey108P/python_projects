#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

struct Rectangle
{
    int length;
    int breadth;
};

void initialize_rect(struct Rectangle *r, int l, int b)
{
    r->length = l;
    r->breadth = b;
}

int area(struct Rectangle r)
{
    return r.length * r.breadth;
}

int perimeter(struct Rectangle r)
{
    int p = 2 * (r.length + r.breadth);
    return p;
}

int main()
{

    struct Rectangle r = {1, 1};
    int l, b;
    cout << "Enter length: ";
    cin >> l;
    cout << "Enter breadth: ";
    cin >> b;

    initialize_rect(&r, l, b);

    int a = area(r);
    int p = perimeter(r);

    cout << "Area of Rectangle: " << a << endl;
    cout << "Perimeter of Rectangle: " << p << endl;

    return 0;
}