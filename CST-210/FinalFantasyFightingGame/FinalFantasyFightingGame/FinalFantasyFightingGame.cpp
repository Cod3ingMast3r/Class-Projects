# include "Arena.h"
#include <iostream>
#include <ctime>
using namespace std;

int main()
{
    srand(time(NULL));
    Arena myArena = Arena("GCU");
    myArena.LoadingScreen();
}
