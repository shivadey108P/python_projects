#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{

    int fact = 1, n = 4;

    for (int i = 1; i <= n; i++)
    {
        if (i == 1)
        {
            cout << i << "! = " << fact << endl;
        }
        fact = fact * (2 * i) * (2 * i + 1);
        cout << 2 * i + 1 << "! = " << fact << endl;
    }

    return 0;
}