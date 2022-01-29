#include "Horse.h"
#include <iostream>
using namespace std;

Horse::Horse(string n, int w, string t)
	:Animal(n,w,t)

{
}

void Horse::eat()
{
	cout << this -> getName() << " the " << this -> getType() << " weighs " << this -> getWeight() << " lbs." << endl;
	setWeight(getWeight() + 8);
	cout << this-> getName() << " is eating and now weighs " << this-> getWeight() << " lbs." << endl;
}

void Horse::speak()
{
	cout << "nehhhh" << endl;
}

int Horse::getTopWeight()
{
	return 2200;
}

