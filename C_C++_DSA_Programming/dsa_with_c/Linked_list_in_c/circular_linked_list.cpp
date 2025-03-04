#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

class CircularLinkedList
{
private:
    Node *head;
    void helper(Node *p);

public:
    CircularLinkedList(int A[], int n);
    ~CircularLinkedList();
    void display();
    void rec_display();
    void insert(int index, int value);
    int length();
};

CircularLinkedList::CircularLinkedList(int A[], int n)
{
    Node *last, *temp;
    int i;
    head = new Node;
    head->data = A[0];
    head->next = head;
    last = head;

    for (int i = 1; i < n; i++)
    {
        temp = new Node;
        temp->data = A[i];
        temp->next = last->next;
        last->next = temp;
        last = temp;
    }
}

CircularLinkedList::~CircularLinkedList()
{
    Node *p = head;
    do
    {
        head = head->next;
        delete p;
        p = head;
    } while (p != head);
}

void CircularLinkedList::display()
{
    Node *h = head;
    do
    {
        cout << h->data << " ";
        h = h->next;
    } while (h != head);
    cout << endl;
}

void CircularLinkedList::helper(Node *p)
{
    static int flag = 0;
    if (p != head || flag == 0)
    {
        flag = 1;
        cout << p->data << " ";
        helper(p->next);
    }
}

void CircularLinkedList::rec_display()
{
    if (head != nullptr)
        helper(head);
    cout << endl;
}

int CircularLinkedList::length()
{
    int count = 0;
    Node *p = head;
    if (head == NULL)
        return 0;
    else if (head->next == head)
    {
        return 1;
    }
    else
    {
        do
        {
            count++;
            p = p->next;
        } while (p != head);
        return count;
    }
}

void CircularLinkedList::insert(int index, int value)
{
    if (index < 0 || index > length())
    {
        cout << "Invalid Index!" << endl;
        return;
    }

    Node *p = head, *temp;
    temp = new Node;
    temp->data = value;
    temp->next = NULL;

    if (index == 0)
    {
        temp->next = head;
        while (p->next != head)
        {
            p = p->next;
        }
        p->next = temp;
        head = temp;
    }
    else
    {
        for (int i = 0; i < index - 1; i++)
        {
            p = p->next;
        }
        temp->next = p->next;
        p->next = temp;
    }
}

int main()
{
    int A[] = {1, 2, 3, 4, 5};
    CircularLinkedList c(A, 5);
    c.insert(0, 10);
    c.rec_display();
}
