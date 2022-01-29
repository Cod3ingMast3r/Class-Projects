#include "Player.h"

int totalRolls = 0;

int Player::roll()
{
	int total = 0;
	if (totalRolls == 0) {
		cout << "First Roll:" << endl;
		for (int i = 0; i < 5; i++) {
			bones[i].rollDice();
		}
		totalRolls = totalRolls + 1;

	}
	else{
		cout << "Re roll " << totalRolls << ":" << endl;
		totalRolls = totalRolls + 1;
	}

	for (int i = 0; i < 5; i++) {
		if (i != 4) {
			cout << "Dice " << i+1 << ": " << bones[i].value() << ", ";
		}
		else {
			cout << "Dice " << i+1 << ": " << bones[i].value() << endl;
		}
		total += bones[i].value();
	}
	cout << "Total: " << total << endl;

	return total;
}

Player::Player()
{
	total = 0;
	showTotal = 0;
}

int Player::getTotal()
{	
	if (totalRolls >= 3)
	{
		cout << endl <<"Your final dice are shown below:" << endl;
		showTotal = roll();
		return showTotal;
	}
	showTotal = roll();
	rollAgain();
	return showTotal;
}

void Player::rollAgain()
{
	int again;

	int diceNumber;
	cout << " How many dice do you want to re roll? ";
	cin >> again;

	for (int i = 0; i < again; i++)
	{
		cout << "Which dice do you want to re roll? ";
		cin >> diceNumber;
		bones[diceNumber-1].rollDice();
	}
	if (again == 0) {
		totalRolls = 3;
	}
	getTotal();
}


