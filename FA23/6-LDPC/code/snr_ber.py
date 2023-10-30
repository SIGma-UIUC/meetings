import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from math import erfc, sqrt, log

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
matplotlib.rcParams['font.size'] = 14


def Q(x: float) -> float:
    return 0.5 * erfc(x / sqrt(2))


x = np.linspace(0, 12, num=10**3)
ber = list(map(lambda x: Q(sqrt(2 * 10**(x / 10))), x))

plt.xlabel(r'$E_b/N_0$ (db)')
plt.ylabel(r'BER')
plt.yscale('log')


def monte_carlo_BER(rounds: int, trials: int, sigma: float) -> float:
    errs = 0
    for _ in range(rounds):
        signal = np.random.choice([-1, 1], size=(trials))
        noise = np.random.normal(0, sigma, trials)

        rcvd = signal + noise
        rcvd = [-1 if x < 0 else 1 for x in rcvd]

        errs += sum(1 for x, y in zip(signal, rcvd) if x != y)
    return errs / (trials * rounds)


# Increase the number of rounds/trials for more precision!
ber_exp = [
    monte_carlo_BER(10**2, 10**2, sqrt(1 / (2 * 10**(y / 10)))) for y in x
]
ber_exp = [x if x != 0 else float("NaN") for x in ber_exp]

path = "tmp.svg"

plt.plot(x, ber_exp, color='red')
plt.plot(x, ber, color='black', linewidth=1)
plt.savefig(path, format='svg')
