#include "Hero.h"
#include <iostream>
using namespace std;

Hero::Hero(string i, string n, string maj, int h, int d, string sA, int mon)
	:Character(i, n, maj, h, d, sA, mon)
{
}

void Hero::getStats()
{
	cout << "Your Hero " << getMajor() << " major " << getName() << "'s stats are..." << endl;
	cout << "     Health: " << getHealth() << endl;
	cout << "     Damage: " << getDamage() << endl;
	cout << "     Special Ability: " << getSpecialAbility() << endl;
	cout << "Your Current Money status is: " << getMoney() << endl;
}


