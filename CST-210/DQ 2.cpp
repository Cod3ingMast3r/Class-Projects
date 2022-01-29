#include <iostream>
#include <vector>
using namespace std;

void vall(vector<int> x){
x.push_back(9);
for(int i = 0; i < x.size(); i++){
cout << x[i] << " ";
}
cout << "Same vector being passed in by Value \n";
}

void reff(vector<int> &x){
x.push_back(9);
for(int i = 0; i < x.size(); i++){
cout << x[i] << " ";
}
cout << "copying vector location reference \n";
}

int main() {
vector <int> myVector = {0,1,2,3};
vall(myVector); //vall
vall(myVector);//vall

reff(myVector);//reff
reff(myVector);//reff
}