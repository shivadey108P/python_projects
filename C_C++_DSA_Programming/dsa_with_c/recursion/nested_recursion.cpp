#include <iostream>
#include <stdio.h>
using namespace std;

int func(int n)
{
    if (n > 100)
        return n - 10;
    return func(func(n + 11));
}

int main()
{
    int r = 20;
    cout << func(r) << endl;
}