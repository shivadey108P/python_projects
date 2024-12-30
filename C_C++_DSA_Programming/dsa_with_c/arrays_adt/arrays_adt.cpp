#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

struct Array
{
    int A[10];
    int size;
    int length;
};

void display_array(struct Array arr)
{
    for (int i = 0; i < arr.length; i++)
    {
        cout << arr.A[i] << " ";
    }
    cout << endl;
}

void append(struct Array *arr, int value)
{
    if (arr->length < arr->size)
    {
        arr->A[arr->length++] = value;
    }
}

void insert(struct Array *arr, int index, int key)
{
    if (index >= 0 && index <= arr->length)
    {
        for (int i = arr->length; i >= index; i--)
        {
            arr->A[i] = arr->A[i + 1];
        }
        arr->A[index] = key;
        arr->length++;
    }
}

void swap(int *x, int *y)
{
    int temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

int delete_element(struct Array *arr, int index)
{
    int value = 0;
    if (index >= 0 && index < arr->length)
    {
        value = arr->A[index];
        for (int i = index; i < arr->length - 1; i++)
        {
            arr->A[i] = arr->A[i + 1];
        }
        arr->A[arr->length] = 0;
        arr->length--;
        return value;
    }
    return 0;
}

int LinearSearch(struct Array *arr, int value)
{
    for (int i = 0; i < arr->length; i++)
    {
        if (value == arr->A[i])
        {
            // swap(&arr->A[i], &arr->A[i - 1]);
            swap(&arr->A[i], &arr->A[0]);
            return i;
        }
    }
    return -1;
}

int BinarySearch(struct Array arr, int value)
{
    int left = 0;
    int right = arr.length - 1;
    int mid;

    while (left <= right)
    {
        mid = (left + right) / 2;
        if (value == arr.A[mid])
        {
            return mid;
        }
        else if (value < arr.A[mid])
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

int recursionBinarySearch(int a[], int left, int right, int value)
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

void sortArray(struct Array *arr)
{
    int len = arr->length - 1;
    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j < arr->length - i - 1; j++)
        {
            if (arr->A[j] > arr->A[j + 1])
            {
                swap(&arr->A[j], &arr->A[j + 1]);
            }
        }
    }
}

int get_value(struct Array arr, int index)
{

    if (index >= 0 && index < arr.length)
    {
        return arr.A[index];
    }

    return -1;
}

void set_value(struct Array *arr, int index, int value)
{
    if (index >= 0 && index <= arr->length)
    {
        arr->A[index] = value;
    }
    else
    {
        cout << "Given index to set value is invalid" << endl;
    }
}

int max_value(struct Array arr)
{
    int max = arr.A[0];
    for (int i = 0; i < arr.length; i++)
    {
        if (max < arr.A[i])
        {
            max = arr.A[i];
        }
    }
    return max;
}

int min_value(struct Array arr)
{
    int min = arr.A[0];
    for (int i = 0; i < arr.length; i++)
    {
        if (min > arr.A[i])
        {
            min = arr.A[i];
        }
    }
    return min;
}

int sum_of_values(struct Array arr)
{
    int sum = 0;
    for (int i = 0; i < arr.length; i++)
    {
        sum += arr.A[i];
    }
    return sum;
}

float avg_of_values(struct Array arr)
{
    return (float)sum_of_values(arr) / arr.length;
}

bool is_sorted(struct Array arr)
{
    for (int i = 0; i < arr.length - 1; i++)
    {
        if (arr.A[i] > arr.A[i + 1])
        {
            return false;
        }
    }
    return true;
}

void reverse_array(struct Array *arr)
{
    int i = arr->length - 1;
    int j = 0;
    int *B;
    B = (int *)malloc(arr->length * sizeof(int));
    for (; i >= 0; i--, j++)
    {
        B[j] = arr->A[i];
    }

    for (i = 0; i < arr->length; i++)
    {
        arr->A[i] = B[i];
    }

    free(B);
}

void reverse_swap(struct Array *arr)
{
    int i = 0, j = arr->length - 1;
    for (; i < j; i++, j--)
    {
        swap(&arr->A[i], &arr->A[j]);
    }
}

void inserted_sorted_value(struct Array *arr, int value)
{
    if (arr->length < arr->size)
    {
        int i = arr->length - 1;
        while (value < arr->A[i])
        {
            arr->A[i + 1] = arr->A[i];
            i--;
        }
        arr->A[i + 1] = value;
        arr->length++;
    }
    else
    {
        cout << "Cannot insert a value as the array is already out of space" << endl;
    }
}

void rearrange_array(struct Array *arr)
{
    int i = 0, j = arr->length - 1;
    while (i < j)
    {
        while (arr->A[i] < 0)
            i++;
        while (arr->A[j] >= 0)
            j--;
        if (i < j)
            swap(&arr->A[i], &arr->A[j]);
    }
}

void left_shift(struct Array *arr)
{
    for (int i = 0; i < arr->length - 1; i++)
    {
        arr->A[i] = arr->A[i + 1];
    }
    arr->A[arr->length - 1] = 0;
}

void left_rotate(struct Array *arr)
{
    int first = arr->A[0];
    for (int i = 0; i < arr->length - 1; i++)
    {
        arr->A[i] = arr->A[i + 1];
    }
    arr->A[arr->length - 1] = first;
}

void right_shift(struct Array *arr)
{
    for (int i = arr->length - 1; i > 0 - 1; i--)
    {
        arr->A[i] = arr->A[i - 1];
    }
    arr->A[0] = 0;
}

void right_rotate(struct Array *arr)
{
    int last_element = arr->A[arr->length - 1];
    for (int i = arr->length - 1; i > 0; i--)
    {
        arr->A[i] = arr->A[i - 1];
    }
    arr->A[0] = last_element;
}

int main()
{
    /*struct Array arr;
    cout << "Enter the size of the array : ";
    cin>>arr.size;

    arr.A = (int*)malloc(arr.size * sizeof(int));

    cout << "Enter the length of array to display: ";
    cin >> arr.length;
    cout << endl << "Enter the elements for the array below: " << endl;
    for (int i = 0; i < arr.length; i++) {
        cin >> arr.A[i];
    }*/

    // free(arr.A);

    // struct Array arr = { {8,7,3,15,5,4,17,16,2}, 10, 9 };
    struct Array arr = {{1, 2, 3, 4, 5}, 10, 5};
    // append(&arr, 6);
    // insert(&arr, 3, 10);
    // int delete_index = 1;
    // cout << "Deleted value at index " << delete_index << " is " << delete_element(&arr,delete_index) << endl;
    // cout << LinearSearch(&arr, 15) << endl;
    /*display_array(arr);
    sortArray(&arr);
    display_array(arr);
    cout << BinarySearch(arr, 8) << endl;
    cout << recursionBinarySearch(arr.A, 0, arr.length-1, 8) << endl;*/

    // cout << get_value(arr, 5) << endl;;
    // set_value(&arr, 3, 20);
    // cout << max_value(arr) << endl;
    // cout << min_value(arr) << endl;
    // cout << sum_of_values(arr) << endl;
    // cout << avg_of_values(arr) << endl;
    // printf("%f \n", avg_of_values(arr));

    // printf("%s \n", is_sorted(arr)? "true":"false");
    // reverse_swap(&arr);
    // inserted_sorted_value(&arr, 4);
    // rearrange_array(&arr);
    // display_array(arr);
    // left_rotate(&arr);
    // left_rotate(&arr);
    // left_rotate(&arr);

    display_array(arr);
    right_rotate(&arr);
    right_rotate(&arr);
    right_rotate(&arr);
    display_array(arr);

    return 0;
}
