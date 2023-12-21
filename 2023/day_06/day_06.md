This is obviously a system of equations:

button_time + race_time = total_time
button_time * race_time = total_score

so, button_time * race_time - record = 0

eg, total_time = 7, record = 9

button_time + race_time = 7
button_time * race_time = 9

(7 - race_time) * race_time = 9
7R - R^2 = 9

9/R = 7 - R
-R2 + 7R - 9 = 0

quadratic equation:
R = (-1 +- squareroot(7^2 - 4(-1)(-9))) / 2*(-1)
(-1 +- sqrt(49-36)) / -2
(-1 +- 3.6) / -2
-4.6 / -2 = 2.3
2.6 / -2  = -1.3


try that again:
button time    race time     score
0                 7             0
1                 6             6
2                 5            10 (?)
3                 4            12
4                 3            12
5                 2            10
6                 1             6


B + R = T
B * R = S

solving for B:
B + R - T = 0

B * (T - B) = S
-B^2 + TB - S = 0

-B^2 + 7B - 9 = 0

Right, correct the first time.  The solutions are 1.69 and 5.3.  take
the floor and ceiling of those and you get 5 and 2, and the number of 
solutions when 2 is the lowest solution and 5 is the highest one is 4,
because it's inclusive


Except the strict quadratic solution as I implemented it is problematic when the solutions
are whole numbers.  Let's check that out:
race:  time 30, distance 200
quadratic equation  =  -b^2 + 30b - 200 = 0

button time     race time     score
10                20            200   *NOT a record
11                19            209
12                18            
13                17
14
15
16
17
18
19
20