#include <iostream>
#include <stdio.h>
using namespace std;

void func(int n)
{
    if (n > 0)
    {
        cout << n << " ";
        func(n - 1);
        func(n - 1);
    }
}

int main()
{
    int r = 3;
    func(r);

    return 0;
}