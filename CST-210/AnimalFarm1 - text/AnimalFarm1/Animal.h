#pragma once
using namespace std;
#include <string>

class Animal
{
private:
	string name;
	int weight;
	string type;
public:
	Animal();
	Animal(string n, int w, string t);
	void eat();
	int getWeight();
	string getName();
	string getType();

};

