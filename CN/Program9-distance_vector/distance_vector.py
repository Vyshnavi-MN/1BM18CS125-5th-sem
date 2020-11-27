# Individual routing tables
class Routing_table:
    def _init_(self, current):
        # Current point(router)
        self.current = current

        # Routing table
        ### Format:-
        ### Dest   Cost   NextHopPoint
        ###  C       0         C
        
        self.table = {'Dest':[current], 'Cost':[0], 'NextH':[current]}

        # Neighbours array to store directly connected points
        self.neig = []
        
                    
        
    
    def add_direct_connection(self, p, cost):
        # Connects given point to this router directly
        self.table['Dest'].append(p)
        self.table['Cost'].append(cost)
        self.table['NextH'].append(p)

        # Add point to neighbour table as it is directly connected
        self.neig.append(p)


    def recieve_msg(self, dest, cost, sender):
        # If any changes have been made based in recieved sender information
        # These changes must be sent to all neighbours even the sender
        flag = 0
        
        # TO find index in the table which corresponds to sender values
        index_of_sender = self.table['Dest'].index(sender)
        cost_to_sender = self.table['Cost'][index_of_sender]
        for d, c in zip(dest, cost):

            # If destination not in this routing table
            if d not in self.table['Dest']:
                self.table['Dest'].append(d)
                self.table['Cost'].append(cost_to_sender + c)
                self.table['NextH'].append(sender)
                flag = 1
            
            # If estimated cost to destination is less through sender
            elif cost_to_sender + c < self.table['Cost'][self.table['Dest'].index(d)]:
                self.table['Cost'][self.table['Dest'].index(d)] = cost_to_sender + c
                self.table['NextH'][self.table['Dest'].index(d)] = sender
                flag = 1


        ### Uncomment these lines to see the ripples as the spread across the network until
        ### all the network has self optimised itself to have the fastest route to all points in
        ### the network

        # print('Correcting', self.current, 'from info sent by', sender)
        # self.print_routing_table()
        # print('Flag:', flag)
        # print('---------------------------')



        # If Changes are made they need to be sent to all Neighbours even the sender
        if flag == 1:
            # Neighbours of the msg, The msg(dest, cost, current sender) containing new changed values
            return self.neig, [self.table['Dest'], self.table['Cost'], self.current] 
        
        # If nothing was changed send empty msges
        return [], []
        
    

    # Function to print Current routing table
    def print_routing_table(self):
        for x, val in self.table.items():
            print(x, val)
            

# Network Topology
class Topology:
    def _init_(self, array_of_points):
        # Create Routing tables for each point(router) and store in the dictionary
        self.tables = {}
        for p in array_of_points:
            self.tables[p] = Routing_table(p)
    
    def add_direct_connection(self, p1, p2, cost):
        ## We need to add to both routing tables as they are connected to each other

        # Add direct connection to routing table p1
        self.tables[p1].add_direct_connection(p2, cost)

        # Add direct connection to routing table p2
        self.tables[p2].add_direct_connection(p1, cost)
    
    def send_msges(self, recipients, msg):
        # Uses recursion to accept msges from individual routing tables and sends to points to 
        # change(if possible) neighbouring routing tables

        # Base case
        # If no recipients of any msges meaning "that ripple has died down"
        # then no msges will be sent anymore
        if recipients == []:
            return []
        
        # For all recipients(neighbours) of the current "ripple" send msges 

        for p in recipients:
            self.send_msges(*self.tables[p].recieve_msg(*msg)) # Each individual routing table recives msges

        
        

    
    def print_routing_tables(self):
        # Print all routing tables for each point in the Network
        for x, val in self.tables.items():
            print(x) #prints point
            val.print_routing_table() #prints individual routing table
            print('--------------------------------')
    
    def start(self, p1, p2):
        # Routing tables before the first msg is sent
        print('Initial configuration of all routing tables after direct connections')
        self.print_routing_tables()
        print('***************')

        # Send the first msg to start of the self correcting process
        # From point 2 to point 1
        p2_dest = self.tables[p2].table['Dest']
        p2_cost = self.tables[p2].table['Cost']
        self.send_msges(p1, [p2_dest, p2_cost, p2])

        print('***************')

        # After the "water has settled", final configuration of the routing tables
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
