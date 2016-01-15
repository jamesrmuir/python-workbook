// ComputerSciencePrize20142015.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
	//Array to store the random points
	int points[5][2];

	//Creates the 2D array for the map
	int grid[50][50];  

	for (int x = 0; x < 50; x++){
		for (int y = 0; y < 50; y++){
			grid[x][y] = 0;
		}
	}

	/*Prints out array 
	for (int i = 0; i < 50; i++){
		for (int j = 0; j < 50; j++)
		{
			cout << "grid[" << i << "][" << j << "]: ";
			cout << grid[i][j] << endl;
		}
	}
	*/

	//Generates five random points 
	for (int x = 0; x < 5; x++){
		points[x][0] = rand() % 50;
		points[x][1] = rand() % 50;
	}

	/*Prints out array
	for (int i = 0; i < 5; i++){
		for (int j = 0; j < 2; j++)
		{
		cout << "points[" << i << "][" << j << "]: ";
		cout << points[i][j] << endl;
		}
	}
	//*/

	// Generates a start and end point and makes sure they are not the same
	int startPoint[2];
	int endPoint[2];
	do {
		//Defines the start point 
		
		int randomNumberOne = rand() % 5;
		startPoint[0] = points[randomNumberOne][0];
		startPoint[1] = points[randomNumberOne][1];

		//Defines the end point
		int randomNumberTwo = rand() % 5;
		endPoint[0] = points[randomNumberTwo][0];
		endPoint[1] = points[randomNumberTwo][1];
	} while (startPoint[0] == endPoint[0] && startPoint[1] == endPoint[1]);

	cout << "Start point: " << startPoint[0] << " " << startPoint[1] << endl;
	cout << "End point: " << endPoint[0] << " " << endPoint[1] << endl;
	
	system("pause");
	return 0;
}
