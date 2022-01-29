#pragma once
#include "Animal.h"
class Chicken: public Animal
{
public:
	Chicken(string n, int w, string t);
	void eat();
	void speak();
	int getTopWeight();
};

