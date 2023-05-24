class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    # def __str__(self):
    #     return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def remove_neighbor(self, neighbor):
        self.adjacent.pop(neighbor)

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def remove_edge(self, frm, to):
        k = False

        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        for w in self.vert_dict[frm].get_connections():
            if(w == self.vert_dict[to]):
                k = True
        if(k):     
            self.vert_dict[frm].remove_neighbor(self.vert_dict[to])
            self.vert_dict[to].remove_neighbor(self.vert_dict[frm])
   
    def get_vertices(self):
        return self.vert_dict.keys()
    
    def remove_all_edges(self):
        for v in self.get_vertices():
            for w in self.get_vertices():
                self.remove_edge(v, w)
                
    
    def find_all_paths(self, frm, to, path = []):
        path = path + [frm]
        if frm == to:
            return [path]
        paths = []
        newpaths = []
        for node in self.vert_dict[frm].get_connections():
            node = node.get_id()
            if node not in path:
                newpaths = self.find_all_paths(node, to, path)
            for newpath in newpaths:
                paths.append(newpath)
        return paths
    
    def fastest_path(self, frm, to):
        paths = self.find_all_paths(frm, to)
        index_min = 1000
        for path in paths:
            index = 0
            for idx, id in enumerate(path):
                if(idx+1 > len(path) - 1):
                    break
                else:
                    index = index + self.vert_dict[id].get_weight(self.vert_dict[path[idx+1]])
            if(index < index_min):
                index_min = index
        return index_min
    
    def index_per(self):
        index1 = 0
        index2 = 0
        for i in self.vert_dict.keys():
            for j in self.vert_dict[i].get_connections():
                for k in self.vert_dict.keys():
                    index1 = index1 + self.fastest_path(j.get_id(),self.vert_dict[k].get_id())

                for k in self.vert_dict.keys():
                    index2 = index2 + self.fastest_path(self.vert_dict[i].get_id(),self.vert_dict[k].get_id())
        if(index1 + index2 > 0):
            index = 1000/(index1 * (index1 + index2) / index2)
        else:
            index = 10000
            
        return index
    
    def gen_to_graph(self, str):

        self.remove_all_edges()

        if(str[0] == 1):
            self.add_edge('1', '2', 100)  
        if(str[1] == 1):
            self.add_edge('1', '3', 140)  
        if(str[2] == 1):
            self.add_edge('1', '4', 100)  
        if(str[3] == 1):
            self.add_edge('1', '5', 152)  
        if(str[4] == 1):
            self.add_edge('2', '3', 100)  
        if(str[5] == 1):
            self.add_edge('2', '4', 140)  
        if(str[6] == 1):
            self.add_edge('2', '5', 168)  
        if(str[7] == 1):
            self.add_edge('3', '4', 100)  
        if(str[8] == 1):
            self.add_edge('3', '5', 90)  
        if(str[9] == 1):
            self.add_edge('4', '5', 56)  
        

    


if __name__ == '__main__':

    g = Graph()

    g.add_vertex('1')
    g.add_vertex('2')
    g.add_vertex('3')
    g.add_vertex('4')
    g.add_vertex('5')

    # g.add_edge('a', 'b', 7)  
    # g.add_edge('b', 'c', 9)
    # g.add_edge('c', 'd', 14)
    # g.add_edge('d', 'e', 10)
    # g.add_edge('e', 'a', 15)

    g.gen_to_graph([1,1,1,1,1,1,1,1,1,1])
    g.gen_to_graph([1,1,0,0,0,0,0,0,0,0])

    # print('dsa')
    # print(find_all_paths(g, 'a', 'e').forward())

    # for v in g:
        
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    # print(g.index_per())

    # for v in g:
    #     print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))