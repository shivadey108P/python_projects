

#include <iostream>
using namespace std;

int get_length(char A[])
{
    int i = 0;
    for (; A[i] != '\0'; i++)
    {
    }
    return i;
}

void swap_char(char *a, char *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void change_cases(char *A)
{
    int i = get_length(A);
    for (int j = 0; j < i; j++)
    {
        if (A[j] >= 65 && A[j] <= 90)
        {
            A[j] += 32;
        }
        else if (A[j] >= 'a' && A[j] <= 122)
        {
            A[j] -= 32;
        }
    }
}

void word_count(char A[])
{
    int len = get_length(A);
    int count_word = 0;
    if (len <= 1 && A[0] == ' ' || A[0] == '\0')
    {
        count_word = -1;
    }
    else
    {
        for (int i = 0; i < len; i++)
        {

            if (A[i] == ' ' && A[i - 1] != ' ' && i != 0)
            {
                count_word++;
            }
        }
    }

    count_word += 1;

    if (count_word > 0)
    {
        cout << "Word count: " << count_word << endl;
    }
    else if (count_word == -1)
    {
        cout << "No word is given!" << endl;
    }
}

void count_vowels_and_consonants(char A[])
{
    int len = get_length(A);
    int count_vowel, count_consonant;
    count_vowel = 0;
    count_consonant = 0;
    for (int i = 0; i < len; i++)
    {
        if (A[i] == 'a' || A[i] == 'e' || A[i] == 'i' || A[i] == 'o' || A[i] == 'u' || A[i] == 'A' || A[i] == 'E' || A[i] == 'I' || A[i] == 'O' || A[i] == 'U')
        {
            count_vowel++;
        }
        else if ((A[i] >= 'A' && A[i] <= 'Z') || A[i] >= 'a' && A[i] <= 'z')
        {
            count_consonant++;
        }
    }
    cout << "Vowel Count = " << count_vowel << endl;
    cout << "Consonant Count = " << count_consonant << endl;
}

bool is_valid_username(char name[])
{
    int len = get_length(name);
    for (int i = 0; i < len; i++)
    {
        if (!(name[i] >= 65 && name[i] <= 90) && !(name[i] >= 97 && name[i] <= 122) && !(name[i] >= 48 && name[i] <= 57))
        {
            return false;
        }
    }
    return true;
}

void reverse_string_using_swap(char A[])
{
    int len = get_length(A);
    int i, j;
    i = 0;
    j = len - 1;
    for (; i < j; i++, j--)
    {
        swap_char(&A[i], &A[j]);
    }
}

void reverse_string(char A[])
{
    int len = get_length(A);
    char *B = (char *)malloc((len + 1) * sizeof(char));
    if (B == NULL)
    {
        cout << "Memory Allocation failed!" << endl;
        return;
    }
    int i, j;
    i = 0;
    j = len - 1;
    for (; j >= 0; j--, i++)
    {
        B[i] = A[j];
    }
    B[len] = '\0';
    cout << B << endl;
    free(B);
}

int main()
{
    char A[] = "python";
    int i = 0;
    cout << get_length(A) << endl;
    // change_cases(A);
    printf("%s\n", A);
    /*count_vowels_and_consonants(A);
    word_count(A);*/

    /*if (is_valid_username(A)) {
        cout << "Valid username" << endl;
    }
    else {
        cout << "Not a valid username" << endl;
    }*/

    reverse_string_using_swap(A);
    cout << A << endl;
    reverse_string(A);

    return 0;
}
