#pragma once
#include "Horse.h"
#include "Cow.h"
#include "Chicken.h"
#include <vector>
using namespace std;

class Barn
{
private:
	vector <Animal*> barn;


public:
	Barn();
	void feedingTime();
};

