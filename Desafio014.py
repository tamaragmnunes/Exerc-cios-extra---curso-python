# Crie um programa que leia a temperatura  em Celsius e mostre os resultados em Farenheit e Kelvin

tc = float(input('Digite a temperatura em Celsius: '))
tk = tc+273
tf = (tc*(9/5)+32)
print ('A temperatura de {} Celsius, corresponde a {} Kelvin e {} Farenheit'.format(tc, tk, tf))
