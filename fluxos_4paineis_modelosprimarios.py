import crflux.models as crf
from MCEq.core import MCEqRun
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


interaction_model = "SIBYLL23E"
theta_degs = [0.0, 70.0]
mag = 3

# Cores por modelo primario (como no codigo de referencia).
modelos_primarios = [
    ("H3a", (crf.HillasGaisser2012, "H3a"), "red"),
    ("H4a", (crf.HillasGaisser2012, "H4a"), "blue"),
    ("GST3", (crf.GaisserStanevTilav, "3-gen"), "lime"),
    ("GST4", (crf.GaisserStanevTilav, "4-gen"), "black"),
]

# Estilos por tipo de fluxo (como no codigo de referencia).
estilos_fluxo = {
    "total": {"linewidth": 2.0},
}

fig, axes = plt.subplots(2, 2, figsize=(10, 10), sharex=False, sharey=False)

paineis = {
    "mu": {
        "ax": axes[0, 0],
        "xlabel": r"$E_{\mu}\,/\,\mathrm{GeV}$",
        "ylabel": r"$\left(E/\mathrm{GeV}\right)^3\,\Phi_{\mu}\,/\,(\mathrm{GeV\,cm^{-2}\,s^{-1}\,sr^{-1}})$",
        "total": ("total_mu+", "total_mu-"),
    },
    "nue": {
        "ax": axes[0, 1],
        "xlabel": r"$E_{\nu_e}\,/\,\mathrm{GeV}$",
        "ylabel": r"$\left(E/\mathrm{GeV}\right)^3\,\Phi_{\nu_e}\,/\,(\mathrm{GeV\,cm^{-2}\,s^{-1}\,sr^{-1}})$",
        "total": ("total_nue", "total_antinue"),
    },
    "numu": {
        "ax": axes[1, 0],
        "xlabel": r"$E_{\nu_\mu}\,/\,\mathrm{GeV}$",
        "ylabel": r"$\left(E/\mathrm{GeV}\right)^3\,\Phi_{\nu_\mu}\,/\,(\mathrm{GeV\,cm^{-2}\,s^{-1}\,sr^{-1}})$",
        "total": ("total_numu", "total_antinumu"),
    },
    "nutau": {
        "ax": axes[1, 1],
        "xlabel": r"$E_{\nu_\tau}\,/\,\mathrm{GeV}$",
        "ylabel": r"$\left(E/\mathrm{GeV}\right)^3\,\Phi_{\nu_\tau}\,/\,(\mathrm{GeV\,cm^{-2}\,s^{-1}\,sr^{-1}})$",
        "total": ("total_nutau", "total_antinutau"),
    },
}

for _, primary_model, cor in modelos_primarios:
    for theta_deg in theta_degs:
        mceq = MCEqRun(
            interaction_model=interaction_model,
            primary_model=primary_model,
            theta_deg=theta_deg,
        )
        mceq.solve()
        energias = mceq.e_grid

        linestyle = "-" if theta_deg == 0.0 else "--"

        for painel in paineis.values():
            ax = painel["ax"]
            total = (
                mceq.get_solution(painel["total"][0], mag)
                + mceq.get_solution(painel["total"][1], mag)
            )

            ax.loglog(
                energias,
                total,
                color=cor,
                linestyle=linestyle,
                **estilos_fluxo["total"],
            )


for painel in paineis.values():
    ax = painel["ax"]
    ax.set_xlim(1.0, 1e10)
    ax.set_ylim(1e-6, 1.0)
    ax.set_xlabel(painel["xlabel"])
    ax.set_ylabel(painel["ylabel"])
    ax.grid(False)

    legend_modelos = [
        Line2D([0], [0], color=cor, lw=2.0, linestyle="-", label=nome)
        for nome, _, cor in modelos_primarios
    ]
    leg_modelos = ax.legend(
        handles=legend_modelos,
        loc="upper right",
        fontsize=8,
        title_fontsize=9,
        frameon=True,
    )
    ax.add_artist(leg_modelos)

plt.tight_layout()
plt.savefig("fluxos_4paineis_primarios_sibyll23e.svg", dpi=300)
plt.show()