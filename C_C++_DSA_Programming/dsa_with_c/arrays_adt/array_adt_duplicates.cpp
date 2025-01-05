#include <iostream>
using namespace std;

class Array
{
private:
    int *A;
    int size;
    int length;

public:
    Array()
    {
        size = 20;
        length = 0;
        A = new int[size];
    }
    ~Array()
    {
        delete[] A;
    }

    void display()
    {
        cout << "Elements are: " << endl;
        for (int i = 0; i < length; i++)
        {
            cout << A[i] << " ";
        }
        cout << endl;
    }

    void append(int element)
    {
        if (length < size)
        {
            A[length++] = element;
        }
        else
        {
            cout << "No space left in the array to insert a new element!" << endl;
        }
    }

    void find_duplicates()
    {
        int last_duplicate = 0;
        for (int i = 0; i < length - 1; i++)
        {
            if (A[i + 1] == A[i] && A[i] != last_duplicate)
            {
                cout << A[i] << endl;
                last_duplicate = A[i];
            }
        }
    }

    void count_duplicates()
    {
        int i, j;
        i = j = 0;
        for (; i < length - 1; i++)
        {
            if (A[i + 1] == A[i])
            {
                j = i + 1;
                while (A[j] == A[i])
                {
                    j++;
                }
                cout << A[i] << " is appearing " << j - i << " times!" << endl;
                i = j - 1;
            }
        }
    }

    void find_duplicates_hash()
    {
        int h = A[length - 1];
        int *hash = new int[h + 1]{0};
        for (int i = 0; i < length; i++)
        {
            hash[A[i]]++;
        }
        for (int i = 0; i <= h; i++)
        {
            if (hash[i] > 1)
            {
                cout << i << " is duplicated " << hash[i] << " times!" << endl;
            }
        }
        delete[] hash;
    }

    int max_value()
    {
        int max_element = A[0];
        for (int i = 0; i < length; i++)
        {
            if (A[i] > max_element)
            {
                max_element = A[i];
            }
        }
        return max_element;
    }

    void find_duplicate_unsorted_hash()
    {
        int h = max_value() + 1;
        int *hash = new int[h]{0};
        for (int i = 0; i < length; i++)
        {
            hash[A[i]]++;
        }
        for (int i = 0; i < h; i++)
        {
            if (hash[i] > 1)
            {
                cout << i << " is duplicated " << hash[i] << " times!" << endl;
            }
        }

        delete[] hash;
    }

    int linear_search(int element)
    {
        for (int i = 0; i < length; i++)
        {
            if (A[i] == element)
                return i;
        }
        return -1;
    }

    void find_duplicates_unsorted()
    {
        int i, j, count;
        for (i = 0; i < length - 1; i++)
        {
            count = 1;
            if (A[i] != -1)
            {
                for (j = i + 1; j < length; j++)
                {
                    if (A[j] == A[i])
                    {
                        count++;
                        A[j] = -1;
                    }
                }
                if (count > 1)
                {
                    cout << A[i] << " is duplicated " << count << " times!" << endl;
                }
            }
        }
    }

    void find_pair_unsorted_hash(int target)
    {
        int h = max_value() + 1;
        int *hash = new int[h]{0};
        for (int i = 0; i < length; i++)
        {
            int comp = target - A[i];
            if (comp >= 0 && hash[comp] != 0)
            {
                printf("%d + %d = %d \n", A[i], target - A[i], target);
            }
            hash[A[i]]++;
        }
    }

    void find_pair_unsorted(int k)
    {
        for (int i = 0; i < length - 1; i++)
        {
            for (int j = i + 1; j < length; j++)
            {
                if (A[i] + A[j] == k)
                {
                    printf("%d + %d = %d\n", A[i], A[j], k);
                }
            }
        }
    }

    void find_pair_unsorted_indices(int k)
    {
        for (int i = 0; i < length - 1; i++)
        {
            for (int j = i + 1; j < length; j++)
            {
                if (A[i] + A[j] == k)
                {
                    printf("[%d, %d]\n", i, j);
                }
            }
        }
    }

    void find_indices_pair_elements_unsorted_hash(int k)
    {
        int h = max_value() + 1;
        int *hash = new int[h]{0};
        for (int i = 0; i < length; i++)
        {
            int comp = k - A[i];
            if (comp >= 0 && hash[comp] != 0)
            {
                printf("(%d,%d)\n", i, linear_search(k - A[i]));
            }
            hash[A[i]]++;
        }
    }

    void find_pair_sorted(int k)
    {
        int i, j;
        i = 0;
        j = length - 1;
        while (i < j)
        {
            if (A[i] + A[j] == k)
            {
                printf("%d + %d = %d\n", A[i], A[j], k);
                printf("[%d,%d]\n", i, j);
                i++;
                j--;
            }
            else if (A[i] + A[j] > k)
            {
                j--;
            }
            else
            {
                i++;
            }
        }
    }
};

int main()
{
    Array arr;
    int target = 10;
    arr.append(1);
    arr.append(3);
    arr.append(4);
    arr.append(5);
    arr.append(6);
    arr.append(8);
    arr.append(9);
    arr.append(10);
    arr.append(12);
    arr.append(14);
    arr.display();
    // arr.find_duplicates();
    // arr.count_duplicates();
    // arr.find_duplicates_unsorted();
    // arr.find_pair_unsorted_hash(target);
    // arr.find_indices_pair_elements_unsorted_hash(target);
    // arr.find_pair_unsorted(target);
    // arr.find_pair_unsorted_indices(target);
    arr.find_pair_sorted(target);

    return 0;
}