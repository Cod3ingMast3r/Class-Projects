#pragma once
#include "Character.h"
class Villain : public Character
{
public:
	Villain(string index, string name, string major, int health, int damage, string specialAbility, int money);
	void getStats();
};

