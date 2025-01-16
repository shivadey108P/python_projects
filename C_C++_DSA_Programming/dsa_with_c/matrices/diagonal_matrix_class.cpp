#include <iostream>
using namespace std;

class Diagonal
{
private:
    int *A;
    int n;

public:
    Diagonal(){
        n=2;
        A= new int[2];
    }

    Diagonal(int n)
    {
        this->n = n;
        A = new int[n];
    }
    ~Diagonal(){
        delete [] A;
    }
    void set_value(int i, int j, int value);
    int get_value(int i, int j);
    void display();
};

void Diagonal::set_value(int i, int j, int value)
{
    if (i == j)
    {
        A[i - 1] = value;
    }
}

int Diagonal::get_value(int i, int j)
{
    if (i == j)
    {
        return A[i - 1];
    }
    else
    {
        return 0;
    }
}

void Diagonal::display()
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == j)
            {
                cout << A[i] << " ";
            }
            else
            {
                cout << 0 << " ";
            }
        }
        cout << endl;
    }
}

int main()
{

    Diagonal d(5);
    d.set_value(1, 1, 5);
    d.set_value(2, 2, 3);
    d.set_value(3, 3, 2);
    d.set_value(4, 4, 6);
    d.set_value(5, 5, 1);

    cout << "The value at (3,3) is: " << d.get_value(3, 3) << endl;
    d.display();

    return 0;
}