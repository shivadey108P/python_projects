#include <iostream>
using namespace std;

class Element
{
public:
    int i;
    int j;
    int x;
};

class SparseMatrix
{
private:
    int row;
    int col;
    int num;
    Element *e;

public:
    SparseMatrix(int m, int n, int num)
    {
        this->row = m;
        this->col = n;
        this->num = num;
        this->e = new Element[this->num];
    }
    ~SparseMatrix()
    {
        delete[] e;
    }
    void read()
    {
        cout << "Enter non-zero elements(row,col,num): " << endl;
        for (int i = 0; i < num; i++)
        {
            cin >> e[i].i >> e[i].j >> e[i].x;
        }
    }

    void display()
    {
        cout << endl
             << "The matrix is: " << endl;
        int k = 0;
        for (int i = 0; i < row; i++)
        {
            for (int j = 0; j < col; j++)
            {
                if (k < num && e[k].i == i && e[k].j == j)
                {
                    cout << e[k++].x << " ";
                }
                else
                {
                    cout << "0 ";
                }
            }
            cout << endl;
        }
    }

    SparseMatrix *add(SparseMatrix s2)
    {
        int i, j, k;
        i = j = k = 0;
        if (row != s2.row || col != s2.col)
        {
            return NULL;
        }

        SparseMatrix *sum = new SparseMatrix(row, col, num + s2.num);
        while (i < num && j < s2.num)
        {
            if (e[i].i < s2.e[j].i)
            {
                sum->e[k++] = e[i++];
            }
            else if (e[i].i > s2.e[j].i)
            {
                sum->e[k++] = s2.e[j++];
            }
            else
            {
                if (e[i].j < s2.e[j].j)
                {
                    sum->e[k++] = e[i++];
                }
                else if (e[i].j > s2.e[j].j)
                {
                    sum->e[k++] = s2.e[j++];
                }
                else
                {
                    sum->e[k] = e[i];
                    sum->e[k++].x = e[i++].x + s2.e[j++].x;
                }
            }
        }
        for (; i < num; i++)
        {
            sum->e[k++] = e[i];
        }
        for (; j < s2.num; j++)
        {
            sum->e[k++] = s2.e[j];
        }

        sum->num = k;
        return sum;
    }
};

int main()
{
    SparseMatrix s1(4, 4, 4), s2(4, 4, 4), *s3;
    cout << "Enter matrix details" << endl;
    s1.read();
    s2.read();
    s3 = s1.add(s2);

    if (s3 == NULL)
    {
        cout << "Matrix dimensions do not match. Addition cannot be performed." << endl;
        return 1;
    }

    cout << endl
         << "First matrix: " << endl;
    s1.display();

    cout << endl
         << "Second matrix: " << endl;
    s2.display();

    cout << endl
         << "Sum of matrices: " << endl;
    s3->display();

    delete s3;

    return 0;
}
