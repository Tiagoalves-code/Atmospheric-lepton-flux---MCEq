import crflux.models as crf
import MCEq.core
import MCEq.particlemanager
import numpy as np

# para criar gráficos com resultados, não é necessário para execução
import matplotlib.pyplot as plt

zenit_deg=0
#----------------------------------Múons para SIBYLL-2.E
mceq = MCEq.core.MCEqRun(
  interaction_model = 'SIBYLL23E',
  primary_model=(crf.HillasGaisser2012, 'H3a'),
  theta_deg =zenit_deg
)

mceq.solve()
MCEq.core.config.h_obs
mceq.pman.print_particle_tables(0)
mag = 3

muon_flux_prompt = (
  mceq.get_solution("pr_mu+",  mag) +
  mceq.get_solution("pr_mu-", mag)
)
energies = mceq.e_grid
plt.loglog(energies, muon_flux_prompt,
           label = "SIBYLL-2.3E",
           color='red',
           linestyle="-",
           linewidth=2)

#----------------------------------Múons para SIBYLL-2.D
mceq = MCEq.core.MCEqRun(
  interaction_model = 'SIBYLL23D',
  primary_model=(crf.HillasGaisser2012, 'H3a'),
  theta_deg =zenit_deg
)

mceq.solve()
MCEq.core.config.h_obs
mceq.pman.print_particle_tables(0)
mag = 3

muon_flux_prompt = (
  mceq.get_solution("pr_mu+",  mag) +
  mceq.get_solution("pr_mu-", mag)
)
energies = mceq.e_grid
plt.loglog(energies, muon_flux_prompt,
           label = "SIBYLL-2.3D",
           color='red',
           linestyle="--",
           linewidth=2)

#----------------------------------Múons para SIBYLL-2.3C (não funciona no MCEQ 1.4 então importamos os dados de uma simulação com os mesmos parâmetros no MCEq 1.3)
dados_23c = np.load(r"C:\Users\tiago\OneDrive\Documentos\Python\Pesquisa\sibyll23c_prompt.npz")

energies_23c = dados_23c["energies"]
flux_23c = dados_23c["flux"]
print("23c carregado:", dados_23c["flux"].shape)
plt.loglog(
    energies_23c,
    flux_23c,
    label="SIBYLL-2.3c",
    color="red",
    linestyle="-.",
    linewidth=1
)

#----------------------------------Múons para SIBYLL-2.1 (É o de referência)
mceq = MCEq.core.MCEqRun(
  interaction_model = 'SIBYLL21',
  primary_model=(crf.HillasGaisser2012, 'H3a'),
  theta_deg =zenit_deg
)

mceq.solve()
MCEq.core.config.h_obs
mceq.pman.print_particle_tables(0)
mag = 3

muon_flux_prompt = (
  mceq.get_solution("pr_mu+",  mag) +
  mceq.get_solution("pr_mu-", mag)
)
energies = mceq.e_grid
plt.loglog(energies, muon_flux_prompt,
           label = "SIBYLL-2.1",
           color='red',
           linestyle="dotted",
           linewidth=2)
#------------------------------Múons para EPOS-LHCR

mceq = MCEq.core.MCEqRun(
  interaction_model = 'EPOSLHCR',
  primary_model=(crf.HillasGaisser2012, 'H3a'),
  theta_deg = zenit_deg
)

mceq.solve()
MCEq.core.config.h_obs
mceq.pman.print_particle_tables(0)
mag = 3


muon_flux_prompt = (
  mceq.get_solution("pr_mu+",  mag) +
  mceq.get_solution("pr_mu-", mag)
)
energies = mceq.e_grid
plt.loglog(energies, muon_flux_prompt,
           label = "EPOS-LHCR",
           color='blue',
           linestyle="-",
           linewidth=2)



#------------------------------Múons para EPOS-LHC

mceq = MCEq.core.MCEqRun(
  interaction_model = 'EPOS-LHC',
  primary_model=(crf.HillasGaisser2012, 'H3a'),
  theta_deg = zenit_deg
)

mceq.solve()
MCEq.core.config.h_obs
mceq.pman.print_particle_tables(0)
mag = 3


