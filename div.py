#!/usr/bin/env python3

def div(b,a,value_after_decimal=True,full=False):
    """
    Integer Division
    a -> divisor
    b -> dividend
    (b/a) as fraction
    """
    if type(b) == int and type(a) == int and a != b:
        if b == 0:
            return float(0)
        if a == 0:
            raise ZeroDivisionError(f"({b}/{a}), division by zero") from None
        neg = False
        if b < 0 and a < 0:
            b = b * -1
            a = a * -1
            pass
        elif b < 0:
            b = b * -1
            neg = True
        elif a < 0:
            a = a * -1
            neg = True
        b = [int(i) for i in list(str(b))]
        remainder = 0
        res = ''
        for i in range(len(b)):
            load = [remainder, b[i]]
            v = ''
            for i in load:
                v += str(i)
            v = int(v)
            n = 0
            for x in range(0,11):
                if a*x <= v:
                    n = x
                else:
                    res += str(n)
                    remainder = v - a*(x-1)
                    break
        def floating(b,a):
            res = ''
            v = b
            for x in range(0,11):
                if a*x <= v:
                    n = x
                else:
                    res += str(n)
                    remainder = v - a*(x-1)
                    break
            if remainder != 0:
                b = remainder*10
                try:
                    res += floating(b,a)
                except RecursionError:
                    pass
            return res
        if neg == True:
            res = int(res) * -1
        if remainder != 0 and value_after_decimal == True:
            res = str(int(res))
            res += "."
            b = remainder * 10
            res += floating(b,a)
        if full == True:
            return res
        else:
            return float(res)
    elif type(a) == int and type(b) == int and a == b:
        if a == 0:
            raise ZeroDivisionError(f"({b}/{a}), division by zero") from None
        return float(1)
    else:
        raise ValueError("Invalid argument.")

if __name__ == '__main__':
    import sys
    try:
        v = sys.argv[1].split("/")
        a = int(v[1])
        b = int(v[0])
        try:
            if sys.argv[2] == '-f':
                print(div(b,a,full=True))
        except IndexError:
            print(div(b,a))
    except IndexError:
        help = """
        MISSING Argument.

            Usage:
            $: python div.py x/y
            where, x and y are integers

            Other usage:
            $: python div.py x/y -f
            Display a longer value
            for irrational result
            """
        print(help)