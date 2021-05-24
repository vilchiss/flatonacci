"""
Flatonacci secuence is a secuence which is result from the same given secuence
plus the sum of the last 3 numbers of the secuence.

The challenge is to create a flatonacci function that given a signature returns the first
n elements - signature included of the so seeded sequence. So, if we are to
start our Flatonacci sequence with [1, 1, 1] as a starting input (AKA signature) and n = 8,
we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31]

Another example; if signature is the secuence [0, 0, 1] we should get some thing
like:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]

- Signature will always contain 3 numbers
- n will always be a non-negative number
- if n == 0, then return an empty list and be ready for anything else which is not
clearly specified ;)

Note. Please note that we are gonna test the funcion against a lot of different signatures and n's
"""


def flatonacci(signature: list, n: int) -> list:
    if n <= 3:
        return signature[:n]
    else:
        copy = signature[:]
        for _ in range(3, n):
            copy.append(sum(copy[-3:]))
        return copy 

if __name__ == '__main__':
    print('Test')
    assert [] == flatonacci([1, 1, 1], 0)
    assert [1] == flatonacci([1, 1, 1], 1)
    assert [1, 1] == flatonacci([1, 1, 1], 2)
    assert [1, 1, 1] == flatonacci([1, 1, 1], 3)
    assert [1, 1, 1, 3, 5, 9, 17, 31] == flatonacci([1, 1, 1], 8)
    assert [0, 0, 1, 1, 2, 4, 7, 13, 24] == flatonacci([0, 0, 1], 9)
    print('All test passed')
