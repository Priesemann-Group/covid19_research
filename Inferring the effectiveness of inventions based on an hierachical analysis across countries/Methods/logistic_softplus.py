import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def logistics(x):
    """
    Logistics function for plotting purpose
    
    f(x) = e^x / ( 1 + e^x )

    Parameters
    ----------
    x: number

    Returns
    -------
    :number
        Function value f(x) in [0,1]
    """

    return np.exp(x) / (1 + np.exp(x))


def softplus(x):
    """
    Softplus function for plotting purpose
    
    f(x) = ln(1+e^x)

    Parameters
    ----------
    x: number

    Returns
    -------
    :number
        Function value f(x) in [0,1]

    """

    return np.log(1 + np.exp(x))


if __name__ == "__main__":

    fig, ax = plt.subplots(1, 1, figsize=(4.5, 2.5), constrained_layout=True)

    x = np.linspace(-4, 4, 5000)  #
    y1 = logistics(x)
    y2 = softplus(x)
    ax.plot(x, y2, color="tab:orange", label="Softplus function")
    ax.plot(x, y1, color="tab:blue", label="Logistic function")

    x1 = np.linspace(-4, 0, 5000)
    x2 = np.linspace(0, 4, 5000)
    ax.plot(x1, [0.01] * 5000, color="tab:purple", ls="--")
    ax.plot(x2, x2, color="tab:purple", label="Rectifier", ls="--")

    ax.legend(loc=2)
    ax.set_ylabel(r"$f(x)$")
    ax.set_xlabel(r"$x$")
    ax.set_ylim(0, 2)
    ax.set_xlim(-4, 4)
    ax.axhline(1.0, ls=":", color="tab:gray")
    save_kwargs = dict(transparent=True, format="pdf", dpi=300)
    fig.savefig("figures/logistic_softplus_comparison.pdf", **save_kwargs)
