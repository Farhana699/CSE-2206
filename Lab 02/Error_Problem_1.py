def error_analysis(true_value, approx_value):
    absolute_error = abs(true_value - approx_value)
    relative_error = absolute_error/abs(true_value)
    percentage_errror = relative_error*100
    
    return absolute_error, relative_error, percentage_errror

true_value = float(3.1416)
approx_value = float(3.14)
ae,re,pe= error_analysis(true_value,approx_value)

print(f"Absolute Error: {ae:.5f}")
print(f"Relative Error: {re:.5f}")
print(f"Percentage Error: {pe:.5f}%")