muon_flux_prompt = (
  mceq.get_solution("pr_mu+",  mag) +
  mceq.get_solution("pr_mu-", mag)
)
energies = mceq.e_grid
plt.loglog(energies, muon_flux_prompt,
           label = "EPOS-LHC",
           color='blue',
           linestyle="--",
           linewidth=1)

#-----------------------Múons para QGSJet-III
mceq = MCEq.core.MCEqRun(
  interaction_model = 'QGSJETIII',
  primary_model=(crf.HillasGaisser2012, 'H3a'),
  theta_deg = zenit_deg
)

mceq.solve()
MCEq.core.config.h_obs
mceq.pman.print_particle_tables(0)
mag = 3


muon_flux_prompt = (
  mceq.get_solution("pr_mu+",  mag) +
  mceq.get_solution("pr_mu-", mag)
)
energies = mceq.e_grid
plt.loglog(energies, muon_flux_prompt,
           label = "QGSJet-III",
           color='green',
           linestyle="-",
           linewidth=2)


#-----------------------Múons para QGSJet-II-04
mceq = MCEq.core.MCEqRun(
  interaction_model = 'QGSJet-II-04',
  primary_model=(crf.HillasGaisser2012, 'H3a'),
  theta_deg = zenit_deg
)
mceq.solve()
MCEq.core.config.h_obs
mceq.pman.print_particle_tables(0)
mag = 3


muon_flux_prompt = (
  mceq.get_solution("pr_mu+",  mag) +
  mceq.get_solution("pr_mu-", mag)
)
energies = mceq.e_grid
plt.loglog(energies, muon_flux_prompt,
           label = "QGSJet-II-04",
           color='green',
           linestyle="--",
           linewidth=1)

#-----------------------Múons para DPMJETIII193
mceq = MCEq.core.MCEqRun(
  interaction_model = 'DPMJETIII193',
  primary_model=(crf.HillasGaisser2012, 'H3a'),
  theta_deg = zenit_deg
)
mceq.solve()
MCEq.core.config.h_obs
mceq.pman.print_particle_tables(0)
mag = 3


muon_flux_prompt = (
  mceq.get_solution("pr_mu+",  mag) +
  mceq.get_solution("pr_mu-", mag)
)
energies = mceq.e_grid
plt.loglog(energies, muon_flux_prompt,
           label = "DPMJET-III-193",
           color='black',
           linestyle="-",
           linewidth=2)

#legendas

plt.xlim(1., 1e9)
plt.xlabel("E / GeV")

plt.ylim(1e-6, 1.)
plt.ylabel("($E$/GeV)$^3$ $\Phi$/(GeV cm$^{-2}$ s$^{-1}$ sr$^{-1}$) ")

legend=plt.legend(loc="upper center", ncol=5, frameon=False)
plt.subplots_adjust(top=0.85) 
plt.tight_layout()
plt.legend(
    loc="upper left",          # Ponto de referência (canto superior esquerdo)
    bbox_to_anchor=(0.02, 0.98), # Coordenadas (x, y) levemente afastadas da borda
    ncol=1,                    # 1 coluna coloca um embaixo do outro
    frameon=True,              # Com fundo para não misturar com as linhas
    fontsize='small'           # Reduz um pouco o tamanho se forem muitos itens
)
# Definindo o estilo da caixa
caixa_estilo = dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', alpha=0.8)

# Adicionando o texto
# (x, y) são as coordenadas. No exemplo abaixo, 10^4 no eixo X e 0.5 no eixo Y.
plt.text(1e4, 0.4, rf'$\theta_{{zen}} = {zenit_deg}^\circ$', 
         fontsize=9, 
         bbox=caixa_estilo,
         horizontalalignment='center')
# Definindo o texto com LaTeX para os símbolos de neutrino e antineutrino
# \nu = neutrino, \bar{\nu} = antineutrino, \mu = muon
texto_fluxo = r"$\mu + \bar{\mu}$ prompt"
# Adicionando no canto superior direito (x=0.95, y=0.95)
plt.text(0.95, 0.95, texto_fluxo, 
         transform=plt.gca().transAxes, 
         fontsize=12,
         verticalalignment='top', 
         horizontalalignment='right',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.5))
plt.tight_layout()
plt.savefig("12.svg", dpi=300, bbox_extra_artists=[legend])
plt.show()

