//Power
#include <iostream>
#include <stdio.h>
using namespace std;

int power(int m, int n){
    if (n== 0)
    return 1;
    return m*power(m,n-1);
}

int power1(int m, int n){
    if (n==0)
    return 1;
    
    if(n%2 ==0)
    return power1(m*m, n/2);
    else
    return m*power1(m*m, (n-1)/2);
}

int iterative_power(int m, int n){
    int p= 1;
    for (int i=1; i<=n; i++){
        p = p*m;
    }
    
    return p;
}


int main()
{
    int num=2, p=9;
    
    cout<<iterative_power(num,p);
    
    return 0;
}