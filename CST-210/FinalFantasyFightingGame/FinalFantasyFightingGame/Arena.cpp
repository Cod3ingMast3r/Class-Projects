#include "Arena.h"
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <Compare>
#include <vector>
#include "Hero.h"
#include "Villain.h"
using namespace std;

int selection;
string HerosFile = "Heros.txt";
string NewHerosFile = "NewHeros.txt";
fstream myFile;     //create myFile object
fstream myNewFile;

string userInput, temp, newTemp;
string arenaName;
string CurrentIndex, name, major, HealthLevel, DamageLevel, SpecialAbility, money;
bool validInput = false;
int index;
int NumberOfInputs = 8; // this is all string info entered pluss index value and a space between each one

int damageCostMultiplier = 13;
int healthCostMultiplier = 10;

Villain* Antagonist;
Hero* Protagonist;
vector <string> heroStats;
vector <string> labeledHeroStats;
vector <string> nonLabeledHeroStats;

vector <string> Arena::AddHero()
{
    cin.ignore();
    cout << "enter name ";
    getline(cin, name);         //use getline() incase user wants a space.       
    cout << "Choose your Major: Engineering or Business or Nursing" << endl << "Enter E or B or N respectively: ";
    getline(cin, major);
    major = "Character major: " + major;
    name = "Character name: " + name;

    if (major == "Character major: E")
    {
        major = "Character major: Engineering";
        HealthLevel = "Character Health Level: 1";
        DamageLevel = "Character Damage Level: 3";
        SpecialAbility = "Character Special Ability: Prove teacher wrong (Double Damage (25% Chance))";
        money = "Character Money : 100";
    }
    if (major == "Character major: B")
    {
        major = "Character major: Buisness";
        HealthLevel = "Character Health Level: 2";
        DamageLevel = "Character Damage Level: 1";
        SpecialAbility = "Character Special Ability: Pay for someone to do Your Hw (Kill instantlly (5% Chance))";
        money = "Character Money : 300";
    }
    if (major == "Character major: N")
    {
        major = "Character major: Nursing";
        HealthLevel = "Character Health Level: 3";
        DamageLevel = "Character Damage Level: 1";
        SpecialAbility = "Character Special Ability: Take Aderoll (Restore to Max Health (34% Chance))";
        money = "Character Money : 10";
    }
    
    
    index = GetIndex();

    CurrentIndex = "Character Index: ";
    CurrentIndex += to_string(index);
    myFile.open(HerosFile, ios::app);
    myFile << CurrentIndex << endl << name << endl << major << endl <<  HealthLevel << endl << DamageLevel << endl <<  SpecialAbility << endl <<  money << endl << endl;
    myFile.close();

    heroStats.push_back(CurrentIndex);
    heroStats.push_back(name);
    heroStats.push_back(major);
    heroStats.push_back(HealthLevel);
    heroStats.push_back(DamageLevel);
    heroStats.push_back(SpecialAbility);
    heroStats.push_back(money);

    cout << "Here are your selected Characters Stats: " << endl;

    for (int i = 0; i < heroStats.size(); i++)
    {
        cout << heroStats[i] << endl;
    }

    cout << endl;
    return heroStats;
}

