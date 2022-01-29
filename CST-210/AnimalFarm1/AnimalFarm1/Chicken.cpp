#include "Chicken.h"
#include <iostream>
using namespace std;

Chicken::Chicken(string n, int w, string t)
	:Animal(n, w, t)
{
}
void Chicken::eat()
{
	cout << this->getName() << " the " << this->getType() << " weighs " << this->getWeight() << " lbs." << endl;
	setWeight(getWeight() + 1);
	cout << this->getName() << " is eating and now weighs " << this->getWeight() << " lbs." << endl;
}

void Chicken::speak()
{
	cout << "cluk cluk" << endl;
}

int Chicken::getTopWeight()
{
	return 12;
}