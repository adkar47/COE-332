ADJUSTMENTS

read_animals.py now can precisely distinguish the number of animals using the parameter num_of_animals
read_animals.py also checks for different errors now when trying to return a number from the list
Prints a number based on animals.json
generate_animals.py will provide 20 random animals into animals.json from the previous homework


RUN DIRECTLY

1.) Use git clone https:github.com/adkar47/COE-332.git
2.) Then you can run locally on whatever text editor within the required libraries (emacs,vim)


RUN THROUGH DOCKER

1.) Launch a container through: docker run --rm -it -v $PWD:/code centos:7.7.1908 /bin/bash

2.) Use docker build through the homeowork2 directory: docker build -t {username}/json_parser:1.0 .
3.) Make sure to use the yum update and the yum install python 3
4.) Avoidd the petname unicode error 
    export LC_CTYPE=en_US.UTF-8
    export LANG=en_US.UTF-8
    pip3 install petname
5.) run: generate_animals.py animals.json
6.) run  read_animals.py animals.json

UNIT TESTING

1.) emacs or vim test_read_animals.py
2.) All tests should pass
