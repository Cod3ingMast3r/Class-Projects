#include "QuadAnswers.h"

double QuadAnswers::getSolution1(double a, double b, double c)
{
	if (pow(b, 2) - 4 * a * c > 0) {
		solution = (-b - sqrt(pow(b, 2) - (4 * a * c))) / (2 * a);
		cout << "Solution 1 is: " << solution << endl;
		return solution;
	}
	else if (pow(b, 2) - 4 * a * c < 0) {
		cout << "Solution 1 has a negative under the square root." << endl;
		return false;
	}
	else {
		return 0;
	}
}

double QuadAnswers::getSolution2(double a, double b, double c)
{
	if (pow(b, 2) - 4 * a * c > 0) {
		solution = (-b + sqrt(pow(b, 2) - (4 * a * c))) / (2 * a);
		cout << "Solution 2 is: " << solution << endl;
		return solution;
	}
	else if (pow(b, 2) - 4 * a * c < 0) {
		cout << "Solution 2 has a negative under the square root." << endl;
		return false;
	}
	else {
		return 0;
	}
}
