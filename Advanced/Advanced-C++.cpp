// This script will teach you some more advanced programming concepts using C++.
// This tutorial is for advanced programmers who have a good understanding of the basics. 
// It assumes that you are familiar with basic data types, loops and conditional statements in C++

// We will be making some complex calculations involving vectors and matrices.
// Lets begin!

//  First we need to include necessary libraries
#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Let's start by creating a vector of integers
    vector<int> myVector = {10,20,30,40};
    
    cout << "The elements of the vector are: ";
    // Now let's print out each element of the vector
    for (int i=0 ; i < myVector.size(); i++) {
        cout << myVector[i] << " ";
    }
    cout << endl;

    // Next, let's create a matrix which is essentially a two-dimensional array.
    // In this case, our matrix will consist of vectors as its rows.
    vector<vector<int>> myMatrix(3);   // Create a 3xN matrix where N can vary
                                       // The number of columns is not specified here
                                       // but it can be set later on if needed

    // Fill the first row of the matrix with values from -5 to 5
    int val = -5;
    for (auto &row : myMatrix) {
        row.push_back(val);
        val++;
    }

    // Print out the elements of the matrix
    cout << "Elements of the matrix:" << endl;
    for (const auto& row : myMatrix) {
        for (const auto& elem : row) {
            cout << elem << "\t";
        }
        cout << endl;
    }

    // Add another column to the matrix filled with even numbers starting from 0
    // We use an index operator to access the last row of the matrix and add a value to it
    // This way we append a new column to the right side of the matrix
    for (int i=0; i < myMatrix.size(); i++) {
        int newColumnValue = (myMatrix.back().size() % 2 == 0 ? myMatrix.back().size()/2 : -(myMatrix.back().size()/2 + 1));
        myMatrix.back().push_back(newColumnValue);
    }

    // Print out the newly added column
    cout << "Newly added column:" << endl;
    for (const auto& row : myMatrix) {
        for (const auto& elem : row) {
            cout << elem << "\t";
        }
        cout << endl;
    }

    return 0;
    }