#pragma once
#include "Dice.h"
class Player
{
private:
	Dice bones[5];
	int total, showTotal;
	int roll();
public:
	Player();
	int getTotal();
	void rollAgain();
};


