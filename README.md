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
