# DS402_final_project
Implementation of Envy-free Matchings in Bipartite Graphs and their Applications to Fair Division with a back-end in Python and front-end in JavaScript.

## Installation

We have provided a `requirements.txt` file you can use to install the dependencies needed to work with our code. You can run it like so:

```bash
pip install --user -r requirements.txt
```

## Resources

This is the list of resources we consulted while developing our implementions of the algorithms, server, and front-end interface

### Algorithms

* https://www.youtube.com/watch?v=lM5eIpF0xjA
* https://www.youtube.com/watch?v=CSUEVu-qUgM
* https://www.youtube.com/watch?v=0GNYjXUPTFM

## Server

* https://github.com/NucciTheBoss/DS300_mini_project

## Testing

Here information on how to test the code in this repository

### Algorithms

We have some unit tests written. You can run them by using the following command:

```bash
python -m unittest test.py
```

### Server

You can talk to the server using the command line application `curl`. Here are the example commands that we used:


**Algorithm 1**
```bash
curl --header "Content-Type: application/json" \
  --request GET \
  --data '{"0": {"name": "A", "preferences": "X->Y->Z"},"1": {"name": "B", "preferences": "W->Y->Z"},"2": {"name": "C", "preferences": "Z->X->W"}}' \
  http://127.0.0.1:5000/algo1
```

**Algorithm 2**
```bash
curl --header "Content-Type: application/json" \
  --request GET \
  --data '{"0": {"name": "A", "preferences": "X->Y->Z"},"1": {"name": "B", "preferences": "W->Y->Z"},"2": {"name": "C", "preferences": "Z->X->W"}}' \
  http://127.0.0.1:5000/algo2
```
