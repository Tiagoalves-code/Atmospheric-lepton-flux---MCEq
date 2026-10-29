import crflux.models as crf
import MCEq.core
import MCEq.particlemanager
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

mag = 3

# figura com 4 painéis
fig, axes = plt.subplots(2, 2, figsize=(10, 10), sharex=True, sharey=True)

# facilitar acesso
ax_mu   = axes[0, 0]
ax_nue  = axes[0, 1]
ax_numu = axes[1, 0]
ax_nutau= axes[1, 1]

# cores das contribuições
cores = {
    "total": "red",
    "conv": "blue",
    "prompt": "green"
}

# estilos dos ângulos
angulos = {
    0: "-",
    60: "--"
}

for theta, estilo in angulos.items():
    mceq = MCEq.core.MCEqRun(
        interaction_model='SIBYLL23E',
        primary_model=(crf.HillasGaisser2012, 'H3a'),
        theta_deg=theta
    )
    mceq.solve()
    energies = mceq.e_grid

    # -------------------
    # MÚONS
    # -------------------
    mu_total = (
        mceq.get_solution("total_mu+", mag) +
        mceq.get_solution("total_mu-", mag)
    )
    mu_conv = (
        mceq.get_solution("conv_mu+", mag) +
        mceq.get_solution("conv_mu-", mag)
    )
    mu_prompt = (
        mceq.get_solution("pr_mu+", mag) +
        mceq.get_solution("pr_mu-", mag)
    )

    ax_mu.loglog(energies, mu_total,  color=cores["total"],  linestyle=estilo, linewidth=2.5)
    ax_mu.loglog(energies, mu_conv,   color=cores["conv"],   linestyle=estilo, linewidth=2)
    ax_mu.loglog(energies, mu_prompt, color=cores["prompt"], linestyle=estilo, linewidth=2)

    # -------------------
    # NEUTRINOS ELETRÔNICOS
    # -------------------
    nue_total = (
        mceq.get_solution("total_nue", mag) +
        mceq.get_solution("total_antinue", mag)
    )
    nue_conv = (
        mceq.get_solution("conv_nue", mag) +
        mceq.get_solution("conv_antinue", mag)
    )
    nue_prompt = (
        mceq.get_solution("pr_nue", mag) +
        mceq.get_solution("pr_antinue", mag)
    )

    ax_nue.loglog(energies, nue_total,  color=cores["total"],  linestyle=estilo, linewidth=2.5)
    ax_nue.loglog(energies, nue_conv,   color=cores["conv"],   linestyle=estilo, linewidth=2)
    ax_nue.loglog(energies, nue_prompt, color=cores["prompt"], linestyle=estilo, linewidth=2)

    # -------------------
    # NEUTRINOS MUÔNICOS
    # -------------------
    numu_total = (
        mceq.get_solution("total_numu", mag) +
        mceq.get_solution("total_antinumu", mag)
    )
    numu_conv = (
        mceq.get_solution("conv_numu", mag) +
        mceq.get_solution("conv_antinumu", mag)
    )
    numu_prompt = (
        mceq.get_solution("pr_numu", mag) +
        mceq.get_solution("pr_antinumu", mag)
    )

    ax_numu.loglog(energies, numu_total,  color=cores["total"],  linestyle=estilo, linewidth=2.5)
    ax_numu.loglog(energies, numu_conv,   color=cores["conv"],   linestyle=estilo, linewidth=2)
    ax_numu.loglog(energies, numu_prompt, color=cores["prompt"], linestyle=estilo, linewidth=2)

    # -------------------
    # NEUTRINOS TAUÔNICOS
    # -------------------
    nutau_total = (
        mceq.get_solution("total_nutau", mag) +
        mceq.get_solution("total_antinutau", mag)
    )
    nutau_conv = (
        mceq.get_solution("conv_nutau", mag) +
        mceq.get_solution("conv_antinutau", mag)
    )
    nutau_prompt = (
        mceq.get_solution("pr_nutau", mag) +
        mceq.get_solution("pr_antinutau", mag)
    )

    ax_nutau.loglog(energies, nutau_total,  color=cores["total"],  linestyle=estilo, linewidth=2.5)
    ax_nutau.loglog(energies, nutau_conv,   color=cores["conv"],   linestyle=estilo, linewidth=2)
    ax_nutau.loglog(energies, nutau_prompt, color=cores["prompt"], linestyle=estilo, linewidth=2)


# -------------------
# ajustes dos eixos
# -------------------
for ax in [ax_mu, ax_nue, ax_numu, ax_nutau]:
    ax.set_xlim(1., 1e9)
    ax.set_ylim(1e-6, 1.)
    ax.grid(True, which="both", alpha=0.3)

# labels eixo x
ax_mu.set_xlabel(r"$E_{\mu}\,/\,\mathrm{GeV}$")
ax_nue.set_xlabel(r"$E_{\nu_e}\,/\,\mathrm{GeV}$")
ax_numu.set_xlabel(r"$E_{\nu_\mu}\,/\,\mathrm{GeV}$")
ax_nutau.set_xlabel(r"$E_{\nu_\tau}\,/\,\mathrm{GeV}$")

# labels eixo y
ax_mu.set_ylabel(r"$\left(E/\mathrm{GeV}\right)^3\,\Phi_{\mu}\,/\,(\mathrm{GeV\,cm^{-2}\,s^{-1}\,sr^{-1}})$")

ax_nue.set_ylabel(r"$\left(E/\mathrm{GeV}\right)^3\,\Phi_{\nu_e}\,/\,(\mathrm{GeV\,cm^{-2}\,s^{-1}\,sr^{-1}})$")

ax_numu.set_ylabel(r"$\left(E/\mathrm{GeV}\right)^3\,\Phi_{\nu_\mu}\,/\,(\mathrm{GeV\,cm^{-2}\,s^{-1}\,sr^{-1}})$")

ax_nutau.set_ylabel(r"$\left(E/\mathrm{GeV}\right)^3\,\Phi_{\nu_\tau}\,/\,(\mathrm{GeV\,cm^{-2}\,s^{-1}\,sr^{-1}})$")
# -------------------
# legenda 1: tipo de fluxo
# -------------------
legend_fluxos = [
    Line2D([0], [0], color='red',   lw=2.5, label='Fluxo total'),
    Line2D([0], [0], color='blue',  lw=2.5, label='Fluxo convencional'),
    Line2D([0], [0], color='green', lw=2.5, label='Fluxo prompt')
]

# -------------------
# legenda 2: ângulo
# -------------------
legend_angulos = [
    Line2D([0], [0], color='black', lw=2.5, linestyle='-',  label=r'$\theta = 0^\circ$'),
    Line2D([0], [0], color='black', lw=2.5, linestyle='--', label=r'$\theta = 60^\circ$')
]

fig.legend(handles=legend_fluxos, loc='upper center', ncol=3, frameon=False, bbox_to_anchor=(0.5, 0.98))
fig.legend(handles=legend_angulos, loc='upper center', ncol=2, frameon=False, bbox_to_anchor=(0.5, 0.94))

plt.tight_layout(rect=[0, 0, 1, 0.90])
plt.savefig("fluxos_4paineis.svg", dpi=300)
plt.show()
