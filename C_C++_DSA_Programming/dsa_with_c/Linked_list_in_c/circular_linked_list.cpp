#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node *next;
};

class CircularLinkedList {
private:
    Node* head;
public:
    CircularLinkedList(int A[], int n);
    ~CircularLinkedList();
    void display();
    void rec_display();
};

CircularLinkedList::CircularLinkedList(int A[], int n)
{
    Node* last, * temp;
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
    Node* p = head;
    do
    {
        head = head->next;
        delete p;
        p = head;
    } while (p != head);
}

void CircularLinkedList::display()
{
    Node* h = head;
    do {
        cout << h->data << " ";
        h = h->next;
    } while (h != head);
    cout << endl;
}

void CircularLinkedList::rec_display()
{
    static int flag = 0;
    Node *h = head;
    if(h != head && flag ==1)
    {
        
    }
}

int main()
{
    int A[] = { 1,2,3,4,5 };
    CircularLinkedList c(A, 5);
    c.display();
}

