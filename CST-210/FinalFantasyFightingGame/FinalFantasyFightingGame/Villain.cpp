#include "Villain.h"
#include <iostream>
using namespace std;

Villain::Villain(string i, string n, string maj, int h, int d, string sA, int mon)
	:Character(i, n, maj, h, d, sA, mon)
{
}

void Villain::getStats()
{
	cout << "Villan " << getName() << "'s stats are..." << endl;
	cout << "	Health: " << getHealth() << endl;
	cout << "	Damage: " << getDamage() << endl;
	cout << "Money if you beat them is: " << getMoney() << endl;
}
