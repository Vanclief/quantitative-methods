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

            if c_counter > 1:
                self.insert_next_client()
                c_counter = 0

            if s_counter > 4:
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


if __name__ == "__main__":

    n_clients = int(input("Enter the number of clients: >> "))

    b = Bank()

    for _ in range(0, n_clients):
        b.new_client()

    b.serve_clients()

    for i, client in enumerate(b.clients):
        print('Waiting time: ' + str(client.get_waiting_time()))
        print('System time: ' + str(client.get_serving_time()))
