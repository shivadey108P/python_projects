//Fact.cpp
#include <iostream>
#include <stdio.h>
using namespace std;

int fact(int n){
    if (n<0){
        return 0;
    }
    
    if(n==0 || n==1){
        return 1;
    }
    else{
        return fact(n-1)*n;
    }
}

int iterate_fact(int n){
    if (n ==0)
    return 1;
    int f = 1;
    for (int i=1; i<=n ; i++){
        f *= i;
    }
    return f;
}

int main()
{
    int r=5;
    cout<<iterate_fact(r);
    return 0;
}
