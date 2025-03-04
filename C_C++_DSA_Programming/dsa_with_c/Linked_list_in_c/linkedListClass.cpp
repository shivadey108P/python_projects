#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

class LinkedList
{
private:
    Node *first;

public:
    LinkedList() { first = NULL; }
    LinkedList(int A[], int n);
    ~LinkedList();
    void display();
    void insert(int index, int value);
    int delete_node(int index);
    int length();
};

LinkedList::LinkedList(int A[], int n)
{
    Node *last, *temp;
    int i = 0;

    first = new Node;
    first->data = A[0];
    first->next = NULL;
    last = first;

    for (i = 1; i < n; i++)
    {
        temp = new Node;
        temp->data = A[i];
        temp->next = NULL;
        last->next = temp;
        last = temp;
    }
}

LinkedList::~LinkedList()
{
    Node *p = first;
    while (first)
    {
        first = first->next;
        delete p;
        p = first;
    }
}

void LinkedList::display()
{
    Node *p = first;
    while (p)
    {
        cout << p->data << " ";
        p = p->next;
    }
    cout << endl;
}

int LinkedList::length()
{
    Node *p = first;
    int count = 0;
    while (p)
    {
        count++;
        p = p->next;
    }

    return count;
}

void LinkedList::insert(int index, int value)
{
    if (index < 0 || index > length())
    {
        cout << "Invalid Index!" << endl;
        return;
    }
    Node *p = first, *temp;
    temp = new Node;
    temp->data = value;
    temp->next = NULL;

    if (index == 0)
    {
        temp->next = first;
        first = temp;
    }
    else
    {
        p = first;
        for (int i = 0; i < index - 1; i++)
        {
            p = p->next;
        }
        temp->next = p->next;
        p->next = temp;
    }
}

int LinkedList::delete_node(int index)
{
    if (index < 1 || index > length())
    {
        cout << "Invalid Index!" << endl;
        return -1;
    }
    Node *p = first, *q = NULL;
    int x = -1;
    if (index == 1)
    {
        first = first->next;
        x = p->data;
        delete p;
    }
    else
    {
        for (int i = 0; i < index - 1; i++)
        {
            q = p;
            p = p->next;
        }
        q->next = p->next;
        x = p->data;
        delete p;
    }
    return x;
}

int main()
{
    int A[] = {1, 2, 3, 4, 5};
    LinkedList l1(A, 5);
    l1.display();
}
