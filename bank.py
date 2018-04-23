import os
import time
import math
import random
from datetime import datetime


def isWaiting(client):
    if client.status == 'waiting':
        return True
    else:
        return False


class Counter:

    def __init__(self, number):
        self.number = number + 1
        self.status = 'free'

    def serve_client(self, client):
        self.status = 'busy'
        print('Counter ' + str(self.number) + ' serving client ' +
              str(client.number))

    def free(self):
        self.status = 'free'
        print('Counter ' + str(self.number) + ' is now free')


class Client:

    def __init__(self, number):
        self.number = number + 1
        self.entered_queue = None
        self.entered_system = None
        self.exited_system = None
        self.status = None

    def change_status(self, status):
        self.status = status
        time = datetime.now().timestamp()

        if status == 'waiting':
            self.entered_queue = time
        elif status == 'serving':
            self.entered_system = time
        elif status == 'served':
            self.exited_system = time

        # print('Client ' + str(self.number) + ' is now ' + status)

    def get_waiting_time(self):
        return self.entered_system - self.entered_queue

    def get_serving_time(self):
        return self.exited_system - self.entered_system


class Bank:

    def __init__(self, lamda, mu):
        self.n_tellers = 2
        self.clients = []
        self.lamda = lamda  # typo on porpuse
        self.mu = mu

    def get_arrival_time(self):
        x = -1 * self.lamda * math.log(random.uniform(0, 1))
        return x

    def get_serving_time(self):
        x = -1 * self.mu * math.log(random.uniform(0, 1))
        return x

    def new_client(self):
        client_number = len(self.clients)

        c = Client(client_number)

        self.clients.append(c)

    def insert_next_client(self):

        i = 0
        c = self.clients[i]

        while c.status and i < len(self.clients) - 1:
            i += 1
            c = self.clients[i]

        if not c.status:
            self.clients[i].change_status('waiting')

    def serve_next_client(self):

        i = 0
        c = self.clients[i]

        while c.status != 'waiting' and i < len(self.clients) - 1:
            i += 1
            c = self.clients[i]

        if c.status == 'waiting':
            self.clients[i].change_status('serving')

    def serve_clients(self):

        last_client = self.clients[-1]

        c_counter = 0
        s_counter = 0

        while last_client.status != 'served':

            queue = list(filter(isWaiting, self.clients))

            if c_counter > self.get_arrival_time():
                self.insert_next_client()
                c_counter = 0

            if s_counter > self.get_serving_time():
                for _ in range(0, self.n_tellers):
                    self.serve_next_client()
                s_counter = 0

            time.sleep(0.25)
            c_counter += 1
            s_counter += 1

            for _, client in enumerate(self.clients):
                if client.status == 'serving':
                    client.change_status('served')

            last_client = self.clients[-1]
            os.system('clear')
            print('Clients in queue: ' + str(len(queue)))




if __name__ == "__main__":

    n_clients = int(input("Enter the number of clients: >> "))
    lamda = float(input("Enter lambda: >> "))
    mu = float(input("Enter mu: >> "))

    b = Bank(lamda, mu)

    for _ in range(0, n_clients):
        b.new_client()

    b.serve_clients()

    for i, client in enumerate(b.clients):
        print('Waiting time: ' + str(client.get_waiting_time()))
        print('System time: ' + str(client.get_serving_time()))
