#include <iostream>
using namespace std;

struct Node
{
    int data;
    struct Node *next;
} *first = NULL;

void create(int A[], int n)
{
    struct Node *t, *last;
    int i;
    first = (struct Node *)malloc(sizeof(struct Node));
    first->data = A[0];
    first->next = NULL;
    last = first;

    for (i = 1; i < n; i++)
    {
        t = (struct Node *)malloc(sizeof(struct Node));
        t->data = A[i];
        t->next = NULL;
        last->next = t;
        last = t;
    }
}

void display(struct Node *p)
{
    while (p != NULL)
    {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl;
}

void display_recursive(struct Node *p)
{
    if (p != NULL)
    {
        cout << p->data << " ";
        display_recursive(p->next);
    }
}

void display_reverese(struct Node *p)
{
    if (p != NULL)
    {
        display_recursive(p->next);
        cout << p->data << " ";
    }
}

int count(struct Node *p)
{
    int c = 0;
    while (p != NULL)
    {
        c++;
        p = p->next;
    }
    return c;
}

int count_rec(struct Node *p)
{
    if (p == NULL)
        return 0;
    return count_rec(p->next) + 1;
}

int sum(struct Node *p)
{
    int s = 0;
    while (p)
    {
        s += p->data;
        p = p->next;
    }

    return s;
}

int sum_recursive(struct Node *p)
{
    /*if (!p)
    {
        return 0;
    }
    return sum_recursive(p->next) + p->data;*/

    return !p ? 0 : sum_recursive(p->next) + p->data;
}

int max(struct Node *p)
{
    int m = INT64_MIN;
    while (p)
    {
        if (p->data > m)
        {
            m = p->data;
        }
        p = p->next;
    }
    return m;
}

int max_recursive(struct Node *p)
{
    int x = 0;
    if (!p)
    {
        return INT64_MIN;
    }
    x = max_recursive(p->next);
    return x > p->data ? x : p->data;
}

struct Node *linear_search(struct Node *p, int key)
{
    while (p)
    {
        if (key == p->data)
            return p;
        p = p->next;
    }
    return NULL;
}
struct Node *recursive_search(struct Node *p, int key)
{
    if (!p)
    {
        return NULL;
    }
    if (key == p->data)
    {
        return p;
    }
    return recursive_search(p->next, key);
}

struct Node *improved_linear_search(struct Node *p, int key)
{
    struct Node *q = NULL;
    while (p)
    {
        if (key == p->data)
        {
            q->next = p->next;
            p->next = first;
            first = p;
            return p;
        }
        q = p;
        p = p->next;
    }
    return NULL;
}

void insert(struct Node *p, int pos, int value)
{
    if (pos < 0 || pos > count(p))
    {
        cout << "invalid position to insert the node at position: " << pos << endl;
        return;
    }
    struct Node *temp = (struct Node *)malloc(sizeof(struct Node));
    temp->data = value;
    if (pos == 0)
    {
        temp->next = first;
        first = temp;
    }
    else
    {
        for (int i = 0; i < pos - 1 && p; i++)
        {
            p = p->next;
        }
        temp->next = p->next;
        p->next = temp;
    }
}

int main()
{
    // struct Node* temp;
    /*int A[] = { 10, 20, 30 };
    create(A, 3);*/

    insert(first, 0, 1);
    insert(first, 1, 2);
    insert(first, 2, 3);
    insert(first, 3, 4);
    insert(first, 5, 5);

    display(first);

    return 0;
}