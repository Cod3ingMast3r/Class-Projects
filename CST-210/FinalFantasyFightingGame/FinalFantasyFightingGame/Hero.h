#pragma once
#include "Character.h"
class Hero: public Character
{
public:
	Hero(string index, string name, string major, int health, int damage, string specialAbility, int money);
	void getStats();
};

