# GHEvolution
![Generations GIF](/generations.gif)

This project was made for my final math research project at GHP 59 where we were tasked to make a project and presentation on something we found interesting in math or computer science. Heavily inspired by [this video](https://youtu.be/N3tRFayqVtk), I decided to make a neuroevolution simulation that would task little square "organisms" to travel to a safe zone in a square area. Those who made it would survive and pass their brain "genes" to the next generation. Over time, the best organisms continually replicate, with the occasional mutation to respond to changes in the environment. It does a pretty good job at basic natural selection and is a gateway into the world of generational evolutionary algorithms. 

I also implemented this same idea in Roblox, and I also have [a video on that](https://youtu.be/uzusbTeSKD4). 

## Quickstart
This project uses python and the [poetry](https://python-poetry.org/) package manager. To start, clone the repo and run
```
poetry install
```
That should get all of the dependencies. Use this command to run:
```
poetry run python ghevolution
```
This will display the pygame window with the generations. There was also a visualizer of the brains and survivor graphs, but I can't get that to work 2 years later and I can't be bothered to fix it, but if you want to see what those looked like, there are still some in the repo:
![brain_graph.png]
Here is the brain, a graph with different weights that is randomly generated at the beginning and evolves over time
![survivor_graph.png]
This graph shows that over time more organisms surive. At first, those who live are random, but over time all of the organisms get the best geners

For a more theoretical overview, you can watch [this video](https://youtu.be/N3tRFayqVtk). It is one of my favorite videos on YouTube, please do yourself a favor and watch it!
