
#Fungsi Load File
def load() :
    #input nama file 
    file = input("Masukkan nama File Daftar Mata Kuliah : ")

    #membuka dan membaca file
    DataMataKuliah = open (file,"r")

    #menyimpan ke dalam array
    MatKul = [[num for num in line.split(',')] for line in DataMataKuliah]

    #menghapus elemen tidak penting
    MatKul = [[m.replace("\n","") for m in n] for n in MatKul]
    MatKul = [[m.replace(" ","") for m in n] for n in MatKul]
    MatKul = [[m.replace(".","") for m in n] for n in MatKul]

    return MatKul

#graph class
class Graph(object):

    def __init__(self, graph_dict=None):
        #inisiasi objek graf
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        #mengembalikan semua simpul
        return list(self.__graph_dict.keys())

    def edges(self):
        #mengembalikan semua busur
        return self.__generate_edges()

    def add_vertex(self, vertex):
        #nambah simpul
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        #nambah busur
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        #mencari dan mengembalikan nilai busur
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges



if __name__ == "__main__":
    #manggil fungsi load
    Matkul = load()
	
    #inisiasi graph
    graph = Graph()

    #membuat matkul sebagai simpul dari graf
    for line in Matkul :
        graph.add_vertex(line[0])
        i = 1
        while i < len(line) :
            graph.add_edge({line[0],line[i]})
            i+=1
    
    print("Vertices of graph:")
    print(graph.vertices())

    
    print("Edges of graph:")
    print(graph.edges())

