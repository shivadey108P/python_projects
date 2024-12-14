#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

struct Rectangle
{
    int length;
    int breadth;
};

struct Test
{
    int n;
    int *A;
};

struct Rectangle *rect_func()
{
    struct Rectangle *r = new Rectangle;
    // struct Rectangle *r = (struct Rectangle*) malloc(sizeof(struct Rectangle));
    r->length = 10;
    r->breadth = 5;

    return r;
}

struct Test *func()
{
    struct Test *t = new Test;
    // struct Test *t = (struct Test*) malloc(sizeof(struct Test));
    t->n = 5;

    t->A = new int[t->n];

    for (int i = 0; i < t->n; i++)
    {
        t->A[i] = i + 1;
    }

    return t;
}

int main()
{
    struct Test *ptr = func();

    for (int i = 0; i < ptr->n; i++)
    {
        cout << ptr->A[i] << " ";
    }

    delete ptr;
    // free(ptr);

    struct Rectangle *r_ptr = rect_func();
    cout << endl
         << "length: " << r_ptr->length << endl
         << "breadth: " << r_ptr->breadth << endl;

    delete r_ptr;
    // free(r_ptr);

    return 0;
}