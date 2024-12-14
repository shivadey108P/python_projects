#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

struct Rectangle
{
    int length;
    int breadth;
};

int main()
{
    struct Rectangle r = {10, 5};
    struct Rectangle *p = &r;
    (*p).length = 20;
    p->breadth = 10;
    r.length = 10;

    cout << "length r: " << r.length << endl
         << "breadth r:" << r.breadth << endl;
    cout << "length p: " << p->length << endl
         << "breadth p:" << (*p).breadth << endl;

    return 0;
}