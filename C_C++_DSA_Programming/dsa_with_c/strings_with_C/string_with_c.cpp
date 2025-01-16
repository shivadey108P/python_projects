

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

void lower_case(char *A)
{
    for (int i = 0; A[i] != '\0'; i++)
    {
        if (A[i] >= 'A' && A[i] <= 'Z')
        {
            A[i] += 32;
        }
    }
}

void upper_case(char *A)
{
    for (int i = 0; A[i] != '\0'; i++)
    {
        if (A[i] >= 'a' && A[i] <= 'z')
        {
            A[i] -= 32;
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

char *reverse_string(char A[])
{
    int len = get_length(A);
    char *B = (char *)malloc((len + 1) * sizeof(char));
    if (B == NULL)
    {
        cout << "Memory Allocation failed!" << endl;
        return NULL;
    }
    int i, j;
    i = 0;
    j = len - 1;
    for (; j >= 0; j--, i++)
    {
        B[i] = A[j];
    }
    B[len] = '\0';
    return B;
}

void compare_two_strings(char A[], char B[])
{
    int i = 0, j = 0;
    for (; A[i] != '\0' && B[j] != '\0'; i++, j++)
    {
        if (A[i] != B[j])
        {
            break;
        }
    }
    if (A[i] == B[j])
    {
        cout << "Both are Equal" << endl;
    }
    else if (A[i] > B[j])
    {
        cout << A << " is grater than " << B << endl;
    }
    else
    {
        cout << A << " is less than " << B << endl;
    }
}

bool is_compare(char A[], char B[])
{
    int i = 0, j = 0;
    for (; A[i] != '\0' && B[j] != '\0'; i++, j++)
    {
        if (A[i] != B[j])
        {
            break;
        }
    }
    if (A[i] == B[j])
    {
        return true;
    }
    else
    {
        return false;
    }
}

void find_palindrome(char A[])
{
    int len = get_length(A);
    int i, j;
    i = 0;
    j = len - 1;
    bool is_palindrome = true;
    for (; i < j; i++, j--)
    {
        if (A[i] != A[j])
        {
            is_palindrome = false;
        }
    }
    if (is_palindrome)
    {
        cout << A << " is palindrome" << endl;
    }
    else
    {
        cout << A << " is not palindrome" << endl;
    }
}

void find_palindrome_ineffective_method(char A[])
{
    int len = get_length(A);
    char *B;
    B = (char *)malloc((len + 1) * sizeof(char));
    if (B == NULL)
    {
        cout << "Memory allocation failed!" << endl;
        return;
    }
    B = reverse_string(A);
    if (is_compare(A, B))
    {
        cout << "is palindrome" << endl;
    }
    else
    {
        cout << "not palindrome" << endl;
    }
    free(B);
}

void duplicates_compare(char A[])
{
    int i, j, count;
    int len = get_length(A);
    for (i = 0; i < len; i++)
    {
        count = 1;
        if (A[i] != 0)
        {
            for (j = i + 1; j < len; j++)
            {
                if (A[i] == A[j])
                {
                    A[j] = 0;
                    count++;
                }
            }
            cout << A[i] << " has appeared " << count << " times!" << endl;
        }
    }
}

void duplicates_using_hash(char A[])
{
    int *hash;
    hash = new int[26]{0};
    lower_case(A);
    for (int i = 0; A[i] != '\0'; i++)
    {
        if (A[i] >= 'a' && A[i] <= 'z')
            hash[A[i] - 'a']++;
    }
    for (int j = 0; j < 26; j++)
    {
        if (hash[j] >= 1)
        {
            cout << (char)(j + 'a') << " has appeared " << hash[j] << " times!" << endl;
        }
    }
    delete[] hash;
}

void duplicates_using_bitwise(char A[])
{
    int H = 0, x = 0, count = 0;
    lower_case(A);
    for (int i = 0; A[i] != '\0'; i++)
    {
        x = 1;
        x = x << (A[i] - 97);
        if ((x & H))
        {
            cout << A[i] << " is duplicated" << endl;
            count++;
        }
        else
        {
            H = x | H;
        }
    }
    if (count == 0)
    {
        cout << "There are no duplicates!" << endl;
    }
}

void find_anagram(char A[], char B[])
{
    lower_case(A);
    lower_case(B);
    int len_a = get_length(A);
    int len_b = get_length(B);
    int hash[26] = {0}, i = 0;

    if (len_a == len_b)
    {
        for (i = 0; i < len_a; i++)
        {
            hash[A[i] - 'a']++;
        }
        for (i = 0; i < len_b; i++)
        {
            hash[B[i] - 'a']--;
            if (hash[B[i] - 'a'] < 0)
            {
                cout << "They are not Anagram!" << endl;
                break;
            }
        }
        if (B[i] == '\0')
        {
            cout << "They are Anagram!" << endl;
        }
    }
    else
    {
        cout << "They are not Anagrams!" << endl;
    }
}

void find_anagram_ineffective_method(char A[], char B[])
{
    int len_a = get_length(A);
    int len_b = get_length(B);
    int i, j;
    bool search_result = false;

    if (len_a == len_b)
    {
        lower_case(A);
        lower_case(B);
        for (i = 0; i < len_a; i++)
        {

            for (j = 0; j < len_a; j++)
            {
                search_result = false;
                if (A[i] == B[j])
                {
                    search_result = true;
                    B[j] = -1;
                    break;
                }
            }
            if (!search_result)
            {
                cout << "They are not anagram!" << endl;
                return;
            }
        }

        cout << "They are anagram!" << endl;
    }
    else
    {
        cout << "They are not anagram!" << endl;
    }
}

void perm(char S[], int k)
{
    static int A[10] = {0};
    static char Res[10];
    int i;

    if (S[k] == '\0')
    {
        Res[k] = '\0';
        cout << Res << endl;
    }
    else
    {
        for (i = 0; S[i] != '\0'; i++)
        {
            if (A[i] == 0)
            {
                Res[k] = S[i];
                A[i] = 1;
                perm(S, k + 1);
                A[i] = 0;
            }
        }
    }
}

void perm_swap(char s[], int l, int h)
{
    int i;
    if (l == h)
    {
        cout << s << endl;
    }
    else
    {
        for (int i = l; i <= h; i++)
        {
            swap_char(&s[l], &s[i]);
            perm_swap(s, l + 1, h);
            swap_char(&s[l], &s[i]);
        }
    }
}

int main()
{
    // char A[] = "findings";
    // char B[] = "Painting";
    /*   int i = 0;
    cout << get_length(A) << endl;*/
    // change_cases(A);
    // printf("%s\n", A);
    /*count_vowels_and_consonants(A);
    word_count(A);*/

    /*if (is_valid_username(A)) {
        cout << "Valid username" << endl;
    }
    else {
        cout << "Not a valid username" << endl;
    }*/

    // reverse_string_using_swap(A);
    // cout << A << endl;
    // reverse_string(A);
    // compare_two_strings(A, B);
    // find_palindrome_ineffective_method(A);
    // duplicates_using_hash(A);
    // duplicates_using_bitwise(A);

    /*char A[] = "verbose";
    char B[] = "observe";
    find_anagram_ineffective_method(A, B);*/

    char S[] = "ABC";
    // int k = 0;
    // perm(S, k);
    perm_swap(S, 0, 2);
    return 0;
}
