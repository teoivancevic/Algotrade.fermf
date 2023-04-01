#include <iostream>
#include <fstream>
#include "json.h"

int main() {
  Json::Value root;  // Create a JSON object

  root["name"] = "John";  // Add some key-value pairs
  root["age"] = 30;
  root["married"] = true;

  std::ofstream file("example.json");  // Open a file for writing
  file << root;  // Write the JSON object to the file

  std::cout << "JSON file written successfully!" << std::endl;

  return 0;
}
