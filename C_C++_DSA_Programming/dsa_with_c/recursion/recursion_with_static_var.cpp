#include <iostream>
#include <stdio.h>
using namespace std;

int func(int n)
{
    static int x = 0;
    if (n > 0)
    {
        x++;
        return func(n - 1)+x;
    }
    return 0;
}

int main()
{
    int num = 5;
    cout << "Number is: " << func(num) << endl;
    return 0;
}