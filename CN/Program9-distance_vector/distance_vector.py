class Routing_table:
    def _init_(self, current):
        self.current = current
        self.table = {'Dest':[current], 'Cost':[0], 'NextH':[current]}
        self.neig = []

    def add_direct_connection(self, p, cost):
        self.table['Dest'].append(p)
        self.table['Cost'].append(cost)
        self.table['NextH'].append(p)
        self.neig.append(p)


    def recieve_msg(self, dest, cost, sender):
        flag = 0
        index_of_sender = self.table['Dest'].index(sender)
        cost_to_sender = self.table['Cost'][index_of_sender]
        for d, c in zip(dest, cost):
            if d not in self.table['Dest']:
                self.table['Dest'].append(d)
                self.table['Cost'].append(cost_to_sender + c)
                self.table['NextH'].append(sender)
                flag = 1
            
            elif cost_to_sender + c < self.table['Cost'][self.table['Dest'].index(d)]:
                self.table['Cost'][self.table['Dest'].index(d)] = cost_to_sender + c
                self.table['NextH'][self.table['Dest'].index(d)] = sender
                flag = 1

        if flag == 1:
            return self.neig, [self.table['Dest'], self.table['Cost'], self.current] 
        
        return [], []

    def print_routing_table(self):
        for x, val in self.table.items():
            print(x, val)
            

class Topology:
    def _init_(self, array_of_points):
        self.tables = {}
        for p in array_of_points:
            self.tables[p] = Routing_table(p)
    
    def add_direct_connection(self, p1, p2, cost):
        self.tables[p1].add_direct_connection(p2, cost)
        self.tables[p2].add_direct_connection(p1, cost)
    
    def send_msges(self, recipients, msg):
        if recipients == []:
            return []
        for p in recipients:
            self.send_msges(*self.tables[p].recieve_msg(*msg)) # Each individual routing table recives msges

    def print_routing_tables(self):
        for x, val in self.tables.items():
            print(x) #prints point
            val.print_routing_table() #prints individual routing table
            print('--------------------------------')
    
    def start(self, p1, p2):
        print('Initial configuration of all routing tables after direct connections')
        self.print_routing_tables()
        print('***************')

        p2_dest = self.tables[p2].table['Dest']
        p2_cost = self.tables[p2].table['Cost']
        self.send_msges(p1, [p2_dest, p2_cost, p2])

        print('***************')

        print('Everything has been Efficiently routed!!!!')
        print()
        print('Final configuration of every routing table')
        self.print_routing_tables()

            


# Create the Topology
# Number of points
array = ['A', 'B', 'C', 'D', 'E']

# Create the network
t = Topology(array)

# Direct connection of each point in the Topology
t.add_direct_connection('A', 'B', 1)
t.add_direct_connection('A', 'C', 5)
t.add_direct_connection('B', 'C', 3)
t.add_direct_connection('B', 'E', 9)
t.add_direct_connection('C', 'D', 4)
t.add_direct_connection('D', 'E', 2)


# Start the self correcting routing algorithm
# You can choose any two points
t.start('A', 'B')
