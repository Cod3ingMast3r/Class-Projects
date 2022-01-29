#include "Dice.h"

Dice::Dice()
{
	sides = 0;
}

int Dice::rollDice()
{
	sides = rand() % 6 + 1;
	return sides;
}

int Dice::value()
{
	return sides;
}
