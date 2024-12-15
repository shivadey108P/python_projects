#include <iostream>
#include <stdio.h>
using namespace std;

class Rectangle{
    private:
    int length;
    int breadth;

    public:
    Rectangle(){
        length = 0;
        breadth = 0;
    }

    Rectangle(int length, int breadth){
        this->length = length;
        this->breadth = breadth;
    }

    int area(){
        return length*breadth;
    }

    int perimeter(){
        return 2*(length+breadth);
    }

    int getLength(){
        return length;
    }

    int getBreadth(){
        return breadth;
    }

    void setLength(int l){
        length = l;
    }

    void setBreadth(int b){
        breadth = b;
    }

};

int main(){
    int l,b;
    cout<<"Enter Length: ";
    cin>>l;
    cout<<"Enter Breadth: ";
    cin>>b;
    Rectangle r(l,b);
    cout<<"length: "<<r.getLength()<<endl;
    cout<<"breadth: "<<r.getBreadth()<<endl;
    cout<<"Area: "<<r.area()<<endl;
    cout<<"Perimeter: "<<r.perimeter()<<endl;

    cout<<"Enter new length: ";
    cin>>l;
    r.setLength(l);
    cout<<"set new length: "<<r.getLength()<<endl;
    cout<<"Area: "<<r.area()<<endl;
    cout<<"Perimeter: "<<r.perimeter()<<endl;
    return 0;
}