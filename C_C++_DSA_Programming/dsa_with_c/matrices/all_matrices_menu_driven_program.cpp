#include <iostream>
// using namespace std;

class DiagonalMatrix
{
private:
    int *A;
    int n;

public:
    DiagonalMatrix() : DiagonalMatrix(2) {}
    DiagonalMatrix(int n)
    {
        this->n = n;
        A = new int[n];
    }
    ~DiagonalMatrix()
    {
        delete[] A;
    }

    void set(int i, int j, int value)
    {
        if (i == j)
        {
            A[i - 1] = value;
        }
    }

    void create()
    {
        int value;
        std::cout << "Enter the matrix elements: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cin >> value;
                set(i, j, value);
            }
        }
    }

    int get(int i, int j)
    {

        if (i == j)
        {
            return A[i - 1];
        }
        return 0;
    }

    void display()
    {
        std::cout << "The matrix elements are: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cout << get(i, j) << " ";
            }
            std::cout << std::endl;
        }
    }
};

class LowerTriangular
{
private:
    int *A;
    int n;

public:
    LowerTriangular() : LowerTriangular(2) {}
    LowerTriangular(int n)
    {
        this->n = n;
        A = new int[(n * (n + 1)) / 2];
    }
    ~LowerTriangular()
    {
        delete[] A;
    }

    void set(int i, int j, int value)
    {
        if (i >= j)
        {
            A[(i * (i - 1)) / 2 + (j - 1)] = value;
        }
    }

    void create()
    {
        int value;
        std::cout << "Enter the matrix elements: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cin >> value;
                set(i, j, value);
            }
        }
    }

    int get(int i, int j)
    {

        if (i >= j)
        {
            return A[(i * (i - 1)) / 2 + (j - 1)];
        }
        return 0;
    }

    void display()
    {
        std::cout << "The matrix elements are: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cout << get(i, j) << " ";
            }
            std::cout << std::endl;
        }
    }
};

class SymmetricMatrix
{
private:
    int *A;
    int n;

public:
    SymmetricMatrix() : SymmetricMatrix(2) {}
    SymmetricMatrix(int n)
    {
        this->n = n;
        A = new int[(n * (n + 1)) / 2];
    }
    ~SymmetricMatrix()
    {
        delete[] A;
    }

    void set(int i, int j, int value)
    {
        if (i >= j)
        {
            A[(i * (i - 1)) / 2 + (j - 1)] = value;
        }
    }

    void create()
    {
        int value;
        std::cout << "Enter the matrix elements: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cin >> value;
                set(i, j, value);
            }
        }
    }

    int get(int i, int j)
    {

        if (i >= j)
        {
            return A[(i * (i - 1)) / 2 + (j - 1)];
        }
        else
        {
            int temp = i;
            i = j;
            j = temp;
            return A[(i * (i - 1)) / 2 + (j - 1)];
        }
    }

    void display()
    {
        std::cout << "The matrix elements are: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cout << get(i, j) << " ";
            }
            std::cout << std::endl;
        }
    }
};

class UpperTriangular
{
private:
    int *A;
    int n;

public:
    UpperTriangular() : UpperTriangular(2) {}
    UpperTriangular(int n)
    {
        this->n = n;
        A = new int[(n * (n + 1)) / 2];
    }
    ~UpperTriangular()
    {
        delete[] A;
    }

    void set(int i, int j, int value)
    {
        if (i <= j)
        {
            A[n * (i - 1) - ((i - 2) * (i - 1) / 2) + (j - i)] = value;
        }
    }

    void create()
    {
        int value;
        std::cout << "Enter the matrix elements: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cin >> value;
                set(i, j, value);
            }
        }
    }

    int get(int i, int j)
    {

        if (i <= j)
        {
            return A[n * (i - 1) - ((i - 2) * (i - 1) / 2) + (j - i)];
        }
        return 0;
    }

    void display()
    {
        std::cout << "The matrix elements are: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cout << get(i, j) << " ";
            }
            std::cout << std::endl;
        }
    }
};

