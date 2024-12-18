#include <iostream>
#include <stdio.h>
using namespace std;


int *F;

int fib(int n){
    if(n <= 1) return n;

    int t0 = 0, t1 = 1, sum = 0;
    for(int i=2; i<=n; i++){
        sum = t0+t1;
        t0 = t1;
        t1 = sum;
    }

    return sum;
}

int r_fib(int n){
    if (n<=1){
        return n;
    }
    
    return fib(n-2)+fib(n-1);
}


int m_fib(int n){
    if (n<=1){
        F[n] = n;
        return n;
    }
    else{
        if(F[n-2]==-1){
            F[n-2] = m_fib(n-2);
        }
        if(F[n-1]==-1){
            F[n-1] = m_fib(n-1);
        }
        F[n] = F[n-2] + F[n-1];
        return F[n];
    }
}


int main(){
    int r = 8;
    // F = new int[r];
    F = (int *)malloc(r*sizeof(int));

    for(int i=0; i<r; i++){
        F[i] = -1;
    }

    cout<<m_fib(r)<<endl;
    cout<<"Fibonacci Series: "<<endl;
    for(int i=0; i<=r;i++){
        cout<<F[i]<<endl;
    }

    // delete [] F;
    free(F);

    return 0;
}