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


def isServed(client):
    if client.status == 'served':
        return True
    else:
        return False


def isFree(counter):
    if counter.status == 'free':
        return True
    else:
        return False


class Counter:

    def __init__(self, number, mu):
        self.number = number + 1
        self.mu = mu
        self.status = 'free'
        self.serving_time = self.get_serving_time()
        self.cooldown = 0

    def serve_client(self, client):
        self.status = 'busy'
        print('Counter ' + str(self.number) + ' serving client ' +
              str(client.number))
        client.change_status('serving')
        client.set_service_time(mu)

    def free(self):
        self.status = 'free'
        self.cooldown = 0
        self.serving_time = self.get_serving_time()
        print('Counter ' + str(self.number) + ' is now free')

    def get_serving_time(self):
        x = -1 * self.mu * math.log(random.uniform(0, 1))
        return x


class Client:

    def __init__(self, number):
        self.number = number + 1
        self.entered_queue = None
        self.entered_system = None
        self.exited_system = None
        self.status = None
        self.x = None
        self.mu = None

    def change_status(self, status):
        self.status = status
        time = datetime.now().timestamp()

        if status == 'waiting':
            self.entered_queue = time
            print('Client ' + str(self.number) + ' has entered the bank')
        elif status == 'serving':
            self.entered_system = time
        elif status == 'served':
            self.exited_system = time
            print('Client ' + str(self.number) + ' has exited the bank')

    def set_arrival_time(self, x):
        self.x = x

    def set_service_time(self, mu):
        self.mu = mu

    def get_waiting_time(self):
        return self.entered_system - self.entered_queue

    def get_serving_time(self):
        return self.exited_system - self.entered_system


class Bank:

    def __init__(self, lamda, mu):
        self.clients = []
        self.counters = []
        self.lamda = lamda  # typo on porpuse
        self.mu = mu

    def get_arrival_time(self):
        x = -1 * self.lamda * math.log(random.uniform(0, 1))
        return x

    def new_client(self):
        client_number = len(self.clients)

        c = Client(client_number)

        self.clients.append(c)

    def new_counter(self):
        counter_number = len(self.counters)

        c = Counter(counter_number, mu)

        self.counters.append(c)

    def insert_next_client(self, x):

        i = 0
        c = self.clients[i]

        while c.status and i < len(self.clients) - 1:
            i += 1
            c = self.clients[i]

        if not c.status:
            self.clients[i].change_status('waiting')
            self.clients[i].set_arrival_time(x)

    def serve_next_client(self, counter):

        i = 0
        c = self.clients[i]

        while c.status != 'waiting' and i < len(self.clients) - 1:
            i += 1
            c = self.clients[i]

        if c.status == 'waiting':
            counter.serve_client(self.clients[i])

    def serve_clients(self):

        last_client = self.clients[-1]

        wait_time = 0

        arrival_time = self.get_arrival_time()

        time_elapsed = 0

        while last_client.status != 'served':

            waiting_clients = list(filter(isWaiting, self.clients))
            served_clients = list(filter(isServed, self.clients))
            free_counters = list(filter(isFree, self.counters))

            # Inser a new client every time the client counter equals the
            # arribal time
            if wait_time > arrival_time:
                self.insert_next_client(arrival_time)
                arrival_time = self.get_arrival_time()
                wait_time = 0

            for i, counter in enumerate(self.counters):

                if counter.status == 'free':
                    self.serve_next_client(counter)

                elif counter.cooldown > counter.serving_time:
                    counter.free()
                else:
                    counter.cooldown += 1

            time.sleep(0.1)
            wait_time += 1
            time_elapsed += 1

            for _, client in enumerate(self.clients):
                if client.status == 'serving':
                    client.change_status('served')

            last_client = self.clients[-1]
            os.system('clear')
            print('Time: ' + str(time_elapsed))
            print('Clients waiting: ' + str(len(waiting_clients)))
            print('Clients served: ' + str(len(served_clients)))
            print('Number of counters: ' + str(len(self.counters)))
            print('Free counters: ' + str(len(free_counters)))
            print('-- Events --')


if __name__ == "__main__":

    n_clients = int(input("Enter the number of clients: >> "))
    n_counters = int(input("Enter the number of servers: >> "))
    lamda = float(input("Enter aproximated arrival time: >> "))
    mu = float(input("Enter aproximated service time: >> "))

    b = Bank(lamda, mu)

    for _ in range(0, n_clients):
        b.new_client()

    for _ in range(0, n_counters):
        b.new_counter()

    b.serve_clients()

    wq = 0
    ws = 0
    l = 0
    mu = 0

    for i, client in enumerate(b.clients):

        wt = client.get_waiting_time()
        st = client.get_serving_time()
        x = client.x
        u = client.mu

        wq += wt
        ws += (wt + st)
        l += x
        mu += u

    wq = wq / len(b.clients)
    ws = ws / len(b.clients)
    x = x / len(b.clients)
    final_lambda = 60 / x
    final_mu = 60 / u

    print('WQ: ' + str(wq))
    print('WS: ' + str(ws))
    print('Lambda ' + str(final_lambda))
    print('Mu ' + str(final_mu))


