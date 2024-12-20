#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()
{

    int A[3][4] = {{1, 2, 3, 4}, {2, 4, 6, 8}, {1, 3, 5, 7}};
    int **C;
    int *B[3];

    B[0] = new int[4];
    B[1] = new int[4];
    B[2] = new int[4];

    C = (int **)malloc(3 * sizeof(int *));
    // C = new int* [3];

    if (C == nullptr)
    {
        cerr << "Memory allocaiton failed for C." << endl;
        return -1;
    }

    // C = new int* [3];
    C[0] = (int *)malloc(4 * sizeof(int));
    C[1] = (int *)malloc(4 * sizeof(int));
    C[2] = (int *)malloc(4 * sizeof(int));

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            C[i][j] = (i) + (j + 1);
        }
    }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cout << C[i][j] << "    ";
        }
        cout << endl;
    }

    free(C);

    return 0;
}