vector <string> Arena::HeroSelection()
{
    cout << "Enter 1 to Search by Index" << endl << endl;
    cout << "Enter 2 to Search by Name" << endl << endl;
    cout << "Directory Selection: ";
    cin >> selection;

    if (selection == 1) {

        cout << "What index Number do you seek from 0 to " << GetIndex() - 1 << endl;
        cout << "Chosen Index: ";
        cin >> userInput;

        index = 0;
        myFile.open(HerosFile);  //reopen it
        while (getline(myFile, temp)) {    //store each line in temp
            index = index + 1;

            if ("Character Index: " + userInput == temp) {
                CurrentIndex = temp;
                heroStats.push_back(CurrentIndex);
                getline(myFile, name);
                heroStats.push_back(name);
                getline(myFile, major);
                heroStats.push_back(major);
                getline(myFile, HealthLevel);
                heroStats.push_back(HealthLevel);
                getline(myFile, DamageLevel);
                heroStats.push_back(DamageLevel);
                getline(myFile, SpecialAbility);
                heroStats.push_back(SpecialAbility);
                getline(myFile, money);
                heroStats.push_back(money);

                cout << "Here is your selected Character's information: " << endl;

                for (int i = 0; i < heroStats.size(); i++)
                {
                    cout << heroStats[i] << endl;
                }

                cout << endl;
            }
        }
        myFile.close();
    }
    if (selection == 2) {
        cin.ignore();

        cout << "What Name do you seek " << endl;
        cout << "Chosen Name: ";

        getline(cin, userInput);

        index = 0;
        myFile.open(HerosFile);  //reopen it
        while (getline(myFile, temp)) {    //store each line in temp
            index = index + 1;

            if ("Character name: " + userInput == temp) {
                heroStats.push_back(CurrentIndex);
                name = temp;
                heroStats.push_back(name);
                getline(myFile, major);
                heroStats.push_back(major);
                getline(myFile, HealthLevel);
                heroStats.push_back(HealthLevel);
                getline(myFile, DamageLevel);
                heroStats.push_back(DamageLevel);
                getline(myFile, SpecialAbility);
                heroStats.push_back(SpecialAbility);
                getline(myFile, money);
                heroStats.push_back(money);

                cout << "Here is your selected Characters information: " << endl;

                for (int i = 0; i < heroStats.size(); i++)
                {
                    cout << heroStats[i] << endl;
                }

                cout << endl;

            }
            //this is at the end because the index comes before the name
            CurrentIndex = temp;
        }
        myFile.close();
    }
    return heroStats;
}

vector<string> Arena::GetNonLabeledStats(vector <string> labeledStats)
{
    vector <string> nonLabeledStats;
    string nonLabeledStat;
    for (int stat = 0; stat < labeledStats.size(); stat++)
    {
        int pos = labeledStats[stat].find(':') + 2; //gets rid of the found character and pace after it by adding two
        nonLabeledStat = labeledStats[stat].substr(pos);
        nonLabeledStats.push_back(nonLabeledStat);
    }

    return nonLabeledStats;
}

int Arena::GetIndex()
{
    index = 0;
    myFile.open(HerosFile);  //reopen it
    while (getline(myFile, temp)) {    //store each line in temp
        index = index + 1;
    }
    index = index / NumberOfInputs;
    myFile.close();
    return index;
}

Villain* Arena::VillainSelection()
{   
    cout << "The following villians available to fight are... " << endl << endl;
    for (int villain = 0; villain < villains.size(); villain++)
    {
        villains[villain]->getStats();
        cout << endl;
    }

    cout << endl << endl << "Which villian would you like to Battle?" << endl;
    cout << "Enter a nuber (0-" << villains.size()-1 << ") Based on where they appeared" << endl;
    int villainChoice;
    cin >> villainChoice;
    return villains[villainChoice];
}

