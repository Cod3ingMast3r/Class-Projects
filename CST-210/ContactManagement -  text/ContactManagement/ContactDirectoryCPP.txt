#include "ContactDirectory.h"
#include <iostream>
#include <fstream>
#include <string>
#include <Compare>
using namespace std;

int selection;
string contactFile = "Contacts.txt";
fstream myFile;     //create myFile object

string userInput, temp, name, address, stZip, phone;

bool foundContact = false;

int numberOfInputs = 6; // this is all info entered pluss index value and a space between each one
int foundIndex;
int index;


void ContactDirectory::AddContact()
{
    cin.ignore();
    cout << "enter name ";
    getline(cin, name);         //use getline() incase user wants a space.       
    cout << "Enter address ";
    getline(cin, address);
    cout << "Enter State and Zip ";
    getline(cin, stZip);
    cout << "Enter Phone Number ";
    getline(cin, phone);


    index = GetIndex();

    cout << index << endl << name << endl << address << endl << stZip << endl << phone << endl << endl;
    myFile.open(contactFile, ios::app);
    myFile << index << endl << name << endl << address << endl << stZip << endl << phone << endl << endl;
    myFile.close();
}

void ContactDirectory::DisplayContact()
{
    cout << "Enter 1 to Search by Index" << endl << endl;
    cout << "Enter 2 to Search by Name" << endl << endl;
    cout << "Directory Selection: ";
    cin >> selection;

    if (selection == 1) {
        
        cout << "What index Number do you seek from 0 to " << GetIndex()-1 << endl;
        cout << "Chosen Index: ";
        cin >> userInput;

        index = 0;
        foundIndex = 0;
        foundContact = false;
        myFile.open(contactFile);  //reopen it
        while (getline(myFile, temp)) {    //store each line in temp
            index = index + 1;
            if (foundContact == true and index < foundIndex + numberOfInputs) {
                cout << temp << endl;
            }
            if (userInput == temp) {
                foundIndex = index;
                foundContact = true;
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
        foundIndex = 0;
        foundContact = false;

        myFile.open(contactFile);  //reopen it
        while (getline(myFile, temp)) {    //store each line in temp
            index = index + 1;
            if (userInput == temp) {
                foundIndex = index;
                foundContact = true;
            }
            if (foundContact == true and index < foundIndex + numberOfInputs-1) {
                cout << temp << endl;
            }
        }
        myFile.close();
    }
}

int ContactDirectory::GetIndex()
{
    index = 0;
    myFile.open(contactFile);  //reopen it
    while(getline(myFile, temp)) {    //store each line in temp
        index = index + 1;
    }
    index = index / numberOfInputs;
    myFile.close();
    return index;
}

void ContactDirectory::DirectorySelection()
{
    cout << "Contact Management System Directory" << endl << endl;
    cout << "=========================================" << endl << endl;
    cout << "Enter 1 to add a contact" << endl << endl;
    cout << "Enter 2 to search a contact" << endl << endl;
    cout << "Enter 3 to quit" << endl << endl;
    cout << "Directory Selection: ";
    cin >> selection;
    if (selection == 1) {
        AddContact();
        DirectorySelection();
    }
    if (selection == 2) {
        DisplayContact();
        DirectorySelection();
    }
    if (selection == 3) {
        myFile.open(contactFile);
        myFile.close();
        GetIndex();
        return;
    }
}

ContactDirectory::ContactDirectory()
{
}
