#include "Character.h"
#include <iostream>
using namespace std;

Character::Character()
{
}

Character::Character(string i, string n, string maj, int h, int d, string sA, int mon)
{
	index = i;
	name = n;
	major = maj;
	currentHealth = h;
	health = h;
	damage = d;
	specialAbility = sA;
	money = mon;
}


string Character::getIndex()
{
	return index;
}

string Character::getName()
{
	return name;
}

string Character::getMajor()
{
	return major;
}

int Character::getCurrentHealth()
{
	return currentHealth;
}

int Character::getHealth()
{
	return health;
}

int Character::getDamage()
{
	return damage;
}

string Character::getSpecialAbility()
{
	return specialAbility;
}

void Character::useSpecialAblity(Character* badguy)
{
	int randomNum = rand() % 100 + 1;
	if (getSpecialAbility() == "None")
	{
		cout << endl << "That was a stupd Choice, You have no Ability" << endl;
	}

	if (getSpecialAbility() == "Prove teacher wrong (Double Damage (25% Chance))")
	{
		if (randomNum <=25)
		{
			badguy->updateCurrentHealth(-(getDamage())*2);
			cout << endl << "You did " << getDamage()*2 << " Damage to " << badguy->getName() << "'s health leaving them with " << badguy->getCurrentHealth() << " remaining." << endl;
		}
		else
		{
			cout << endl << "Sorry but the odds were not in your favor, maybe next time" << endl;
		}

	}

	if (getSpecialAbility() == "Take Aderoll (Restore to Max Health (34% Chance))")
	{
		if (randomNum <= 34)
		{
			updateHealth(0);
			cout << endl << "Nice Job, you healed back to a max health of " << getCurrentHealth() << endl;

		}
		else
		{
			cout << endl << "Sorry but the odds were not in your favor, maybe next time" << endl;
		}

	}

	if (getSpecialAbility() == "Pay for someone to do Your Hw (Kill instantlly (5% Chance))")
	{
		if (randomNum <= 5)
		{
			int instakill = badguy->getCurrentHealth();
			badguy->updateCurrentHealth(-instakill);
			cout << endl << "Wow, cheating works sometimes IG, goodluck." << endl;

		}
		else
		{
			cout << endl << "Sorry but the odds were not in your favor, maybe next time" << endl;
		}

	}

}

int Character::getMoney()
{
	return money;
}

void Character::updateCurrentHealth(int addedHealth)
{
	currentHealth = currentHealth + addedHealth;
	if (currentHealth < 0)
	{
		currentHealth = 0;
	}
}

void Character::updateHealth(int addedHealth)
{
	health = health + addedHealth;
	currentHealth = health;
}

void Character::updateDamage(int addedDamage)
{
	damage = damage + addedDamage;
}

void Character::updateSpecialAbility(string newAblility)
{
	specialAbility = newAblility;
}

void Character::updateMoney(int addedMoney)
{
	money = money + addedMoney;
}

void Character::getStats()
{
}







