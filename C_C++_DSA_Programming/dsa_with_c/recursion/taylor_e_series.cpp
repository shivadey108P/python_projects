#include <iostream>
#include <stdio.h>
using namespace std;

double e(int x, int n)
{
    static double p = 1, f = 1;
    double r;
    if (n == 0)
    {
        return 1;
    }

    r = e(x, n - 1);
    p = p * x;
    f = f * n;

    return r + p / f;
}

double iterative_e(int x, int n)
{
    double res = 1;
    for (; n > 0; n--)
    {
        res = 1 + (x / (double)n) * res;
    }
    return res;
}

double horner_rec_e(int x, int n)
{
    static double s = 1;
    if (n == 0)
    {
        return 1;
    }
    s = 1 + ((x / (double)n) * s);
    return e(x, n - 1);
}

int main()
{
    int power = 1, precision = 20;
    cout << horner_rec_e(power, precision);
    return 0;
}