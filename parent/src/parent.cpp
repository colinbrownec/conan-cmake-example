#include <iostream>
#include <child.h>

int main() {
  for (int i = 0; i < 10; i++)
    std::cout << child::text() << "\n";

  return 0;
}
