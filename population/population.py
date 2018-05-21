#!/usr/bin/env python

#import dependencies
import numpy as np
import random as rnd

def max_population_year(people_list):
        '''Given a list of people with their birth and death years from 
        [1900, 2000], find the year(s) with most number of people alive
        
        Input Parameters
        ----------------
        people_list: list with each entry of the form [birth, death] for each person
        
        Output Parameters:
        ----------------
        max_year_list: list of years that had a population equal to the maximum 
        population obtained in the period 1900, 2000
        
        year_list: list with length of 101 that contains the population per year
        
        >>> max_population_year([[1900,1902]])[0]
        [1900, 1901, 1902]
        
        >>> max_population_year([[1900,1950], [1925,1950], [1900,2000], [1930,1930]])[0]
        [1930]
        
        >>> max_population_year([[2000,2000]])[0]
        [2000]
        
        '''
        #create an array with 100 elements to represent each year between 1900-2000
        #setting its values to zero; index 0-->1900, 1-->1901,  ... , 100 --> 2000 
        year_list = np.zeros(101)
        #loop over the list of people and get the birth and death years
        for person in people_list:
            birth, death = person
            #check the years to be between 1900-2000, send exception upstream
            if birth < 1900 or birth > 2000:
                raise ValueError('Valid birth value must be between [1900, 2000]')
            if death < 1900 or death > 2000:
                raise ValueError('Valid death value must be between [1900, 2000]')
            if birth > death:
                raise ValueError('Birth year must be less or equal to death year')
            #map actual year to index in year_list
            birth = birth - 1900
            death = death - 1900
            #increment the values in the year_list for the years on which the current person was alive
            #beware of numpy's slice access from [initial-index, final-index) 
            year_list[birth:death + 1] = year_list[birth:death + 1] + 1
        
        max_population = year_list.max()
        #find the year (or years) with the maximum count, these years are the years
        #with the most people alive
        max_year_list = np.where(year_list == max_population)[0]
        #convert indices to years
        max_year_list = max_year_list + 1900
        #return the list
        return max_year_list.tolist(), year_list.tolist()
    
def generate_sample(n_samples):
    '''test function to generate a sample of people with birth and death dates
    between 1900 and 2000. Birth dates are selected randomly between 1900-2000
    and death dates are selected randomly between birth-2000
    
    Input Parameters
    ----------------
    n_sample: int, number of samples to generate 
        
    Output Parameters
    ----------------
    samples: list of n_samples lenght. Each entry contains a randomly generated
    birth and death dates as [birht, death] within 1900 and 2000 and the 
    death >= birth
    
    '''
    samples = []
    #loop over n_samples
    for sample in np.arange(n_samples):
        #pick a random birth date: 1900 <= birth <= 2000
        birth = rnd.randint(1900,2000)
        #pick a random death date: birth <= death <= 200
        death = rnd.randint(birth, 2000)
        #add sample to our list
        samples.append([birth, death])
    return samples     
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()