class TriDiagonalMatrix
{
private:
    int *A;
    int n;

public:
    TriDiagonalMatrix() : TriDiagonalMatrix(2) {}
    TriDiagonalMatrix(int n)
    {
        this->n = n;
        A = new int[3 * n - 2];
    }
    void set(int i, int j, int value)
    {
        if (i - j == 1)
        {
            A[i - 2] = value;
        }
        else if (i - j == 0)
        {
            A[n - 1 + i - 1] = value;
        }
        else if (i - j == -1)
        {
            A[2 * n - 1 + i - 1] = value;
        }
    }
    int get(int i, int j)
    {
        if (i - j == 1)
        {
            return A[i - 2];
        }
        else if (i - j == 0)
        {
            return A[n - 1 + i - 1];
        }
        else if (i - j == -1)
        {
            return A[2 * n - 1 + i - 1];
        }
        else
        {
            return 0;
        }
    }
    void create()
    {
        int value;
        std::cout << "Enter the matrix elements: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cin >> value;
                set(i, j, value);
            }
        }
    }

    void display()
    {
        std::cout << "The matrix elements are: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cout << get(i, j) << " ";
            }
            std::cout << std::endl;
        }
    }
};

class ToeplitzMatrix
{
private:
    int *A;
    int n;

public:
    ToeplitzMatrix() : ToeplitzMatrix(2) {}
    ToeplitzMatrix(int n)
    {
        this->n = n;
        A = new int[2 * n - 1];
    }

    void set(int i, int j, int value)
    {
        if (i <= j)
        {
            A[j - i] = value;
        }
        else if (i > j)
        {
            A[n + (i - j - 1)] = value;
        }
    }

    int get(int i, int j)
    {
        if (i <= j)
        {
            return A[j - i];
        }
        else if (i > j)
        {
            return A[n + (i - j - 1)];
        }
    }

    void create()
    {
        int value;
        std::cout << "Enter the matrix elements: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cin >> value;
                set(i, j, value);
            }
        }
    }

    void display()
    {
        std::cout << "The matrix elements are: " << std::endl;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                std::cout << get(i, j) << " ";
            }
            std::cout << std::endl;
        }
    }
};

int main()
{
    int size;
    int choice;
    int type_of_diagonal_matrix;
    std::cout << "Enter the choice of matrix you want to produce:" << std::endl;
    std::cout << "1. Diagonal Matrix" << std::endl;
    std::cout << "2. Lower Traingular Matrix" << std::endl;
    std::cout << "2. Lower Traingular Matrix" << std::endl;
    std::cout << "3. Upper Traingular Matrix" << std::endl;
    std::cout << "4. Symmetrical Matrix" << std::endl;
    std::cout << "5. Tri-Diagonal Matrix" << std::endl;
    std::cout << "6. Toeplitz Matrix" << std::endl;
    std::cin >> type_of_diagonal_matrix;

    std::cout << "Enter the size of matrix you want to produce(just enter either the row or coloumn size): ";
    std::cin >> size;
    DiagonalMatrix d1(size);

    do
    {
        std::cout << std::endl
                  << "Menu: " << std::endl;
        std::cout << "1. Create the matrix." << std::endl;
        std::cout << "2. Set an element" << std::endl;
        std::cout << "3. Get an element" << std::endl;
        std::cout << "4. Display whole matrix" << std::endl;
        std::cout << "5. Exit" << std::endl;
        std::cout << "Enter your choice here: ";
        std::cin >> choice;
        std::cout << std::endl;
        switch (choice)
        {
        case 1:
            d1.create();
            break;
        case 2:
        {
            int i, j, value;
            std::cout << "Enter index i: ";
            std::cin >> i;
            std::cout << std::endl
                      << "Enter index j: ";
            std::cin >> j;
            std::cout << std::endl
                      << "Enter the value you want to enter: ";
            std::cin >> value;
            d1.set(i, j, value);
            break;
        }
        case 3:
        {
            int i, j;
            std::cout << "Enter index i: ";
            std::cin >> i;
            std::cout << std::endl
                      << "Enter index j: ";
            std::cin >> j;
            std::cout << "The value is: " << d1.get(i, j) << std::endl;
            break;
        }
        case 4:
            d1.display();
            break;
        default:
            break;
        }
    } while (choice < 5);
}
