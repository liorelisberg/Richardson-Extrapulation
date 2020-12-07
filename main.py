import numpy


def richardson(f, x, n, h):
    """Richardson's Extrapolation to approximate  f'(x) at a particular x.

    USAGE:
	d = richardson( f, x, n, h )

    INPUT:
	f	- function to find derivative of
	x	- value of x to find derivative at
	n	- number of levels of extrapolation
	h	- initial step size

    OUTPUT:
        numpy float array -  two-dimensional array of extrapolation values.
                             The [n+1,n+1] value of this array should be the
                             most accurate estimate of f'(x).

    NOTES:
        Based on an algorithm in "Numerical Mathematics and Computing"
        4th Edition, by Cheney and Kincaid, Brooks-Cole, 1999.

    AUTHOR:
        Jonathan R. Senning <jonathan.senning@gordon.edu>
        Gordon College
        February 9, 1999
        Converted ty Python August 2008
    """

    # d[n,n] will contain the most accurate approximation to f'(x).

    d = numpy.array([[0] * (n + 1)] * (n + 1), float)

    for i in range(n + 1):
        d[i, 0] = 0.5 * (f(x + h) - f(x - h)) / h

        powerOf4 = 1  # values of 4^j
        for j in range(1, i + 1):
            powerOf4 = 4 * powerOf4
            print(powerOf4)
            d[i, j] = d[i, j - 1] + (d[i, j - 1] - d[i - 1, j - 1]) / (powerOf4 - 1)

        h = 0.5 * h

    return d


if __name__ == '__main__':
    f = lambda x: x ** 6 + 5 * x ** 4 - 3 * x ** 3 + 6 * x
    x = 0.5
    n = 2
    h = 1
    print(richardson(f, x, n, h))
