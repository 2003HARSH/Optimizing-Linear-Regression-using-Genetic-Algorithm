# Linear Regression Optimization Using Genetic Algorithm

This project demonstrates the optimization of linear regression parameters (weights and biases) using a genetic algorithm. The genetic algorithm employs custom crossover and mutation methods to evolve the population of neural networks over several generations.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Classes and Methods](#classes-and-methods)
- [Output](#output)
- [Notes](#notes)
- [License](#license)

## Introduction

The genetic algorithm in this project optimizes the parameters for a simple linear regression model. The goal is to minimize the mean squared error between the predicted and actual values by evolving a population of candidate solutions through selection, crossover, and mutation.

## Installation

To run the code, ensure you have Python and the following libraries installed:

- `numpy`

You can install the required library using the following command:

```bash
pip install numpy
```

## Usage

The main components of this project are the `Dna` and `Population` classes. The `Dna` class defines the crossover and mutation methods, while the `Population` class manages the population of neural networks, calculates fitness scores, performs natural selection, and generates new populations.

### Classes and Methods

#### Dna Class

- **crossover(parent1, parent2)**: Combines the parameters of two parents to create a child.
- **mutation(child, mutation_rate, mutation_scale)**: Applies mutations to the child with a given mutation rate and scale.

#### Population Class

- **\_\_init\_\_(population_size, number_of_parameters, mutation_rate)**: Initializes the population with the given size, number of parameters, and mutation rate.
- **generate_population()**: Generates an initial random population.
- **calculate_fitness(population_list, X, Y)**: Calculates the fitness of each individual in the population based on the mean squared error.
- **natural_selection(population_list, fitness_scores, mating_pool_length)**: Selects the top individuals to form a mating pool.
- **generate_new_population(mating_pool, mutation_scale)**: Generates a new population from the mating pool using crossover and mutation.


## Output

The code will print the parameters and fitness score of each neural network in the population for each generation. Finally, it will display the parameters of the most fit neural network and its fitness score.

## Notes

- The mutation and crossover methods are essential to explore the parameter space effectively.
- The fitness function used here is based on the mean squared error of the predicted values against the actual values.
- The code can be extended or modified to work with different fitness functions, mutation rates, and population sizes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
