#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

struct Rectangle
{
    int length;
    int breadth;
};

void func(struct Rectangle *rect)
{
    rect->length = 15;
    cout << "length: " << rect->length << endl
         << "breadth: " << rect->breadth << endl;
}

int main()
{
    struct Rectangle r = {10, 5};

    func(&r);

    cout << "length: " << r.length << endl
         << "breadth: " << r.breadth << endl;

    return 0;
}