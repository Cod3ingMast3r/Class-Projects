#include "Barn.h"
#include <iostream>
#include <thread>
#include <chrono>
using namespace std;

Barn::Barn()
{
	Horse Lightning = Horse("Lightning", 100, "Horse");
	Horse Greg = Horse("Greg", 200, "Horse");
	Horse Martha = Horse("Martha", 300, "Horse");
	Stalls.push_back(Lightning);
	Stalls.push_back(Greg);
	Stalls.push_back(Martha);

	Chicken Wing = Chicken("Wing", 100, "Chicken");
	Chicken Tender = Chicken("Tender", 200, "Chicken");
	Chicken Sandwich = Chicken("Sandwich", 300, "Chicken");
	Coup.push_back(Wing);
	Coup.push_back(Tender);
	Coup.push_back(Sandwich);

	Cow Beef = Cow("Beef", 100, "Cow");
	Cow Baccon = Cow("Baccon", 200, "Cow");
	Cow Joe = Cow("Joe", 300, "Cow");
	Pen.push_back(Beef);
	Pen.push_back(Baccon);
	Pen.push_back(Joe);
}

void Barn::feedingTime()
{
	cout << "There are 9 Animals. The Horses eat at 1:00. The Chickens eats at 3:00. The Cows eats at 5:00" <<endl << endl;

	cout << "It is 1:00 the Horses are eating" << endl << "#####################################################" << endl;
	for (int i = 0; i < size(Stalls); i++)
	{
		cout << Stalls[i].getName() << " the " << Stalls[i].getType() << " weighs " << Stalls[i].getWeight() << " lbs." << endl;
		Stalls[i].eat();
		cout << Stalls[i].getName() << " is eating and now weighs " << Stalls[i].getWeight() << " lbs." << endl;

	}

	cout << "#####################################################" << endl << endl;
	cout << "It is 3:00 the Chickens are eating" << endl << "#####################################################" << endl;


	for (int i = 0; i < size(Coup); i++)
	{
		cout << Coup[i].getName() << " the " << Coup[i].getType() << " weighs " << Coup[i].getWeight() << " lbs." << endl;
		Coup[i].eat();
		cout << Coup[i].getName() << " is eating and now weighs " << Coup[i].getWeight() << " lbs." << endl;

	}

	cout << "#####################################################" << endl << endl;
	cout << "It is 5:00 the Cows are eating" << endl << "#####################################################" << endl;
	
/*	string top1 = "             __n__n__";
	string top2 = "      .------`-\\00 / -'";
	string top3 = "     / ##   ## (oo)";
	string top4 = "    / \\## __   ./";
	string top5 = "       |//YY \\|/";
	string top6 = "       |||   |||";
	for (int i = 0; i < 100; i++)
	{
		top1 = " " + top1;
		top2 = " " + top2;
		top3 = " " + top3;
		top4 = " " + top4;
		top5 = " " + top5;
		top6 = " " + top6;
		cout << top1 << endl;
		cout << top2 << endl;
		cout << top3 << endl;
		cout << top4 << endl;
		cout << top5 << endl;
		cout << top6 << endl;
		this_thread::sleep_for(chrono::microseconds(100));
		cout << "\033[2J\033[1;1H";
	}
*/



	for (int i = 0; i < size(Pen); i++)
	{
		cout << Pen[i].getName() << " the " << Pen[i].getType() << " weighs " << Pen[i].getWeight() << " lbs." << endl;
		Pen[i].eat();
		cout << Pen[i].getName() << " is eating and now weighs " << Pen[i].getWeight() << " lbs." << endl;

	}
	cout << "#####################################################" << endl << endl;

}
