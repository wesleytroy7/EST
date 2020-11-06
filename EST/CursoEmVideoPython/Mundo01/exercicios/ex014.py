"""
    leia a temperatura em graus celsius e converta em farenheit

"""

temperaturaC = float(input('Entre com a temperatura em °C :'))

conversaoFahrenheit = ((temperaturaC * 1.8) + 32)
print('{:.1f}°C equivale a {:.1f}°F'.format(temperaturaC, conversaoFahrenheit))

temperaturaF = float(input('Entre com a temperatura em °F: ' ))

conversaoCelsius = (temperaturaF - 32) / 1.8 

print('{:.1f}°F equivale a {:.1f}°C'.format(temperaturaF, conversaoCelsius))

