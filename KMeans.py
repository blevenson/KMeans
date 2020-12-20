# Class to create a K-Means classifier
# @author Brett Levenson

import math
import random

class KMeans:
    
    # input: K, number of nodes
    def __init__(self, K, thresh = 0.01, iters=0):
        self.K = K
        self.nodes = []  # len = K
        self.threshold = thresh
        self.num_iterations = iters

    
    # data: array of arrays
    #       each row is a data point
    # output: Nothing, just trains internal model
    def fit(self, data):
        # init nodes to random vals
        num_dimensions = len(data[0])
        
        # init to random values
        for i in range(self.K):
            #self.nodes.append(data[i]) # grab first K items
            self.nodes = random.sample(data, self.K) # grab K random items

        # Iterate until threshold is met
        iteration = 0
        while True:
            nodes_sum = {}
            nodes_count = {}
            
            for elem in data:
                node_i = self.predict_index(elem)
                
                if node_i not in nodes_sum:
                    nodes_sum[node_i] = [0 for i in range(num_dimensions)]
                    nodes_count[node_i] = 0                    
 
                nodes_count[node_i] += 1
                for i in range(len(self.nodes[node_i])):
                    nodes_sum[node_i][i] += elem[i]

            # Update vals
            for node_i, sums in nodes_sum.items():
                for j in range(len(self.nodes[node_i])):
                    self.nodes[node_i][j] = sums[j] / nodes_count[node_i]
 

            if iteration > self.num_iterations:
            #if amount_change < self.threshold:
                print("Done training")
                return
            iteration += 1

    def predict(self, X):
        return self.nodes[self.predict_index(X)]

    def predict_index(self, X):
        min_dist = float('inf')
        closest_point = 0

        for node in range(len(self.nodes)):
            dist = self.compute_dist_squared(self.nodes[node], X)

            if dist < min_dist:
                min_dist = dist
                closest_point = node

        return closest_point

    def compute_dist(self, vec1, vec2):
        return math.sqrt(self.compute_dist_squared(vec1, vec2))

    def compute_dist_squared(self, vec1, vec2):
        assert(len(vec1) == len(vec2))

        dist = 0
        for i in range(len(vec1)):
            dist += (vec1[i] - vec2[i]) ** 2

        return dist

    def get_node_index(self, node):
        for i in range(self.K):
            if node == self.nodes[i]:
                return i

        assert(False)
        return -1
