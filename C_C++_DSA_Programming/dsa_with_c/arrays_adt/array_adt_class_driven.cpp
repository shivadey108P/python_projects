#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

class Array
{
private:
    int *A;
    int size;
    int length;
    void swap(int *x, int *y);

public:
    Array()
    {
        size = 10;
        length = 0;
        A = new int[size];
    }
    Array(int sz)
    {
        size = sz;
        length = 0;
        A = new int[size];
    }
    ~Array()
    {
        delete[] A;
    }

    int *get_Array()
    {
        return A;
    }

    int get_length()
    {
        return length;
    }

    void display_array();
    void append(int value);
    void insert(int index, int value);

    int delete_element(int index);
    int LinearSearch(int value);
    int BinarySearch(int value);
    int recursionBinarySearch(int a[], int left, int right, int value);
    void sortArray();
    int get_value(int index);
    void set_value(int index, int value);
    int max_value();
    int min_value();
    int sum_of_values();
    float avg_of_values();
    bool is_sorted();
    void reverse_array();
    void reverse_swap();
    void inserted_sorted_value(int value);
    void rearrange_array();
    void left_shift();
    void left_rotate();
    void right_shift();
    void right_rotate();
    Array *merge_array(Array arr2);
    Array *union_array(Array arr2);
    Array *intersect_array(Array arr2);
    Array *diff_array(Array arr2);
};

void Array::display_array()
{
    cout << "Elements in the array are: " << endl;
    for (int i = 0; i < length; i++)
    {
        cout << A[i] << " ";
    }
    cout << endl;
}

void Array::append(int value)
{
    if (length < size)
    {
        A[length++] = value;
    }
}

void Array::insert(int index, int key)
{
    if (index >= 0 && index <= length)
    {
        for (int i = length - 1; i >= index; i--)
        {
            A[i + 1] = A[i];
        }
        A[index] = key;
        length++;
    }
    else
    {
        cout << "Entered index is not valid!" << endl;
    }
}

void Array::swap(int *x, int *y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

int Array::delete_element(int index)
{
    int value = 0;
    if (index >= 0 && index < length)
    {
        value = A[index];
        for (int i = index; i < length - 1; i++)
        {
            A[i] = A[i + 1];
        }
        A[length] = 0;
        length--;
        return value;
    }
    return 0;
}

int Array::LinearSearch(int value)
{
    for (int i = 0; i < length; i++)
    {
        if (value == A[i])
        {
            // swap(&A[i], &A[i - 1]);
            swap(&A[i], &A[0]);
            return i;
        }
    }
    return -1;
}

int Array::BinarySearch(int value)
{
    int left = 0;
    int right = length - 1;
    int mid;

    while (left <= right)
    {
        mid = (left + right) / 2;
        if (value == A[mid])
        {
            return mid;
        }
        else if (value < A[mid])
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return -1;
}

int Array::recursionBinarySearch(int a[], int left, int right, int value)
{
    int mid = 0;
    if (left <= right)
    {
        mid = (left + right) / 2;
        if (value == a[mid])
        {
            return mid;
        }
        else if (value < a[mid])
        {
            return recursionBinarySearch(a, left, mid - 1, value);
        }
        else
        {
            return recursionBinarySearch(a, mid + 1, right, value);
        }
    }
    return -1;
}

void Array::sortArray()
{
    int len = length - 1;
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < length - i - 1; j++)
        {
            if (A[j] > A[j + 1])
            {
                swap(&A[j], &A[j + 1]);
            }
        }
    }
}

int Array::get_value(int index)
{

    if (index >= 0 && index < length)
    {
        return A[index];
    }

    return -1;
}

void Array::set_value(int index, int value)
{
    if (index >= 0 && index <= length)
    {
        A[index] = value;
    }
    else
    {
        cout << "Given index to set value is invalid" << endl;
    }
}

int Array::max_value()
{
    int max = A[0];
    for (int i = 0; i < length; i++)
    {
        if (max < A[i])
        {
            max = A[i];
        }
    }
    return max;
}

int Array::min_value()
{
    int min = A[0];
    for (int i = 0; i < length; i++)
    {
        if (min > A[i])
        {
            min = A[i];
        }
    }
    return min;
}

int Array::sum_of_values()
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += A[i];
    }
    return sum;
}

float Array::avg_of_values()
{
    return (float)sum_of_values() / length;
}

bool Array::is_sorted()
{
    for (int i = 0; i < length - 1; i++)
    {
        if (A[i] > A[i + 1])
        {
            return false;
        }
    }
    return true;
}

void Array::reverse_array()
{
    int i = length - 1;
    int j = 0;
    int *B;
    B = (int *)malloc(length * sizeof(int));
    for (; i >= 0; i--, j++)
    {
        B[j] = A[i];
    }

    for (i = 0; i < length; i++)
    {
        A[i] = B[i];
    }

    free(B);
}

void Array::reverse_swap()
{
    int i = 0, j = length - 1;
    for (; i < j; i++, j--)
    {
        swap(&A[i], &A[j]);
    }
}

