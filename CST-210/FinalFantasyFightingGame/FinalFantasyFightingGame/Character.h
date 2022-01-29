#pragma once
using namespace std;
#include <string>
#include <vector>
class Character
{
private:
	string index;
	string name;
	string major;
	int health;
	int damage;
	int currentHealth;
	string specialAbility;
	int money;
public:
	Character();
	Character(string i, string n, string maj, int h, int d, string sA, int mon);
	string getIndex();
	string getName();
	string getMajor();
	int getCurrentHealth();
	int getHealth();
	int getDamage();
	string getSpecialAbility();
	void useSpecialAblity(Character* badguy);
	int getMoney();
	void updateCurrentHealth(int addedHealth);
	void updateHealth(int addedHealth);
	void updateDamage(int addedDamage);
	void updateSpecialAbility(string newAbility);
	void updateMoney(int addedMoney);
	virtual void getStats();
	
};

