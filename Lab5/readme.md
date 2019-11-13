## LAB 5  - RANDOM NUM
There are 3 program files : 
- `randomGen.py` is the solution for part 1  (contains 3 methods)
- `random01.py` is the solution for part 2 (contains 4 methods)
- `test.py` is the solution for part 3

# Parameters Used : 
   - Mixed : a = 48271, m = 2147483647,c = 1
   - Additive : m = 2147483647
   - Multiplicative : a = 48271, m = 2147483647, q = 44488, r = 3399
   - Seed will be a unique number in each iteration by using current time in micro seconds

# How to run

## Part 1
- run `python randomGen.py`
- Sample Input (Number of random numbers to be generated):
    4
- Sample Output :  
    Multiplicative  
    [282821351.0, 515890142.0, 312673870.0, 565307654.0]  
   
    Additive  
    [1642282979.4831543, 1642282980.4831543, 1642282981.4831543, 1642282982.4831543]  

    Mixed
    [282871511.0, 789679856.0, 801594727.0, 418715372.0]  

## Part 2
- run `python random01.py`
- Sample Input (Number of random numbers to be generated):  
    4
- Sample Output :  
    Multiplicative  
    [0.4555919680071957, 0.8798876753448917, 0.057976573267009376, 0.5871681718095989]  

    Additive  
    [0.7648786148396246, 0.7648786153052859, 0.7648786157709472, 0.7648786162366085]  

    Mixed  
    [0.45559615523349317, 0.08200927641336307, 0.6697817499142986, 0.034850113575742636]  

    InBuilt  
    [0.5633565284330987, 0.03525648284326233, 0.26375718712323815, 0.20898680175448292]  

## Part 3
- run `python3 test.py`
- Sample Output :   
    Multiplicative  
    Frequency Obtained : [92, 102, 102, 113, 90, 115, 95, 102, 85, 104]  
    (O - E) * (O - E) / E : [0.64, 0.04, 0.04, 1.69, 1.0, 2.25, 0.25, 0.04, 2.25, 0.16]  
    ChiSquare Value : 8.36  
    Probability from matching the given Chi Square Table : 0.5  

    Additive
    Frequency Obtained : [104, 96, 104, 96, 104, 96, 104, 96, 104, 96]  
    (O - E) * (O - E) / E : [0.16, 0.16, 0.16, 0.16, 0.16, 0.16, 0.16, 0.16, 0.16, 0.16]  
    ChiSquare Value : 1.5999999999999999  
    Probability from matching the given Chi Square Table : 0.995  

    Mixed
    Frequency Obtained : [99, 107, 106, 93, 96, 98, 104, 87, 95, 115]  
    (O - E) * (O - E) / E : [0.01, 0.49, 0.36, 0.49, 0.16, 0.04, 0.16, 1.69, 0.25, 2.25]  
    ChiSquare Value : 5.9  
    Probability from matching the given Chi Square Table : 0.75  

    InBuilt
    Frequency Obtained : [102, 90, 101, 99, 69, 121, 96, 99, 122, 101]  
    (O - E) * (O - E) / E : [0.04, 1.0, 0.01, 0.01, 9.61, 4.41, 0.16, 0.01, 4.84, 0.01]   
    ChiSquare Value : 20.1  
    Probability from matching the given Chi Square Table : 0.05  
