from math import fabs, exp

def func(x):
    return x * exp(x) - 1

def dfunc(x):
    return exp(x) * (1 + x)

def newton_raphson(f, df, x0, max_iter=100, eps=0.0001):
    iter_count = 1
    x_old = x0
    while iter_count <= max_iter:
        f_val = f(x_old)
        df_val = df(x_old)

        if df_val == 0:
            print("Zero derivative. Method fails.")
            return None

        x_new = x_old - f_val / df_val
        error = fabs(x_new - x_old)

        print(f"Iteration {iter_count}: x = {x_new:.6f}, f(x) = {f(x_new):.6f}")

        if error <= eps:
            return x_new

        x_old = x_new
        iter_count += 1

    print("Maximum iterations reached.")
    return x_old

x0 = 2.5
root = newton_raphson(func, dfunc, x0)
if root is not None:
    print(f"\nRoot found at x = {root:.6f}")
    print(f"f(x) = {func(root):.6f}")
