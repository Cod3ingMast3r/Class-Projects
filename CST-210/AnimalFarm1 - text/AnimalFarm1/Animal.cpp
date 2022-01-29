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
	weight += 5;
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

