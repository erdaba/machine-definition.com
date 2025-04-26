'''
Here I will write the website of machines definition
This website will introduce the definition of finite machines that can be represented within a computer.
The machine will be of limited number of variables that is to fit its truth table on one PC page (height and width included).
This may restrict me to 5 variables thus 32 lines. 
I will need to allow poeple to choose the amount of variable which will inputs the rest will be variable which belongs to the machine.
We will still require that the machine's proper variable is at least 1, otherwise the machine would not even exist.
I will ask as input the function of 5 variables. Give an instance of what it should be.
Then I will ask to choose the initial state of the machine and the initially chosen input.
Then the user should be able to start the simulation which will generate the truth table and the the graph of the machine.
I will need to display the state of the machine through the truth table and the graph. 
I need to highlight the edge of actual choice and the vertex of actual state. 
I will need to allow to choose the actual choice in an increasing or decreasing order with j and k.
It is possible to use html5 canvas to achieve a 2D app. Therefore it would be great to build 
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/machine-instance')
def machine_instance():
    return render_template('machine-instance.html')
