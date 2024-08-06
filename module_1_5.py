immutable_var=(1,2,"a","b")
print(immutable_var)
#immutable_var.append("Modified")#команда об изменении содержания кортежа выдает ошибку,
mutable_var=[1,2,"a","b"]                                       # т.к.кортеж является неизменяемой последовательностью
print(mutable_var)
mutable_var.append("Modified")
print(mutable_var)


