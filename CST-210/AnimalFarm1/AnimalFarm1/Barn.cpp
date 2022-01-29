#include "Barn.h"
#include <iostream>
using namespace std;

Barn::Barn()
{
	Horse* Lightning = new Horse("Lightning", 2200, "Horse");
	Horse* Greg = new Horse("Greg", 2197, "Horse");
	Horse* Martha = new Horse("Martha", 2190, "Horse");
	Horse* Horse4 = new Horse("Horse4", 1500, "Horse");
	Horse* Horse5 = new Horse("Horse5", 1700, "Horse");


	barn.push_back(Lightning);
	barn.push_back(Greg);
	barn.push_back(Martha);
	barn.push_back(Horse4);
	barn.push_back(Horse5);
	

	Chicken* Wing = new Chicken("Wing", 10, "Chicken");
	Chicken* Tender = new Chicken("Tender", 11, "Chicken");
	Chicken* Sandwich = new Chicken("Sandwich", 13, "Chicken");
	Chicken* Chicken4 = new Chicken("Chicken4", 9, "Chicken");
	Chicken* Chicken5 = new Chicken("Chicken5", 20, "Chicken");
	barn.push_back(Wing);
	barn.push_back(Tender);
	barn.push_back(Sandwich);
	barn.push_back(Chicken4);
	barn.push_back(Chicken5);


	Cow* Beef = new Cow("Beef", 1500, "Cow");
	Cow* Baccon = new Cow("Baccon", 1497, "Cow");
	Cow* Joe = new Cow("Joe", 1430, "Cow");
	Cow* Cow4 = new Cow("Cow4", 1160, "Cow");
	Cow* Cow5 = new Cow("Cow5", 1630, "Cow");
	barn.push_back(Beef);
	barn.push_back(Baccon);
	barn.push_back(Joe);
	barn.push_back(Cow4);
	barn.push_back(Cow5);

}

void Barn::feedingTime()
{
	for (int i = 0; i < barn.size(); i++)
	{
		barn[i]->speak();
		barn[i]->eat();
		if (barn[i]->getWeight() >= barn[i]->getTopWeight())
		{
			cout << barn[i]->getName() << " the " << barn[i]->getType() << " weighs " << barn[i]->getWeight() << " lbs. and is heading out to pasture" << endl;
			barn[i]->setWeight(barn[i]->getTopWeight() / 2);
			cout << barn[i]->getName() << " the " << barn[i]->getType() << " has returned from the pasture and now weighs " << barn[i]->getWeight() << " lbs." << endl;
		}
		cout << endl;
	}



}