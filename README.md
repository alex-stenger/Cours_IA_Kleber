# Cours d'intelligence artificielle en 2ème année de classe préparatoire scientifique au Lycée Kléber à Strasbourg

## **FR :**

Ce dépot contient les slides ainsi que le code que j'ai utilisé lors de mes cours magistraux sur l'Intelligence Artificielle en 2ème année de CPGE scientifiques au Lycée Kléber à Strabourg.

### Concernant le code

Je m'étais fixé comme objectif de faire un cours le plus visuel et intuitif possible, sans pour autant rogner sur la rigueur. Vous trouverez pour cela dans le notebook ```main_notebook.ipynb``` un grand pannel de visualisations utilisant les bibliothèques interactives ```ipywidgets``` et ```plotly```. À noter que ces bibliothèques sont plutôt capricieuses, n'hésitez pas à changer de navigateur pour ouvrir le notebook, ou à le faire sur vscode...

le notebook ```illustration_non_convexite.ipynb``` essaye de donner aux élèves l'intuition de ce que peut-être un *loss landscape* comme on dit dans la communauté de l'Apprentissage.

Dans le dossier tmp, il y a du code en vrac si je puis dire, cela peut toujours être utile...

### Stucture et contenu résumé du cours

À travers ce cours, j'ai choisi une approche par l'analyse (contrairement aux approches probabilistes de Murphy que je cite plus bas, à l'approche algèbrique du Deep Learning book de Goodfellow, ou encore via la théorie de l'information). Elle me semblait la plus adaptée aux élèves de classes préparatoire.

Ce cours se construit autour d'un premier exemple de régression linéaire réalisée grâce à la descente de gradient. Cette première approche très simpliste permet aux étudiants de saisir le fonctionnement de la descente de gradient, ainsi que de revenir sur la notion fondamentale de convexité d'une fonction. Le tout dans un espace de petite dimension toujours dans le but de faciliter la compréhension.

La descente de gradient est ensuite généralisée à plus grande dimension, pour illuster la généricité de la méthode et son utilisation dans d'autres situations. 

Une fois cette notion bien comprise par les étudiants, le cours introduit les réseaux de neuronnes. Pour cela, j'ai décidé une approche plus mathématique et abstraite qui aborde points par points l'architectures des réseaux, la notion de propagation, de rétro-propagation et le fonctionnement spécifique de la descente de gradient pour les réseaux de neurones. Pour cela, je reprends en grande partie les démonstration de cette très précise et explicative réference : http://neuralnetworksanddeeplearning.com/chap2.html
Cette partie n'est pas vraiment sur les slides, j'avais décidé de faire les explications et démonstrations en direct avec les élèves.

Enfin, ce cours aborde également les notions élémentaires d'apprentissage que sont la phase d'entraînement, de test, les biais, le sur-apprentissage, le sous-apprentissage, les notions de supervisé et non supervisé ou encore la différence entre Classification et régression etc etc...

Les références sont indiquées tout au long des slides, on peut néanmoins nommé ce bouquin très utile, bien que l'approche soit complétement différente : Murphy, K. P. (2012). Machine learning: a probabilistic perspective. MIT press.


## **EN :**

# Repository for Artificial Intelligence Lectures in 2nd Year of Scientific Preparatory Classes at Lycée Kléber in Strasbourg

This repository contains the slides and code that I used during my lectures on Artificial Intelligence in the second year of scientific preparatory classes (equivalent to 2nd or 3rd year of scientific bachelor) at Lycée Kléber in Strasbourg.

### Code Details

My goal was to create a visually appealing and intuitive course without compromising on rigor. In the notebook `main_notebook.ipynb`, you will find a wide range of visualizations using interactive libraries such as `ipywidgets` and `plotly`. Please note that these libraries can be temperamental, so feel free to switch browsers to open the notebook or use it in vscode...

The notebook `illustration_non_convexite.ipynb` aims to provide students with an intuition of what a loss landscape can be, as referred to in the Machine Learning community.

In the `tmp` folder, you will find miscellaneous code that may still be useful...

### Course Structure and Summary Content

In this course, I chose an analytical approach (as opposed to probabilistic approaches like Murphy's, algebraic approaches like the Deep Learning book by Goodfellow, or information theory). It seemed more suitable for students in preparatory classes.

The course is built around an initial example of linear regression using gradient descent. This simplistic approach allows students to grasp the functioning of gradient descent and revisit the fundamental concept of function convexity. All of this takes place in a low-dimensional space to facilitate understanding.

Gradient descent is then generalized to higher dimensions to illustrate the method's versatility and its application in other situations.

Once students have a good understanding of this concept, the course introduces neural networks. For this purpose, I adopted a more mathematical and abstract approach, addressing the architecture of networks, the concept of forward propagation, backpropagation, and the specific functioning of gradient descent for neural networks step by step. For this part, I largely rely on the explanations and demonstrations provided in this precise and informative reference: [Neural Networks and Deep Learning by Michael Nielsen](http://neuralnetworksanddeeplearning.com/chap2.html). These explanations and demonstrations were mostly done live with the students and are not included in the slides.

Finally, the course also covers basic learning concepts such as training and testing phases, biases, overfitting, underfitting, supervised and unsupervised learning, classification and regression differences, and more.

Throughout the slides, the references are mentioned, but it is worth noting this highly useful book with a completely different approach: "Machine Learning: A Probabilistic Perspective" by Kevin P. Murphy (2012), published by MIT Press.
