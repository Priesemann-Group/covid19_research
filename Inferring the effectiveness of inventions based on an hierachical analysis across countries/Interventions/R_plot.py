import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def fsigmoid(x, a, b):
    return 1.0 / (1.0 + np.exp(-a * (x - b)))


class Change_point(object):
    """docstring for Change_point"""

    def __init__(self, alpha, gamma_max, length, begin):
        self.alpha = alpha
        self.gamma_max = gamma_max
        self.length = length
        self.begin = begin

    def get_gamma(self, t):
        return fsigmoid(t, 4.0 / (self.length), self.begin) * self.gamma_max


def gamma_from_delta_t(t, begin, delta_t):
    """
    """
    sigmoid = 1.0 / (1.0 + np.exp(((t - begin) / delta_t * 4)))

    return sigmoid / np.linalg.norm(sigmoid, 1)


def get_R_t(times, R_0, cps):
    R_t = []
    for t in times:
        _sum = 0
        for cp in cps:
            _sum += cp.alpha * cp.get_gamma(t)
        R_t.append(R_0 * np.exp(-_sum))
    return R_t


if __name__ == "__main__":

    fig, ax = plt.subplots(2, 1, figsize=(6, 3), constrained_layout=True)

    cp1 = Change_point(0.1, 0.5, 5, 8)
    cp2 = Change_point(0.2, 1, 2, 15)

    times = np.linspace(0, 24, 5000)  # 20 days

    """
        Create two plots:
        - the first one for gamma_i
        - the second one for R
    """

    # gamma cp 1
    ax[0].plot(
        times,
        cp1.get_gamma(times),
        color="tab:orange",
        label=r"$\gamma_{1,max}=0.5$, $l_1=5$, $d_1=8$",
    )

    # gamma cp 2
    ax[0].plot(
        times,
        cp2.get_gamma(times),
        color="tab:blue",
        label=r"$\gamma_{2,max}=1.0$, $l_2=2$, $d_2=15$",
    )

    # Plot R(t)
    ax[1].plot(
        times,
        get_R_t(times, 2, [cp1, cp2]),
        color="tab:green",
        label=r"$R^*_{eff}(t)$",
    )

    for axis in ax:
        axis.spines["right"].set_visible(False)
        axis.spines["top"].set_visible(False)

    ax[0].set_xlim(0)
    ax[1].set_xlim(0)
    ax[0].set_ylabel(r"$\gamma(t)$")
    ax[1].set_ylabel(r"$R^*_{eff}(t)$")
    ax[1].set_xlabel(r"$t$ in days")
    ax[0].tick_params(labelbottom=False)
    ax[0].legend(loc=2)
    save_kwargs = dict(transparent=True, format="pdf", dpi=300)
    fig.savefig("figures/example_interventions.pdf", **save_kwargs)
