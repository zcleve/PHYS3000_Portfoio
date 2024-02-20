# Zackary Cleveland PHYS3000

def first_order_central_diff(x, dx):
    return (x[1:] - x[:-1]) / dx

def second_order_central_diff(x, dx):
    return (x[2:] - 2 * x[1:-1] + x[:-2]) / (dx ** 2)