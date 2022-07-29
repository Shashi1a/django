### Prediction App
This Django app lets the user supply trained model and input data and identifies the phase(label) of the given data. 


#### Hamiltonian
This app is trained on the ordered and disordered spin configurations of a spin model described by the hamiltonian,
$$H = -J_{1}\sum_{\langle ij\rangle} S_{i}S_{j} - J_{2}\sum_{\langle \langle ij \rangle \rangle}S_{i}S_{i}$$
$S_{i} = \pm 1$ are the classical variables and take two values. 
These classical variables are interacting with each other. However in our calculation we ensure that
the site that are nearest neighbour (represened by $(\langle \rangle)$ in the hamiltonian) to each other are interacting via the $J_{1}$

##### Ferromagnet

![Two possible ferromagnetic configurations ](ferro.svg)

##### Anti-ferromagnet
![Ferromagnetic configurations](af.svg)

##### Stripe
![Ferromagnetic configurations](str.svg)

I have used a Convolutional Neural Network to peform task of the classification. The network is trained to differentiate between
ferromagnet, anti-ferromagnet, stripe ordered and disordered phase.


##### Demo video
The demo of the app can be found via this [Youtube](https://youtu.be/xj00o--9N2U) link.