void Arena::Battle(Hero* goodguy, Villain* badguy)
{
    cout << endl <<"Life is unfair, the vilian always gets the first attack" << endl << endl;
    
    bool dead = false;

    while (dead == false)
    {
        
        cout << badguy->getName() << " Has done " << badguy->getDamage() << " damage to you." << endl;

        goodguy->updateCurrentHealth(-badguy->getDamage());

        cout << "Your new Health is now at " << goodguy->getCurrentHealth() << endl;

        if (goodguy->getCurrentHealth() <= 0)
        {
            cout << "Sorry, you lost, maybe try someone a little easier or buy better stats... or just dont suck." << endl <<endl;
            goodguy->updateCurrentHealth(goodguy->getHealth());
            badguy->updateCurrentHealth(badguy->getHealth());
            BattleorStoreScreen();
        }

        cout << "How wil you repond?" << endl;

        while (validInput == false)
        {
            cout << "1- Attack with " << goodguy->getDamage() << " damage" << endl;
            cout << "or" << endl;
            cout << "2- Use your special Ability: " << goodguy->getSpecialAbility() << endl;
            char x;
            cin >> x;
        
            switch (x) {
            case '1':
                badguy->updateCurrentHealth(-goodguy->getDamage());
                cout << endl << "Nice Job, you did " << goodguy->getDamage() << " Damage to " << badguy->getName() << "'s health leaving them with " << badguy->getCurrentHealth() << " remaining." << endl;
                validInput = true;
                break;
            case '2':
                goodguy->useSpecialAblity(badguy);
                validInput = true;
                break;
            default:
                cout << endl << "Invalid Input, please try again" << endl;
            }
        }
        validInput = false;
        if (badguy->getCurrentHealth() <= 0)
        {
            cout << "Nice Job, You won " << badguy->getMoney() << " dollars!! maybe try someone a little hard or buy better stats... Don't be a wuss." << endl;
            goodguy->updateMoney(badguy->getMoney());
            goodguy->updateCurrentHealth(goodguy->getHealth());
            badguy->updateCurrentHealth(badguy->getHealth());
            BattleorStoreScreen();
        }
    }
}

void Arena::Store(Hero* goodguy)
{
    goodguy->getStats();


    while (validInput == false)
    {
        cout << "Please note that the Cost to upgrade your health is: " << goodguy->getHealth() * healthCostMultiplier << " and the cost to upgrade you damage is: " << goodguy->getDamage() * damageCostMultiplier << endl;

        cout << "You currently have " << goodguy->getMoney() << " dollars to your name." << endl;


        if ((goodguy->getMoney() < (goodguy->getHealth() * healthCostMultiplier)) && (goodguy->getMoney() < (goodguy->getDamage() * damageCostMultiplier)))
        {
            cout << "It appears that you do not have enough money to purchase either of these upgrades and as a result we will be sending you back to the main menue" << endl;
            BattleorStoreScreen();
        }

        cout << "What would you like to upgrade? Health (h) or Damage (d) or go back (b)?" << endl;
        char x;
        cin >> x;
        switch (x) {
        case 'h':
            if (goodguy->getMoney() >= (goodguy->getHealth() * healthCostMultiplier))
            {
                cout << "Your Health was at " << goodguy->getHealth();

                goodguy->updateMoney(-(goodguy->getHealth() * healthCostMultiplier));
                goodguy->updateHealth(1);

                cout << " But it has been upgraded to " << goodguy->getHealth() << endl;
                break;
            }
            else
            {
                cout << "Sorry you have insufficent funds for this" << endl;
                break;
            }
        case 'd':
            if (goodguy->getMoney() >= (goodguy->getDamage() * damageCostMultiplier))
            {
                cout << "Your Damage was at " << goodguy->getDamage();

                goodguy->updateMoney(-(goodguy->getDamage() * damageCostMultiplier));
                goodguy->updateDamage(1);
                

                cout << " But it has been upgraded to " << goodguy->getDamage() << endl;
                break;
            }
            else
            {
                cout << "Sorry you have insufficent funds for this" << endl;
                break;
            }
        case 'b':
            BattleorStoreScreen();
            break;
        default:
            cout << endl << "Invalid Input, please try again" << endl;
        }
    }
    validInput = false;
}

Arena::Arena()
{
}

Arena::Arena(string n)
{
    arenaName = n;
}

string Arena::GetArenaName()
{
    return arenaName;
}

