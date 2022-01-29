#pragma once
#include "Hero.h"
#include "Villain.h"
#include <string>
#include <vector>
using namespace std;
class Arena
{
private:
	vector <Villain*> villains;
	string name;
	vector <string> AddHero();
	vector <string> HeroSelection();
	vector <string> GetNonLabeledStats(vector <string> labeledHeroStats);
	int GetIndex();
	Villain* VillainSelection();
	void Store(Hero* goodguy);
	void Battle(Hero* goodguy ,Villain* badguy);
	string GetArenaName();
	void SaveAndExit();
	void HeroSelectionScreen();
	void BattleorStoreScreen();
	string AbilitySelection();
public:
	Arena();
	Arena(string n);
	void LoadingScreen();
};

