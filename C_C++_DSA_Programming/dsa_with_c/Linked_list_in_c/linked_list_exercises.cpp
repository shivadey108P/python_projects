#include <iostream>
using namespace std;

struct Node
{
	int data;
	struct Node *next;
} *first = NULL, *second = NULL, *third = NULL;

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

void create2(int A[], int n)
{
	struct Node *t, *last;
	int i;
	second = (struct Node *)malloc(sizeof(struct Node));
	second->data = A[0];
	second->next = NULL;
	last = second;

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
			if (q != NULL)
			{
				q->next = p->next;
			}
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

void SortedInsert(struct Node *p, int value)
{
	struct Node *temp, *q = NULL;
	temp = (struct Node *)malloc(sizeof(struct Node));
	temp->data = value;
	temp->next = NULL;
	if (first == NULL)
	{
		first = temp;
	}
	else
	{
		while (p && p->data < value)
		{
			q = p;
			p = p->next;
		}
		if (p == first)
		{
			temp->next = first;
			first = temp;
		}
		else
		{
			temp->next = q->next;
			q->next = temp;
		}
	}
}

int deleteNode(struct Node *p, int index)
{
	int x = INT64_MIN, i;
	struct Node *q = NULL;
	if (index < 1 || index > count(p))
	{
		cout << "Please enter a valid index to delete a node." << endl;
		return x;
	}
	if (index == 1)
	{
		x = first->data;
		q = first;
		first = first->next;
		free(q);
		return x;
	}
	else
	{
		for (i = 0; i < index - 1; i++)
		{
			q = p;
			p = p->next;
		}
		q->next = p->next;
		x = p->data;
		free(p);
		return x;
	}
}

bool isSortedNode(struct Node *p)
{
	int x = -1;
	while (p)
	{
		if (p->data < x)
		{
			return false;
		}
		x = p->data;
		p = p->next;
	}
	return true;
}

void removeDuplicates(struct Node *p)
{
	if (isSortedNode(p))
	{
		struct Node *q = p->next;
		while (q != NULL)
		{
			if (p->data != q->data)
			{
				p = q;
				q = q->next;
			}
			else
			{
				p->next = q->next;
				free(q);
				q = p->next;
			}
		}
	}
	else
	{
		cout << "Node is not sorted! Cannot remove duplicates now!" << endl;
	}
}

void reverse_ll_using_data(struct Node *p)
{
	int length = count(p);
	int *A = (int *)malloc(sizeof(int) * length);
	struct Node *q = p;
	int i = 0;
	while (q)
	{
		A[i] = q->data;
		q = q->next;
		i++;
	}
	q = p;
	i--;
	while (q)
	{
		q->data = A[i];
		q = q->next;
		i--;
	}
}

void reverse_ll_using_node(struct Node *p)
{
	struct Node *q = NULL, *r = NULL;
	while (p)
	{
		r = q;
		q = p;
		p = p->next;
		q->next = r;
	}
	first = q;
}

void reverse_ll_using_node_recursion(struct Node *p, struct Node *q)
{
	if (p)
	{
		reverse_ll_using_node_recursion(p->next, p);
		p->next = q;
	}
	else
	{
		first = q;
	}
}

void concat(struct Node *p, struct Node *q)
{
	third = p;
	while (p->next != NULL)
	{
		p = p->next;
	}
	p->next = q;
}

void merge(struct Node *p, struct Node *q)
{
	struct Node *last = NULL;
	if (p->data < q->data)
	{
		third = last = p;
		p = p->next;
		third->next = NULL;
	}
	else
	{
		third = last = q;
		q = q->next;
		third->next = NULL;
	}

	while (p && q)
	{
		if (p->data < q->data)
		{
			last->next = p;
			last = p;
			p = p->next;
			last->next = NULL;
		}
		else
		{
			last->next = q;
			last = q;
			q = q->next;
			last->next = NULL;
		}

		if (p)
			last->next = p;
		if (q)
			last->next = q;
	}
}

bool isLoop(struct Node *f)
{
	struct Node *q, *p;
	p = q = f;
	do
	{
		p = p->next;
		q = q->next;
		q = q != NULL ? q->next : q;
	} while (p && q && p != q);
	return p == q ? true : false;
}

int main()
{
	struct Node *t1, *t2;
	int A[] = {10, 20, 30, 40, 50};
	int B[] = {5, 15, 25, 35, 45};

	create(A, 5);

	// t1 = first->next->next;
	// t2 = first->next->next->next->next;
	// t2->next = t1;

	if (isLoop(first))
	{
		cout << "The linked list is in loop" << endl;
	}
	else
	{
		cout << "It's not in loop" << endl;
	}

	return 0;
}