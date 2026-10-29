# Atmospheric-lepton-flux---MCEq
Python scripts and simulation workflows using MCEq (Matrix Cascade Equations) to model and analyze atmospheric lepton fluxes for high-energy astrophysics research.

Tiago Alves Pereira
||Federal University of Pelotas (UFPel)
||Institute of Physics and Mathematics (IFM)
||High and Medium Energy Group (GAME)

# Atmospheric Lepton Fluxes with MCEq

Notebooks and scripts for computing and visualizing atmospheric muon and neutrino fluxes using [MCEq](https://github.com/mceq-project/MCEq) (Matrix Cascade Equations) together with the [`crflux`](https://github.com/mceq-project/crflux) cosmic-ray flux models.

The analyses explore how the predicted lepton fluxes depend on:

- the **hadronic interaction model** (SIBYLL, EPOS-LHC, QGSJet, DPMJET),
- the **primary cosmic-ray flux model** (Hillas-Gaisser H3a/H4a, Gaisser-Stanev-Tilav),
- the **zenith angle** and **atmospheric density profile**,
- the **primary composition** (proton vs. iron),
- the **pion/kaon production ratio** (K/π).

Results are presented for conventional, prompt and total fluxes of muons and of electron, muon and tau neutrinos, including detector-specific scenarios (IceCube and Pierre Auger sites).

---

## Repository contents

### Notebooks

| File | Description |
|------|-------------|
| `Dependencia_energetica.ipynb` | Angular (cos θ) dependence of the muon and muon-neutrino flux at fixed energies (10 GeV, 10 TeV, 1 PeV), split into contributions from π decay, K decay and prompt decays, for two seasons at the South Pole (IceCube site, MSIS00 atmosphere). |
| `Espetro_do_Múon_e_Profundidade_inclinada.ipynb` | Single-primary air-shower study (proton and iron) at the **Auger** (1425 m, θ = 67°) and **IceCube** (2835 m, θ = 13°) sites. Includes atmospheric depth vs. height, longitudinal muon profiles, muon and ν<sub>μ</sub> energy spectra, model-to-EPOS-LHC ratios, and the Fe/p ratio with a model-spread metric. Compares EPOS-LHC-R, QGSJet-III, SIBYLL-2.3E and SIBYLL-2.1. |
| `KPi.ipynb` | Sensitivity of the lepton fluxes to the kaon-to-pion production ratio, implemented by reweighting p→π and p→K production with `set_mod_pprod`. Shows nominal vs. modified fluxes for μ, ν<sub>μ</sub> and ν<sub>e</sub>. |
| `Partículas_x_perfil_atm.ipynb` | Impact of the atmospheric model (CORSIKA parametrizations and MSIS00 for South Pole January/August, plus the US Standard atmosphere) on the μ, ν<sub>μ</sub>, ν<sub>e</sub> and ν<sub>τ</sub> fluxes at θ = 0° and 90°, shown as ratios to the US Standard atmosphere. |

### Scripts

| File | Description |
|------|-------------|
| `Densidade_Atmosférica.py` | Plots the atmospheric mass density ρ as a function of slant depth X for the US Standard, CORSIKA and MSIS00 South Pole atmospheres (θ = 0° and 70°). |
| `Fluxo_de_partículas_em_função_da_energia_variando_o_angulo_zenital.py` | Four-panel figure (μ, ν<sub>e</sub>, ν<sub>μ</sub>, ν<sub>τ</sub>) with total, conventional and prompt fluxes versus energy for θ = 0° and 60° (SIBYLL-2.3E, H3a). Saves `fluxos_4paineis.svg`. |
| `fluxos_4paineis_modelosprimarios.py` | Four-panel comparison of the total flux for different primary models (H3a, H4a, GST 3-gen, GST 4-gen) at θ = 0° and 70° with SIBYLL-2.3E. Saves `fluxos_4paineis_primarios_sibyll23e.svg`. |
| `NOVO_MCEQ_Fluxo_de_múons_para_multiplos_modelos_de_interação_3_.py` | Prompt muon flux (μ⁺ + μ⁻) for multiple interaction models: SIBYLL-2.3E/2.3D/2.3c/2.1, EPOS-LHC-R, EPOS-LHC, QGSJet-III, QGSJet-II-04 and DPMJET-III-193. Saves `12.svg`. |

---

## Requirements

- Python 3.9+
- [MCEq](https://github.com/mceq-project/MCEq) (developed and tested with **v1.4**)
- [crflux](https://github.com/mceq-project/crflux)
- `numpy`, `scipy`, `matplotlib`
- Jupyter (for the notebooks)

```bash
pip install MCEq crflux numpy scipy matplotlib jupyter
```

Refer to the MCEq documentation for details on installing the interaction-model databases.

## Usage

Run a script directly:

```bash
python fluxos_4paineis_modelosprimarios.py
```

Or open a notebook:

```bash
jupyter notebook KPi.ipynb
```

Each script creates one or more `MCEqRun` instances, calls `solve()`, extracts fluxes with `get_solution(...)` scaled by E³ (`mag = 3`), and plots them in log-log scale. Expect noticeable run times when many interaction models or angles are evaluated.

## Notes

- **SIBYLL-2.3c** is not available in MCEq 1.4. The multi-model muon script loads a precomputed spectrum (`sibyll23c_prompt.npz`) generated with MCEq 1.3 using the same parameters. The path to this file is hard-coded to a local Windows directory; update it before running (and place the file in the repository if you want others to reproduce the plot).
- Variable names, comments and axis labels are partly in Portuguese.
- Flux conventions: `conv_` = conventional (π, K), `pr_` = prompt (charm and heavier), `total_` = conv + prompt. Fluxes are in GeV cm⁻² s⁻¹ sr⁻¹ after E³ scaling.

## References

- A. Fedynitch et al., *Calculation of conventional and prompt lepton fluxes at very high energy*, EPJ Web Conf. 99 (2015) 08001, [arXiv:1503.00544](https://arxiv.org/abs/1503.00544).
- MCEq documentation and examples: <https://mceq.readthedocs.io>

## Acknowledgments

Several notebooks are adapted from the example notebooks distributed with MCEq.

## License

Add a license of your choice (e.g. MIT) in a `LICENSE` file.
