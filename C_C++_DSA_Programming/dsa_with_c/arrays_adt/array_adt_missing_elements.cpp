#include <iostream>
using namespace std;

template <class T>
class Array
{
private:
    T *A;
    int size;
    int length;

public:
    Array()
    {
        size = 10;
        A = new T[size];
        length = 0;
    }
    Array(int sz)
    {
        size = sz;
        A = new T[size];
        length = 0;
    }

    void display()
    {
        cout << "The elements are: " << endl;
        for (int i = 0; i < length; i++)
        {
            cout << A[i] << " ";
        }
        cout << endl;
    }

    void append(T element)
    {
        if (length < size)
        {
            A[length++] = element;
        }
        else
        {
            cout << "Not enough space left to insert a new element!" << endl;
        }
    }

    void insert(int index, T element)
    {
        if (index >= 0 && index <= length)
        {
            for (int i = length - 1; i >= index; i++)
            {
                A[i + 1] = A[i];
            }
            A[index] = element;
            length++;
        }
        else
        {
            cout << "Not enough space left to insert a new element!" << endl;
        }
    }

    int single_missing_element()
    {
        int n = A[length - 1];
        int s = (n * (n + 1)) / 2;
        int sum = 0;
        for (int i = 0; i < length; i++)
        {
            sum += A[i];
        }
        return s - sum;
    }

    int missing_one_element()
    {
        int diff = A[0];
        for (int i = 0; i < length; i++)
        {
            if (A[i] - i != diff)
            {
                return i + diff;
                break;
            }
        }
        return -1;
    }

    int *missing_multiple_elements(int &count)
    {
        int diff = A[0] - 0;
        count = 0;
        int max_missing_numbers = A[length - 1] - A[0] - (length - 1);
        int *missing_elements = new int[max_missing_numbers];
        for (int i = 0; i < length; i++)
        {
            if (A[i] - i != diff)
            {
                while (diff < A[i] - i)
                {
                    // cout << diff + i << endl;
                    missing_elements[count++] = diff + i;
                    diff++;
                }
            }
        }
        return missing_elements;
    }

    void missing_unsorted_elements(int l, int h){
        int hash[h+1] = {0};
        for(int i=0; i<length ; i++){
            hash[A[i]]++;
        }

        for(int i=l; i<h+1 ; i++){
            if(hash[i] == 0){
                cout<<i<<" ";
            }
        }
    }
};

int main()
{
    // Array<int> *arr;
    // int sz, l;
    // int element;
    // cout << "Enter the size of the array you want: ";
    // cin >> sz;
    // arr = new Array<int>(sz);
    // cout << "Enter the number of elements you want to insert in this array: ";
    // cin >> l;
    // cout << "Now enter the elements: " << endl;
    // for (int i = 0; i < l; i++)
    // {
    //     cin >> element;
    //     arr->insert(i, element);
    // }
    // arr->display();

    Array<int> arr(12);
    arr.append(3);
    arr.append(7);
    arr.append(4);
    arr.append(1);
    arr.append(10);
    arr.append(9);
    arr.append(2);
    arr.append(6);
    arr.append(13);
    arr.append(17);
    arr.append(14);
    arr.append(12);
    arr.display();

    // int *m_elements;
    // int count;

    // cout << "The missing elements are:" << endl;
    // m_elements = arr.missing_multiple_elements(count);
    // for (int i = 0; i < count; i++)
    // {
    //     cout << m_elements[i] << " ";
    // }

    // cout << endl;

    // delete[] m_elements;
    cout << "The missing elements are:" << endl;
    arr.missing_unsorted_elements(1, 17);


    return 0;
}