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
	virtual void eat();
	virtual void speak();
	virtual int getTopWeight();
	void setWeight(int w);
	int getWeight();
	string getName();
	string getType();

};

