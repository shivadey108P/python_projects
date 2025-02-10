#include <iostream>
#include <string>

using namespace std;

struct Terms
{
    int coeff;
    int exp;
};

struct Poly
{
    int n;
    struct Terms *t;
};

void create(struct Poly *p)
{
    cout << "Enter Poly size: ";
    cin >> p->n;
    p->t = new Terms[p->n];
    cout << "Insert Terms (coeff exp):" << endl;
    for (int i = 0; i < p->n; i++)
    {
        cin >> p->t[i].coeff >> p->t[i].exp;
    }
}

// Function to convert exponent to superscript format
string toSuperscript(int num)
{
    string normal = "0123456789";
    string superscript = "⁰¹²³⁴⁵⁶⁷⁸⁹"; // Unicode superscript characters
    string result = "";

    string numStr = to_string(num);
    for (char c : numStr)
    {
        result += superscript[normal.find(c)];
    }

    return result;
}

void display(struct Poly p)
{
    for (int i = 0; i < p.n; i++)
    {
        if (i > 0)
            cout << " + ";

        cout << p.t[i].coeff;

        if (p.t[i].exp != 0)
        {
            cout << "x" << p.t[i].exp;
        }
    }
    cout << endl;
}

struct Poly *add(struct Poly *p1, struct Poly *p2)
{
    struct Poly *sum;
    int i, j, k;
    i = j = k = 0;
    sum = (struct Poly *)malloc(sizeof(struct Poly));

    if (!sum)
    {
        cout << "Memory allocation failed for sum" << endl;
        return nullptr;
    }

    sum->t = (struct Terms *)malloc((p1->n + p2->n) * sizeof(struct Terms));

    if (!sum->t)
    {
        cout << "Memory allocation failed for sum->t" << endl;
        return nullptr;
    }

    while (i < p1->n && j < p2->n)
    {
        if (p1->t[i].exp > p2->t[j].exp)
        {
            sum->t[k++] = p1->t[i++];
        }
        else if (p1->t[i].exp < p2->t[j].exp)
        {
            sum->t[k++] = p2->t[j++];
        }
        else
        {
            sum->t[k] = p1->t[i];
            sum->t[k++].coeff = p1->t[i++].coeff + p2->t[j++].coeff;
        }
    }
    for (; i < p1->n; i++)
    {
        sum->t[k++] = p1->t[i];
    }
    for (; j < p2->n; j++)
    {
        sum->t[k++] = p2->t[j];
    }

    sum->n = k;
    return sum;
}

int main()
{
    struct Poly p1, p2, *p3;
    create(&p1);
    create(&p2);
    p3 = add(&p1, &p2);

    display(p1);
    display(p2);
    display(*p3);

    delete[] p1.t;
    delete[] p2.t;
    delete p3;
    return 0;
}
