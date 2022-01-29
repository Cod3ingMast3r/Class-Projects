#include "Cow.h"
#include <iostream>
using namespace std;

Cow::Cow(string n, int w, string t)
	:Animal(n, w, t)
{
}
void Cow::eat()
{
	cout << this->getName() << " the " << this->getType() << " weighs " << this->getWeight() << " lbs." << endl;
	setWeight(getWeight() + 7);
	cout << this->getName() << " is eating and now weighs " << this->getWeight() << " lbs." << endl;
}

void Cow::speak()
{
	cout << "moooo" << endl;
}

int Cow::getTopWeight()
{
	return 1500;
}