## On the Risks of Collecting Multidimensional Data Under LDP

[Héber H. Arcolezi](https://hharcolezi.github.io/), [Sébastien Gambs](https://sebastiengambs.openum.ca/), [Jean-François Couchot](https://members.femto-st.fr/jf-couchot/en), [Catuscia Palamidessi](http://www.lix.polytechnique.fr/Labo/Catuscia.Palamidessi/). "On the Risks of Collecting Multidimensional Data Under Local Differential Privacy". PVLDB, 16(5): 1126 - 1139, 2023. doi:10.14778/3579075.3579086.

If our codes and work are useful to you, we would appreciate a reference to:

```
@article{Arcolezi2023,
  doi = {10.14778/3579075.3579086},
  url = {https://doi.org/10.14778/3579075.3579086},
  year = {2023},
  month = jan,
  publisher = {Association for Computing Machinery ({ACM})},
  volume = {16},
  number = {5},
  pages = {1126--1139},
  author = {H{\'{e}}ber H. Arcolezi and S{\'{e}}bastien Gambs and Jean-Fran{\c{c}}ois Couchot and Catuscia Palamidessi},
  title = {On the Risks of Collecting Multidimensional Data Under Local Differential Privacy},
  journal = {Proceedings of the {VLDB} Endowment}
}
```

## Codes
- The [attack_SMP](https://github.com/hharcolezi/risks-ldp/tree/main/attack_SMP) folder has the codes for reproducing the attacks to the SMP solution.
- The [attack_RSpFD](https://github.com/hharcolezi/risks-ldp/tree/main/attack_RSpFD) folder has the codes for reproducing the attacks to the RS+FD solution.
- The [countermeasure_RSpRFD](https://github.com/hharcolezi/risks-ldp/tree/main/countermeasure_RSpRFD) folder has the codes for reproducing the experiments/attacks of our countermeasure RS+RFD solution.

## Datasets
The [datasets](https://github.com/hharcolezi/risks-ldp/tree/main/datasets) folder has the following (pre-processed) datasets.
- [ACSEmployement](https://github.com/zykls/folktables)
- [Adult](https://archive.ics.uci.edu/ml/datasets/adult)

## Environment
I mainly used Python 3 with numpy, pandas, numba, and ray libaries. The versions I use are listed below:

- Python 3.8.8
- Numpy 1.23.1
- Pandas 1.2.4
- Numba 0.53.1
- Ray 1.11.0

## Contact
For any question, please contact [Héber H. Arcolezi](https://hharcolezi.github.io/): heber.hwang-arcolezi [at] inria.fr

## License
[MIT](https://github.com/hharcolezi/risks-ldp/blob/main/LICENSE)
