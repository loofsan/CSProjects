/*
  Lynn T. Aung
  CIS - 254
  Project 8.1
  Drawing Rocket
*/

#include <iostream>
using namespace std;

// Function declarations
void drawCone();
void drawBox(int width, int height);
void drawHorizontalLine(int numXs);
void draw2VerticalLines(int numSpaces, int numRows);
void drawOneRow(int numSpaces);
void getDimensions(int& width, int& height, int& stages);
void drawRocket(int width, int height, int stages);

int main() {
    int width, height, stages;

    // Phase 3: Getting user input for dimensions and number of stages
    getDimensions(width, height, stages);

    // Drawing the rocket with the user-specified dimensions
    drawRocket(width, height, stages);

    return 0;
}

// Function to get the dimensions (width, height, and number of stages) from the user
void getDimensions(int& width, int& height, int& stages) {
    cout << "enter width: ";
    cin >> width;
    cout << "enter height of each stage: ";
    cin >> height;
    cout << "enter number of stages: ";
    cin >> stages;
}

// Function to draw the rocket
void drawRocket(int width, int height, int stages) {
    drawCone();
    for (int i = 0; i < stages; i++) {
        drawBox(width, height);
    }
    drawCone();
}

// Function to draw the cone part of the rocket
void drawCone() {
    cout << "  X  " << endl;
    cout << " X X " << endl;
    cout << "X   X" << endl;
}

// Function to draw the box part of the rocket (stage)
void drawBox(int width, int height) {
    drawHorizontalLine(width);  // Top horizontal line
    draw2VerticalLines(width - 2, height - 2);  // Vertical sides
    drawHorizontalLine(width);  // Bottom horizontal line
}

// Function to draw the horizontal line
void drawHorizontalLine(int numXs) {
    for (int count = 0; count < numXs; count++) {
        cout << "X";
    }
    cout << endl;
}

// Function to draw the two vertical lines (for box sides)
void draw2VerticalLines(int numSpaces, int numRows) {
    for (int rowCount = 0; rowCount < numRows; rowCount++) {
        drawOneRow(numSpaces);
    }
}

// Function to draw one row of vertical lines
void drawOneRow(int numSpaces) {
    cout << "X";
    for (int spaceCount = 0; spaceCount < numSpaces; spaceCount++) {
        cout << " ";
    }
    cout << "X" << endl;
}
