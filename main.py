#
# $H(z)= H_0 \sqrt{\Omega_m (1+z)^3 +(1-\Omega_m)}$

import numpy as np

distances_hubble_data=np.array([0.07  , 0.09  , 0.12  , 0.17  , 0.179 , 0.199 , 0.2   , 0.27  ,
       0.28  , 0.352 , 0.3802, 0.4   , 0.4004, 0.4247, 0.4497, 0.47  ,
       0.4783, 0.48  , 0.5929, 0.6797, 0.7812, 0.8754, 0.88  , 0.9   ,
       1.037 , 1.3   , 1.363 , 1.43  , 1.53  , 1.75  , 1.965 ]);


hubble_parameter_wrt_distance = np.array([ 69. ,  69. ,  68.6,  83. ,  75. ,  75. ,  72.9,  77. ,  88.8,
        83. ,  83. ,  95. ,  77. ,  87.1,  92.8,  89. ,  80.9,  97. ,
       104. ,  92. , 105. , 125. ,  90. , 117. , 154. , 168. , 160. ,
       177. , 140. , 202. , 186.5])

shz=np.array([19.6, 12. , 26.2,  8. ,  4. ,  5. , 29.6, 14. , 36.6, 14. , 13.5,
       17. , 10.2, 11.2, 12.9, 34. ,  9. , 62. , 13. ,  8. , 12. , 17. ,
       40. , 23. , 20. , 17. , 33.6, 18. , 14. , 40. , 50.4])


# define the model (y = mx + b)
def line_model(params, x):
    m, c = params
    y = m*x + c
    return y

def alt_empirical_model(params, x):
    # the formula
    # $H(z)= H_0 \sqrt{\Omega_m (1+z)^3 +(1-\Omega_m)}$
    omega = params[0]
    h_naught = params[1]
    omega_1plusxcube = omega * (1 + x)**3
    arrtobeqsrted = omega_1plusxcube + (1 - omega)
    roott = np.sqrt(arrtobeqsrted)
    hypothesized = h_naught * roott
    return hypothesized

def get_chisq(params, x, y):
    # hypothesized = line_model(params, x)
    hypothesized = alt_empirical_model(params, x)
    err = y - hypothesized
    res = np.sum(err**2 / hypothesized)
    # p = (1 / np.sqrt(2 * np.pi * data['ey']**2)) * exp( - err**2 / (2 * data['ey']**2))
    return res

def andhere_me_teer():
    inp = ''
    while True:
        inp = input('Enter param1 and param2 sepped by space ["done" when done]: ')
        if inp == 'done':
            break
        param1, param2 = list([float(x) for x in inp.split()])
        print('chi sq is: ')
        print(get_chisq([param1, param2], distances_hubble_data, hubble_parameter_wrt_distance))


if __name__ == '__main__':
    andhere_me_teer()



# TODO:
# Write a code for $\chi^2$ minimization and calculating log likelihood

# got m=72, c=60 with almost minimum of chi sq 34.1 with the linear model
# got H0=69.4, omega=7 with almost minimum of chi sq 353.97 with the linear model
