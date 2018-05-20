#import dependencies
import numpy as np
import random as rnd
import population
  
if __name__ == '__main__':
    
    test_people = generate_sample(30)
    most_alive_years = max_population_year(test_people)[0]
    
    print(f'year(s) with the most people alive: {most_alive_years}')