void Arena::LoadingScreen()
{
    Villain* business = new Villain("0", " Professor Easy A", "B", 1, 1, "None", 10);
    villains.push_back(business);

    Villain* Jackson = new Villain("1", " Professor Jackson", "B", 5, 5, "None", 200);
    villains.push_back(Jackson);

    Villain* Sarlo = new Villain("2", "Professor Sarlo", "E", 7, 7, "None", 500);
    villains.push_back(Sarlo);

    Villain* Doc = new Villain("3", "Doc", "E", 10, 10, "None", 1000);
    villains.push_back(Doc);

    while (validInput == false)
    {
        cout << "Would you like to play a game? (y/n): ";
        char x;
        cin >> x;
        switch (x) {
        case 'y':
            cout << endl << "Yay" << endl;
            HeroSelectionScreen();
            break;
        case 'n':
            cout << endl << "Fine, goodbye" << endl;
            ::exit(0);
        default:
            cout << endl << "Invalid Input, please try again" << endl;
        }
    }
    validInput = false;
}
void Arena::HeroSelectionScreen()
{
    while (validInput == false)
    {
        cout << "Create or select Hero? (c/s): ";
        char x;
        cin >> x;
        switch (x) {
        case 'c':
            labeledHeroStats = AddHero();
            validInput = true;
            break;
        case 's':
            labeledHeroStats = HeroSelection();
            validInput = true;
            break;
        default:
            cout << endl << "Invalid Input, please try again" << endl;
        }
    }
    validInput = false;
    nonLabeledHeroStats = GetNonLabeledStats(labeledHeroStats);
    Protagonist = new Hero(nonLabeledHeroStats[0], nonLabeledHeroStats[1], nonLabeledHeroStats[2], stoi(nonLabeledHeroStats[3]), stoi(nonLabeledHeroStats[4]), nonLabeledHeroStats[5], stoi(nonLabeledHeroStats[6]));
    BattleorStoreScreen();
}

void Arena::BattleorStoreScreen()
{
    while (validInput == false)
    {
        cout << "Want to go batle in the " << GetArenaName() << " arena (a) or spend money in the store (s) or save and exit(e): ";
        char x;
        cin >> x;
        switch (x) {
        case 'a':
            Antagonist = VillainSelection();
            Battle(Protagonist, Antagonist);
            break;
        case 's':
            Store(Protagonist);
            break;
        case 'e':
            SaveAndExit();
            break;
        default:
            cout << endl << "Invalid Input, please try again" << endl;
        }
    }
    validInput = false;
}

void Arena::SaveAndExit()
{
    myFile.open(HerosFile);
    ofstream CreateNewHerosFile(NewHerosFile);
    myNewFile.open(NewHerosFile);
    while (getline(myFile, temp)) {    //store each line in temp
        if ("Character Index: " + Protagonist->getIndex() == temp) {
            myNewFile << temp << endl;
            cout << "Your Hero " << Protagonist->getName() << "s new saved stats are..." << endl;
            getline(myFile, temp);
            temp = "Character name: " +  Protagonist->getName();
            myNewFile << temp << endl;
            getline(myFile, temp);
            temp =  "Character major: " + Protagonist->getMajor();
            myNewFile << temp << endl;
            getline(myFile, temp);
            temp = "Character Health Level: " + to_string(Protagonist->getHealth());
            cout << temp << endl;
            myNewFile << temp << endl;
            getline(myFile, temp);
            temp =  "Character Damage Level: " + to_string(Protagonist->getDamage());
            cout << temp << endl;
            myNewFile << temp << endl;
            getline(myFile, temp);
            temp = "Character Special Ability: " + Protagonist->getSpecialAbility();
            cout << temp << endl;
            myNewFile << temp << endl;
            getline(myFile, temp);
            temp = "Character Money : " + to_string(Protagonist->getMoney());
            cout << temp << endl;
            myNewFile << temp << endl;
        }
        else
        {
        myNewFile << temp << endl;
        }
        
        //this is at the end because the index comes before the name
    }
    myFile.close();
    myNewFile.close();
    CreateNewHerosFile.close();
    remove(HerosFile.c_str());
    rename(NewHerosFile.c_str(), HerosFile.c_str());
    ::exit(0);
}




