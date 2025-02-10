#include <iostream>
using namespace std;

struct Elements
{
    int i;
    int j;
    int x;
};

struct SparseMatrix
{
    int row;
    int col;
    int num;
    struct Elements *e;
};

void create(struct SparseMatrix *s)
{
    cout << "Enter the dimensions of the matrix" << endl;
    cout << "Enter number of rows: ";
    cin >> s->row;
    cout << "Enter number of columns: ";
    cin >> s->col;
    cout << "Enter number of non-zero elements: ";
    cin >> s->num;
    s->e = (struct Elements *)malloc(s->num * sizeof(struct Elements));
    // s->e = new Elements[s->num];
    if (s->e == nullptr)
    {
        cout << "Memory allocation failed" << endl;
        exit(1);
    }
    cout << "Enter row,col and element for all:" << endl;
    for (int i = 0; i < s->num; i++)
    {
        cin >> s->e[i].i >> s->e[i].j >> s->e[i].x;
    }
}

void display(struct SparseMatrix s)
{
    int k = 0;
    for (int i = 0; i < s.row; i++)
    {
        for (int j = 0; j < s.col; j++)
        {
            if (i == s.e[k].i && j == s.e[k].j && k < s.num)
            {
                cout << s.e[k++].x << " ";
            }
            else
            {
                cout << "0 ";
            }
        }
        cout << endl;
    }
}

struct SparseMatrix *add(struct SparseMatrix *s1, struct SparseMatrix *s2)
{
    int i, j, k;
    i = j = k = 0;
    struct SparseMatrix *sum;
    if (s1->row != s2->row || s1->col != s2->col)
    {
        return NULL;
    }
    sum = (struct SparseMatrix *)malloc(sizeof(SparseMatrix));

    sum->e = (struct Elements *)malloc((s1->num + s2->num) * sizeof(struct Elements));
    if (sum->e == nullptr)
    {
        cout << "Memory space not allocated!" << endl;
        return NULL;
    }

    while (i < s1->num && j < s2->num)
    {
        if (s1->e[i].i < s2->e[j].i)
        {
            sum->e[k++] = s1->e[i++];
        }
        else if (s1->e[i].i > s2->e[j].i)
        {
            sum->e[k++] = s2->e[j++];
        }
        else
        {
            if (s1->e[i].j < s2->e[j].j)
            {
                sum->e[k++] = s1->e[i++];
            }
            else if (s1->e[i].j > s2->e[j].j)
            {
                sum->e[k++] = s2->e[j++];
            }
            else
            {
                sum->e[k] = s1->e[i];
                sum->e[k++].x = s1->e[i++].x + s2->e[j++].x;
            }
        }
    }

    for (; i < s1->num; i++)
    {
        sum->e[k++] = s1->e[i];
    }
    for (; j < s2->num; j++)
    {
        sum->e[k++] = s2->e[j];
    }

    sum->row = s1->row;
    sum->col = s1->col;
    sum->num = k;

    return sum;
}

int main()
{
    struct SparseMatrix s1, s2, *s3;
    cout << "Enter details of 1st matrix: " << endl;
    create(&s1);
    cout << endl
         << "Enter details of 2nd matrix: " << endl;
    create(&s2);
    cout << endl
         << "First Matrix: " << endl;
    ;
    display(s1);
    cout << endl
         << "Second Matrix: " << endl;
    ;
    display(s2);
    cout << endl
         << "Sum of two matrices " << endl;
    s3 = add(&s1, &s2);
    display(*s3);

    free(s3);
    free(s1.e);
    free(s2.e);
    return 0;
}
