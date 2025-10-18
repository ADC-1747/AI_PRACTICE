#include <iostream>
#include <vector>

using namespace std;

class Perceptron{
    private:
    vector<float> weights;
    float bias;
    float threshold;

    public:
    Perceptron(vector<float> weights_, float bias_, float threshold_)
        : weights(weights_), bias(bias_), threshold(threshold_) {}

};

int main(){
  std::cout << "Hello perceptron.cpp" << std::endl;
  
  Perceptron p({0.0f,1.0f}, 0.0f, 0.0f);

  return 0;
}
