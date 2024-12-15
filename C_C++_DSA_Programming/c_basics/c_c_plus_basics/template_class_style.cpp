#include<iostream>
#include<stdio.h>
using namespace std;

template<class T>
class Arithmetic{
    private:
    T num1, num2;

    public:
    Arithmetic();
    Arithmetic(T a,T b);
    T add();
    T subtract();
    T multiply();
    T divide();
};

template<class T>
Arithmetic<T>::Arithmetic(){
    num1 = 0;
    num2 = 0;
}

template<class T>
Arithmetic<T>::Arithmetic(T a, T b){
    num1 = a;
    num2 = b;
}

template<class T>
T Arithmetic<T>::add(){
    return num1+num2;
}

template<class T>
T Arithmetic<T>::subtract(){
    return num1-num2;
}

template<class T>
T Arithmetic<T>::multiply(){
    return num1*num2;
}

template<class T>
T Arithmetic<T>::divide(){
    return num1/num2;
}

int main(){
    float n1,n2;
    cout<<"Enter first number: ";
    cin>>n1;
    cout<<"Enter second number: ";
    cin>>n2;
    Arithmetic<float> ar(n1,n2);
    cout<<"Addition: "<<ar.add()<<endl;
    cout<<"Subtraction: "<<ar.subtract()<<endl;
    cout<<"Multiplication: "<<ar.multiply()<<endl;
    cout<<"Division: "<<ar.divide()<<endl;
    return 0;
}