console.log("This is perceptron.js")

class Perceptron{
    constructor(weights,bias,threshold){
        this.weights = weights;
        this.bias = bias;
        this.threshold = threshold;
    }
    toString(){
        return `Weights = ${this.weights}, bias = ${this.bias}, threshold = ${this.threshold}`
    }
    stepActivation(){
        
    }
}

const p = new Perceptron([0,0],0,0);
console.log(p);
