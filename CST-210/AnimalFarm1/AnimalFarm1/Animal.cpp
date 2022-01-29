#include "Animal.h"
#include <iostream>
using namespace std;

Animal::Animal()
{
}

Animal::Animal(string n, int w, string t)
{
	name = n;
	weight = w;
	type = t;
}

void Animal::eat()
{
}

void Animal::speak()
{
}

int Animal::getTopWeight()
{
	return 0;
}

void Animal::setWeight(int w)
{
	weight = w;
}

int Animal::getWeight()
{
	return weight;
}

string Animal::getName()
{
	return name;
}

string Animal::getType()
{
	return type;
}

