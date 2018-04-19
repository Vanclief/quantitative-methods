import time
from datetime import datetime, timedelta


class Client:

    def __init__(self, number):
        self.number = number + 1
        self.entered_queue = None
        self.entered_system = None
        self.exited_system = None
        self.status = None
        print('New client ' + str(self.number) + ' entered the bank')

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

    def serve_next_client(self, t):

        i = 0
        c = self.clients[i]

        while c.status != 'waiting':
            c = self.clients[i]
            i += 1

        c.change_status('serving')
        time.sleep(t)
        c.change_status('served')


if __name__ == "__main__":

    b = Bank()
    b.new_client()
    b.new_client()
    b.serve_next_client(1)
    b.serve_next_client(1)

    for i, client in enumerate(b.clients):
        print(client.number)
        print('Waiting time: ' + str(client.get_waiting_time()))
        print('System time: ' + str(client.get_serving_time()))
