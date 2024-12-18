#include <iostream>
using namespace std;

double sin_recursive(double x, int n, double power, double fact)
{
    double term;
    if (n == 0)
    {
        return x;
    }

    term = sin_recursive(x, n - 1, power * x * x, fact * (2 * n) * (2 * n + 1));

    int sign = (n % 2 == 0) ? -1 : 1;

    return term + sign * (power / fact);
}

// double sin_iterate(double x, int n) {
//     double res = x;      // First term is x
//     double power = x;    // Initialize power as x (x^1)
//     double fact = 1;     // Initialize factorial as 1 (1!)
//     int sign = -1;       // The sign alternates, starting with -1 for the second term
//
//     for (int i = 1; i < n; i++) {  // Start at term 2 (x^3 / 3!)
//         power = power * x * x;     // Increase power to next odd power (x³, x⁵, ...)
//         fact = fact * (2 * i) * (2 * i + 1); // Factorial for next odd number (3!, 5!, ...)
//         res = res + sign * (power / fact);   // Add the term with alternating sign
//         sign = -sign;          // Toggle the sign for next term
//     }
//     return res;
// }

double sin_iterate(double x, double n)
{
    double power = x, fact = 1;
    double res = x;

    for (int i = 1; i <= n; i++)
    {
        power = power * x;
        fact = fact * i;
        int sign = (i % 2 == 0) ? -1 : 1;
        if (i % 2 != 0)
        {
            res = res + (sign * (power / fact));
        }
    }
    return res;
}

double sin_x(double x, int terms)
{
    // return sin_recursive(x, terms, x, 1);
    return sin_iterate(x, terms);
}

int main()
{
    double x = 1.0;
    int terms = 10;

    cout << "sin(" << x << ") = " << sin_x(x, terms) << endl;
    return 0;
}
