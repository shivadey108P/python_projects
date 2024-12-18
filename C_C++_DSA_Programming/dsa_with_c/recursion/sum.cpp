//sum.cpp
#include <iostream>
#include <stdio.h>
using namespace std;

int sum_rec(int n){
    if(n == 0){
        return 0;
    }
    return sum_rec(n-1)+n;
}

int sum(int n){
    return (n*(n+1))/2;
}

int iterate_sum(int n){
    int s=0;
    for(int i=0; i<=n ; i++){
        s += i;
    }
    return s;
}

int main()
{
    int r= 20;
    
    cout<<sum(r)<<endl;
    
    return 0;
}
