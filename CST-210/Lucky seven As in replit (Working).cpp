#include <iostream>
#include <string>
#include <ctime>
#include <fstream>
#include <vector>
using namespace std;

void one(){
  int integers[5] = {0,1,2,3,4};
  int supalow = integers[0];
  int supahigh = integers[0];
  for(int integer = 0; integer < 4; integer++){
    if (supahigh < integers[integer]){
      supahigh = integers[integer];
    }
    if (supalow > integers[integer]){
      supalow = integers[integer];
    }
  }
  //imports number
  cout << "High = " << supahigh << endl; 
  cout << "Low = " << supalow << endl;
}


void two(){
  int count = 0;
  for (int i = 1; i <= 50; i++){ //prints 50 numbers
    if (i % 7 == 0){ //formula to find multiples of 7
      count += i;
      if (i == 50){ //stop
      
      } 
    }
  }
  cout << "Sum = " << count; //Prints Sum
}


void three(){
  unsigned int total = 1;
  for(int i = 10; i >= 2; i--){ //10 terms
    total *= i;
    cout << total << " * " << " " << i - 1 << endl; //* used to seperate 
    
  }
  cout << total;
}


void four(){
  string originala, flippedo;
  cout << "Put a word to see if you can write it backwords : ";
  getline(cin, originala); //reads string
  for (int i = originala.length()-1; i >=0; i--){
    flippedo += originala[i]; //loop to read string
  }
  if (originala == flippedo){ //test if palindrome is postive 
    cout << "Yes you can write this word backwords " << endl; 
  }

  else{
    cout << "Nope, try again. " << endl; //test if palindrome is negative
  }
}

void five(){
  int prime;
  bool checker = true;
  cout << "Put a number ";
  cin >> prime; // verify that number is prime
  for (int i = 2; i <= prime / 2; i++){
    if (prime % 2 == 0){ //formula 
      checker = false; 
    }
  

  }
  if (checker){
    cout << prime << " is a Prime number" << endl;

  }
  else {
    cout << prime << " is not a Prime Number" << endl;
  }
}

void six(){
  srand(time(NULL));
  int total = 0;
  int numArray[20];
  for (int a = 0; a < 20; a++){
  numArray[a] = rand() % 100 + 1; //array of random intergers, picks a place holder and randomly assign a value between 1-100
  cout << numArray[a] << endl;
  total += numArray[a]; //adds the 20 numbers
  }

  cout << "Average is " << total / 20 ; //divides the 20's number total by 20 
  
}

void seven() {
  fstream myFile;
  int vec; 
  vector<string> myVector(vec);
  string show;
  int big = 0; //sets variable for smallest to reiceve size
  myFile.open("text.txt"); //reads string from the file
  cout << "Enter size of the Array : ";
  cin >> vec;
   for (int i = 0; i < vec; i++){
     myFile >> show;
     myVector.push_back(show); //scans text

   }
   myFile.close();

  for (int i = 0; i < myVector.size(); i++){
      cout << myVector[i] << " ";
   }

   for (int i = 0; i < myVector.size(); i++){
     if(myVector[i].size() > myVector[big].size()){
       big = i; //asigns biggest with word that fits array 
     }
   }
   cout << endl << "Biggest word is " << "'" << myVector[big] << "'" ;
  }

  

  

  int main(){ //prints program and spaces them out
  cout << endl;
  cout << endl;
  cout << "1." << endl;
  one();
  cout << endl;
  cout << "2." << endl;
  two();
  cout << endl;
  cout << endl;
  cout << "3." << endl;
  three();
  cout << endl;
 cout << endl;
  cout << "4." << endl;
  four();
  cout << endl;
  cout << endl;
  cout << "5." << endl;
  five();
  cout << endl;
  cout << endl;
  cout << "6." << endl;
  six();
  cout << endl;
  cout << endl;
  cout << "7." << endl;
  seven();
  }