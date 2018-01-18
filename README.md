# Assignment1 - Practice Designing Models

> * Participant name: Matthias Weber
> * Project Title: TCU - Traffic Control Unit (Get to your destination faster and cleaner)
## General Introduction

A **smart city** is an urban area that uses different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently.

![Image of Smart City](images/smartcity.png)

One of the biggest problems of nowadays large cities is the necessary mobility of its residents. As you can observe very well these days, the constant flow of traffic causes many problems. One of these problems is the resulting increased environmental pollution (aggravated by traffic jams) and its impact on the health of the people and animals living there.

The time that people are wasting, due to this traffic situation is also having a negative impact on their life quality.
That's why a smart city needs a highly efficient traffic control system to bring a large number of people to their desired destination quickly and with low emissions.

In my opinion, this can only succeed if the traffic control system can monitor any type of transportation and is able to manage the traffic control elements (e.g. traffic lights).
Thus, a constant distribution of all available resources can be achieved and the emerging traffic can be minimized.
Among other things, this system will have to be based on the existing model of car sharing, because with growing cities the available space will be more and more limited and for example there will not be enough space left, so that every citizen can have their own car-slot in front of his house/flat or in a parking garage next to his  work.
But instead of having an own car, the citizen of the future is having access to a large number of means of transportation, which will consists out of available buses, cars, subways or bicycles.

A centralized schedule (control unit) ensures that everyone comes to the place they want to be, without wasting unnecessary resources (such as time) or making compromises (e.g. available space).

![Mobility in future](images/traffic_controled_city.png)
copyright: Bosch, Siemens

## Requirements (Experimental Design)

For better clarity of the planning process, imagine the following everyday situation:

A citizen has to get to work at 9 a.m., leaving the work at 5 p.m., picking up his 2 kids from the lacrosse training at 6 p.m. and must get back home (including the lacrosse-equipment).
The evening before, each appointment has to be registered in the digital calendar, so that the central traffic control unit can create a preliminary plan based on the submitted plans of all citizens.
When the person is waking up, he would receive an message, that it currently would be faster to take the rental-bike to the subway station (the weather is also good and the health app recommends a little bit of exercise ;) ) to reach his workplace on time. Everything worked like it was planned.
When he is leaving the work at 5:15 p.m. the central unit has to reschedule the plan and offers a bus ride to the school. During these rush hours, the traffic lights are switched by the control unit in the way so that traffic can flow optimally. Our person is arriving at the school at 5:55 p.m. and a reserved car (that is big enough for 3 persons and the equipment) is waiting next to the school, so that they can get easily back home.

To ensure that this scenario can take place and is working as it should, the following requirements are needed:

1. Every involved component must have permanent access to the central database (to receive the current information) as well as allowed access by the planning unit.

2. This components are mainly traffic lights, road signs, cars, buses, subways, bikes, sensors to monitor pedestrians

3. The citizen has to notify the central routing planning application about all planned and wanted appointments that are requiring transportation. 

4. This message must include the following information: place of departure, destination, time of arrival, number of persons to be carried, working space required, need for additional storage space, limitations

5. The notification of this transportation requirement can be made via personal computer, by app or by calling a call center.

6. The central planning unit is responsible for the creation of an optimized schedule that is fulfilling all requests.

7. This schedule includes a balanced load of all available means of transport, while ensuring that all the individual requirements of the applicants are met.

8. In the case of a necessary prioritization of submitted requests, the oldest request is going to be prioritized.

By using this creating and using this simulation it should be possible to identify the minimum amount of transport needed to meet the mobility needs of all the citizens of a city.
This will result in a reduced pollution of the environment and an increased level of satisfaction of all citizens

## Smart City "Traffic Control Unit" Model

In this section I'm going to illustrate my previous described system by presenting different diagrams.

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides a detailed view of the used components 
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of the way how the main-componets are ineracting

## Smart City "Traffic Control Unit" Simulation

My described model of a ["Traffic Control Unit"](model/README.md) is mainly a communication and management application. But his great power lies in the function "createSchedule ()", which is responsible for the creation of an optimized transportation plan upon all submitted user-requests.


## Smart City "Traffic Control Unit" Model
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)

## **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template.
