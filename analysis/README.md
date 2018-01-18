## Smart City "Traffic Control Unit" Simulation

For the simulation of my traffic planning application I would choose the approach of a discrete event simulation, because the overall system is mainly consisting out of management commands that are based upon an previous created schedule.
This is an optimized plan in which the needs of the citizens for mobility are realized, with simultaneous minimum expenditure of means of transport.

For this reason, I think that no continuous simulation is needed, because it is sufficient to calculate the individual processes step by step. 

In order to accomplish this task, the system has control over any traffic control elements and can associate the existing means of transport with the requests.

In the first phase, I would serve the simulation with a given list of corresponding requests, which will face a limited amount of resources. I would then try to determine, by minimizing the resources, from which amount a meaningful planning is no longer possible (optimal solution).

In the second phase, I would then generate the requests randomly and try to determine the optimal threshold for the needed resources by using multiple simulation runs.

In the third and final phase, I would increase the number of generated requests in order to be able to make statements regarding a relationship between the number of requests and the needed resources.
