#pragma once
#include "Horse.h"
#include "Cow.h"
#include "Chicken.h"
#include <vector>
using namespace std;

class Barn
{
private:
	vector <Horse> Stalls;
	vector <Chicken> Coup;
	vector <Cow> Pen;

public:
	Barn();
	void feedingTime();
};

