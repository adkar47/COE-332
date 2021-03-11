Homework03

1.) git clone into repository
2.) cd into coe-322 then week05-http then into web to view the touch files
3.) Launch container using docker compose
4.) Build and run docker file using docker build and docker run
5.) Use 5014 port number to flask into the three different routes

First Route: /gen_Animals: will iterate through generate_animals from week one and will provide a random set of numbers from local variable num_of variables, if not it will provide 5 random animals.
Second Route: /animals will obtain animals from the data set and then remove them. Iterates through local variable num_of_animals
Third Route: /specify_animals acts as the /animals from the instructions, it will give a certain amount of animals from the data set and you can also specify its head type through local variable head.
