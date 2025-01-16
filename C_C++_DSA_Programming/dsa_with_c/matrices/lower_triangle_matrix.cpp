#include <iostream>
using namespace std;

class LowerTriangleMatrix
{
private:
    int *A;
    int n;

public:
    LowerTriangleMatrix()
    {
        n = 2;
        A = new int[(2 * (2 + 1)) / 2];
    }
    LowerTriangleMatrix(int n)
    {
        this->n = n;
        A = new int[(n * (n + 1)) / 2];
    }
    ~LowerTriangleMatrix()
    {
        delete[] A;
    }
    void set(int i, int j, int value);
    int get(int i, int j);
    void display();
};

void LowerTriangleMatrix::set(int i, int j, int value)
{
    if (i >= j)
    {
        A[((i * (i - 1)) / 2) + j - 1] = value;
    }
}

int LowerTriangleMatrix::get(int i, int j)
{
    if (i >= j)
    {
        return A[((i * (i - 1)) / 2) + j - 1];
    }
    else
    {
        return 0;
    }
}

void LowerTriangleMatrix::display()
{
    cout<< "The Lower Triangle Matrix is: " << endl;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (i >= j)
                cout << A[((i * (i - 1)) / 2) + j - 1] << " ";
            else
                cout << 0 << " ";
        }
        cout << endl;
    }
}

int main()
{
    int x;
    LowerTriangleMatrix l1(4);
    cout << "Enter the lower triangle matrix elements: " << endl;
    for (int i = 1; i <= 4; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            cin >> x;
            l1.set(i, j, x);
        }
    }
    l1.display();
    return 0;
}