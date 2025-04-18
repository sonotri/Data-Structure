class maxHeap():
    def __init__(self):
        self.data = list()

    def heappush(self, item):
        self.data.append(item)
        now_index = len(self.data)-1 
        while True:
            parent_index = (now_index-1) // 2
            if (parent_index < 0):
                break
            if (self.data[now_index] <= self.data[parent_index]):
                break
            else:
                self.data[now_index], self.data[parent_index] = self.data[parent_index], self.data[now_index]
                now_index = parent_index


    def heappop(self):
        now_index = len(self.data)-1
        self.data[0] = self.data[now_index]
        del self.data[now_index]
        now_index = 0
        while True:
            left_child_index = (now_index * 2 + 1)
            right_child_index = (now_index * 2 + 2)
            if (left_child_index >= len(self.data)):
                break
            
            if (right_child_index >= len(self.data)):
                if self.data[now_index] < self.data[left_child_index]:
                    self.data[now_index], self.data[left_child_index] = self.data[left_child_index], self.data[now_index]
                    break
                else:
                    break

            if (self.data[now_index] >= self.data[left_child_index]) and (self.data[now_index] >= self.data[right_child_index]):
                break
            else:
                if (self.data[left_child_index] > self.data[right_child_index]):
                    self.data[now_index], self.data[left_child_index] = self.data[left_child_index], self.data[now_index]
                    now_index = left_child_index
                else:
                    self.data[now_index], self.data[right_child_index] = self.data[right_child_index], self.data[now_index]
                    now_index = right_child_index



