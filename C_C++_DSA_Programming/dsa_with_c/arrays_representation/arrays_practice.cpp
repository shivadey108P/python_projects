#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()
{
    int n = 5;
    int A[5] = {2, 4, 6, 8, 10};
    int *p;
    p = (int *)malloc(n * sizeof(int));

    /*cout << "Print even array with static" << endl;

    for (int i = 0; i < n; i++) {
        cout << A[i] << endl;
    }*/

    for (int i = 0; i < n; i++)
    {
        p[i] = 2 * i + 1;
    }

    int *q;
    int m = 10;
    q = (int *)malloc(m * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        q[i] = p[i];
    }

    free(p);
    p = q;
    q = NULL;
    p[5] = 10;

    cout << "Print odd array with malloc" << endl;

    for (int i = 0; i < m; i++)
    {
        cout << p[i] << endl;
    }

    free(p);
}
