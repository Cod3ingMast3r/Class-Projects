#pragma once
#include <iostream>
using namespace std;

class Dice
{
private:
	int sides;
public:
	Dice();
	int rollDice();
	int value();
};

