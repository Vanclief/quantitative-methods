import time
from datetime import datetime


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

        print('Client ' + str(self.number) + ' is now ' + status)

    def get_waiting_time(self):
        return self.entered_system - self.entered_queue

    def get_serving_time(self):
        return self.exited_system - self.entered_system


class Bank:

    def __init__(self):
        self.n_tellers = 2
        self.clients = []

    def new_client(self):
        client_number = len(self.clients)

        c = Client(client_number)
        c.change_status('waiting')

        self.clients.append(c)

    def serve_next_client(self):

        i = 0
        c = self.clients[i]

        while c.status != 'waiting' and i < len(self.clients):
            c = self.clients[i]
            i += 1

        c.change_status('serving')

    def serve_clients(self):

        last_client = self.clients[-1]

        while last_client.status != 'served':

            for _ in range(0, self.n_tellers):
                self.serve_next_client()

            time.sleep(1)

            for _, client in enumerate(self.clients):
                if client.status == 'serving':
                    client.change_status('served')

            last_client = self.clients[-1]


if __name__ == "__main__":

    n_clients = int(input("Enter the number of clients: >> "))

    b = Bank()

    for _ in range(0, n_clients):
        b.new_client()

    b.serve_clients()

    for i, client in enumerate(b.clients):
        print('Waiting time: ' + str(client.get_waiting_time()))
        print('System time: ' + str(client.get_serving_time()))