void Array::inserted_sorted_value(int value)
{
    if (length < size)
    {
        int i = length - 1;
        while (value < A[i])
        {
            A[i + 1] = A[i];
            i--;
        }
        A[i + 1] = value;
        length++;
    }
    else
    {
        cout << "Cannot insert a value as the array is already out of space" << endl;
    }
}

void Array::rearrange_array()
{
    int i = 0, j = length - 1;
    while (i < j)
    {
        while (A[i] < 0)
            i++;
        while (A[j] >= 0)
            j--;
        if (i < j)
            swap(&A[i], &A[j]);
    }
}

void Array::left_shift()
{
    for (int i = 0; i < length - 1; i++)
    {
        A[i] = A[i + 1];
    }
    A[length - 1] = 0;
}

void Array::left_rotate()
{
    int first = A[0];
    for (int i = 0; i < length - 1; i++)
    {
        A[i] = A[i + 1];
    }
    A[length - 1] = first;
}

void Array::right_shift()
{
    for (int i = length - 1; i > 0 - 1; i--)
    {
        A[i] = A[i - 1];
    }
    A[0] = 0;
}

void Array::right_rotate()
{
    int last_element = A[length - 1];
    for (int i = length - 1; i > 0; i--)
    {
        A[i] = A[i - 1];
    }
    A[0] = last_element;
}

Array *Array::merge_array(Array arr2)
{
    int i, j, k;
    i = j = k = 0;
    Array *arr3 = new Array(length + arr2.length);

    while (i < length && j < arr2.length)
    {
        if (A[i] < arr2.A[j])
            arr3->A[k++] = A[i++];
        else
            arr3->A[k++] = arr2.A[j++];
    }
    for (; i < length; i++)
    {
        arr3->A[k++] = A[i];
    }
    for (; j < arr2.length; j++)
    {
        arr3->A[k++] = arr2.A[j];
    }
    arr3->length = k;
    return arr3;
}

Array *Array::union_array(Array arr2)
{
    int i, j, k;
    i = j = k = 0;
    Array *arr3 = new Array(length + arr2.length);

    while (i < length && j < arr2.length)
    {
        if (A[i] < arr2.A[j])
        {
            arr3->A[k++] = A[i++];
        }
        else if (arr2.A[j] < A[i])
        {
            arr3->A[k++] = arr2.A[j++];
        }
        else
        {
            arr3->A[k++] = A[i++];
            j++;
        }
    }
    for (; i < length; i++)
    {
        arr3->A[k++] = A[i];
    }
    for (; j < arr2.length; j++)
    {
        arr3->A[k++] = arr2.A[j];
    }
    arr3->length = k;
    return arr3;
}

Array *Array::intersect_array(Array arr2)
{
    int i, j, k;
    i = j = k = 0;
    Array *arr3 = new Array(length + arr2.length);

    while (i < length && j < arr2.length)
    {
        if (A[i] < arr2.A[j])
            i++;
        else if (arr2.A[j] < A[i])
            j++;
        else
        {
            arr3->A[k++] = A[i++];
            j++;
        }
    }
    arr3->length = k;
    return arr3;
}

Array *Array::diff_array(Array arr2)
{
    int i, j, k;
    i = j = k = 0;

    Array *arr3 = new Array(length + arr2.length);

    while (i < length && j < arr2.length)
    {
        if (A[i] < arr2.A[j])
            arr3->A[k++] = A[i++];
        else if (arr2.A[j] < A[i])
            j++;
        else
        {
            i++;
            j++;
        }
    }

    for (; i < length; i++)
    {
        arr3->A[k++] = A[i];
    }

    arr3->length = k;
    return arr3;
}

