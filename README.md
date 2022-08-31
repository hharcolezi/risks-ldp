## On the Risks of Collecting Multidimensional Data Under LDP

[Héber H. Arcolezi](https://hharcolezi.github.io/), [Sébastien Gambs](https://sebastiengambs.openum.ca/), [Jean-François Couchot](https://members.femto-st.fr/jf-couchot/en), [Catuscia Palamidessi](http://www.lix.polytechnique.fr/Labo/Catuscia.Palamidessi/). "On the Risks of Collecting Multidimensional Data Under Local Differential Privacy" (2022). [Full Version]().

## Abstract
The private collection of multiple statistics from a  population is a fundamental statistical problem. One possible approach to realize this is to rely on the local model of differential privacy (LDP). Numerous LDP protocols have been developed for the task of frequency estimation of single and multiple attributes. These studies mainly focused on improving the utility of the algorithms to ensure the server performs the estimations accurately. In this paper, we investigate privacy threats (re-identification and attribute inference attacks) against LDP protocols for multidimensional data following two state-of-the-art solutions for frequency estimation of multiple attributes. To broaden the scope of our study, we have experimentally assessed five widely used LDP protocols, namely, generalized randomized response, optimal local hashing, subset selection, RAPPOR and optimal unary encoding. In addition, we also propose a countermeasure solution that improves both utility and robustness against the threats we identify. Our contributions can help practitioners aiming to collect users' statistics privately to decide which LDP mechanism best fits their needs.

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

Python 3.8.8
Numpy 1.23.1
Pandas 1.2.4
Numba 0.53.1
Ray 1.11.0

## Contact
For any question, please contact [Héber H. Arcolezi](https://hharcolezi.github.io/): heber.hwang-arcolezi [at] inria.fr

## License
[MIT](https://github.com/hharcolezi/risks-ldp/blob/main/LICENSE)
