#include <iostream>
using namespace std;

double sin_recursive(double x, int n)
{
    static double power = x, fact = 1;
    double res = x;
    
    if (n == 0)
    {
        return x;
    }
    
    res = sin_recursive(x, n - 1);
    power = power * x * x;
    fact =  fact * (2 * n) * (2 * n + 1);
    int sign =  (n%2==0) ? 1:-1;
    return res + (sign *(power/fact));
}

double sin_iterate(double x, double n)
{
    double power = x, fact = 1;
    double res = x;
    int sign = -1;

    for (int i = 1; i <= n; i++)
    {
        power = power * x * x;
        fact = fact * (2 * i) * (2*i+1);
        res = res + (sign * (power / fact));
        sign = -sign;
    }
    return res;
}



double sin_x(double x, int terms)
{
    return sin_recursive(x, terms);
    // return sin_iterate(x, terms);
}

int main()
{
    double x = 2.0;
    int terms = 4;

    cout << "sin(" << x << ") = " << sin_x(x, terms) << endl;
    return 0;
}