int main()
{
    Array *arr;
    int choice, sz;
    int element, index;
    cout << "Enter the size of the array you want to create: " << endl;
    cin >> sz;
    arr = new Array(sz);
    do
    {
        cout << "--------------------------------------------------" << endl;
        cout << endl
             << "Menu: " << endl;
        cout << "1. Add an element" << endl;
        cout << "2. Insert an element" << endl;
        cout << "3. Delete an element" << endl;
        cout << "4. Linear search" << endl;
        cout << "5. Binary search" << endl;
        cout << "6. Recursive binary search" << endl;
        cout << "7. Sum of current elements" << endl;
        cout << "8. Average of current elements" << endl;
        cout << "9. Maximum element" << endl;
        cout << "10. Minimum element" << endl;
        cout << "11. Get value at index" << endl;
        cout << "12. Set value at index" << endl;
        cout << "13. Check if elements are sorted" << endl;
        cout << "14. Sort the array" << endl;
        cout << "15. Reverse the array (with extra space)" << endl;
        cout << "16. Reverse the array (in place using swap)" << endl;
        cout << "17. Insert in a sorted array" << endl;
        cout << "18. Rearrange array (positive and negative numbers)" << endl;
        cout << "19. Left shift array" << endl;
        cout << "20. Left rotate array" << endl;
        cout << "21. Right shift array" << endl;
        cout << "22. Right rotate array" << endl;
        cout << "23. Merge two arrays" << endl;
        cout << "24. Union of two arrays" << endl;
        cout << "25. Intersection of two arrays" << endl;
        cout << "26. Difference of two arrays" << endl;
        cout << "27. Display the array" << endl;
        cout << "28. Exit" << endl;
        cout << endl
             << "Enter your choice (number): " << endl;
        cin >> choice;

        switch (choice)
        {
        case 1:
            cout << "Enter the element:" << endl;
            cin >> element;
            arr->append(element);
            break;

        case 2:
            cout << "Enter index: ";
            cin >> index;
            cout << endl;
            cout << "Enter value: ";
            cin >> element;
            cout << endl;
            arr->insert(index, element);
            break;

        case 3:
            cout << "Enter index to delete an element: ";
            cin >> index;
            arr->delete_element(index);
            break;

        case 4:
            cout << "Enter the value to search: ";
            cin >> element;
            cout << "Index of the element: " << arr->LinearSearch(element) << endl;
            break;

        case 5:
            cout << "Enter the value to search: ";
            cin >> element;
            cout << "Index of the element: " << arr->BinarySearch(element) << endl;
            break;

        case 6:
            cout << "Enter the value to search: ";
            cin >> element;
            cout << "Index of the element: "
                 << arr->recursionBinarySearch(arr->get_Array(), 0, arr->get_length() - 1, element)
                 << endl;
            break;

        case 7:
            cout << "Sum of all values: " << arr->sum_of_values() << endl;
            break;

        case 8:
            cout << "Average of all values: " << arr->avg_of_values() << endl;
            break;

        case 9:
            cout << "Maximum value: " << arr->max_value() << endl;
            break;

        case 10:
            cout << "Minimum value: " << arr->min_value() << endl;
            break;

        case 11:
            cout << "Enter index: ";
            cin >> index;
            cout << "Value at index: " << arr->get_value(index) << endl;
            break;

        case 12:
            cout << "Enter index: ";
            cin >> index;
            cout << "Enter value: ";
            cin >> element;
            arr->set_value(index, element);
            break;

        case 13:
            if (arr->is_sorted())
                cout << "Array is sorted!" << endl;
            else
                cout << "Array is not sorted!" << endl;
            break;

        case 14:
            arr->sortArray();
            break;

        case 15:
            arr->reverse_array();
            break;

        case 16:
            arr->reverse_swap();
            break;

        case 17:
            cout << "Enter value to insert in sorted array: ";
            cin >> element;
            arr->inserted_sorted_value(element);
            break;

        case 18:
            arr->rearrange_array();
            cout << "Rearrangements of array -ve and +ve numbers results: " << endl;
            arr->display_array();
            break;

        case 19:
            arr->left_shift();
            cout << "Left shift results: " << endl;
            arr->display_array();
            break;

        case 20:
            arr->left_rotate();
            cout << "Left rotate results: " << endl;
            arr->display_array();
            break;

        case 21:
            arr->right_shift();
            cout << "Right Shift results: " << endl;
            arr->display_array();
            break;

        case 22:
            arr->right_rotate();
            cout << "Right rotate results: " << endl;
            arr->display_array();
            break;

        case 23:
        {
            Array arr2(sz);
            int l;
            cout << "Enter the number of elements you want in 2nd array(length): ";
            cin >> l;
            cout << "Enter elements for the second array: ";
            for (int i = 0; i < l; i++)
            {
                cin >> element;
                arr2.append(element);
            }
            Array *mergedArray = arr->merge_array(arr2);
            mergedArray->display_array();
            delete mergedArray;
            break;
        }

        case 24:
        {
            Array arr3(sz);
            int l;
            cout << "Enter the number of elements you want in 2nd array(length): ";
            cin >> l;
            cout << "Enter elements for the second array: ";
            for (int i = 0; i < l; i++)
            {
                cin >> element;
                arr3.append(element);
            }
            Array *unionArray = arr->union_array(arr3);
            unionArray->display_array();
            delete unionArray;
            break;
        }

        case 25:
        {
            Array arr4(sz);
            int l;
            cout << "Enter the number of elements you want in 2nd array(length): ";
            cin >> l;
            cout << "Enter elements for the second array: ";
            for (int i = 0; i < l; i++)
            {
                cin >> element;
                arr4.append(element);
            }
            Array *intersectionArray = arr->intersect_array(arr4);
            intersectionArray->display_array();
            delete intersectionArray;
            break;
        }

        case 26:
        {
            Array arr5(sz);
            int l;
            cout << "Enter the number of elements you want in 2nd array(length): ";
            cin >> l;
            cout << "Enter elements for the second array: ";
            for (int i = 0; i < l; i++)
            {
                cin >> element;
                arr5.append(element);
            }
            Array *differenceArray = arr->diff_array(arr5);
            differenceArray->display_array();
            delete differenceArray;
            break;
        }

        case 27:
            arr->display_array();
            break;

        default:
            break;
        }
    } while (choice < 28);

    return 0;
}
