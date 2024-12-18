#include<iostream>
using namespace std;

/*
Pascal's Triangle:
                    1
                    /\
                   /  \ 
                  1    1
                 /\   /\
                /  \ /  \
               1    2    1
              / \  / \  / \
             /   \/   \/   \
            1    3     3    1

*/

int fact(int n){
    if(n==1) return 1;

    return fact(n-1)*n;
}

int combination(int n, int r){
    int t1,t2,t3;
    t1 = fact(n);
    t2 = fact(r);
    t3 = fact(n-r);
    return t1/(t2*t3);
}

int r_comb(int n, int r){
    if(r==0 || n==r) return 1;
    else{
        return r_comb(n-1,r-1) + r_comb(n-1,r); //Formula from Pascal's Triangle
    }
}

int main(){

    int n =5, r =3;

    cout<<n<<"C"<<r<<" = "<<r_comb(n,r);

    return 0;
}