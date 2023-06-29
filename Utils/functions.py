def row_to_attribute_dict(key_list, value_list):
    dict={}
    for (key, value) in zip(key_list, value_list):
        #print(key, ": ", value)
        dict[key] = value
    return dict


def convert_df_to_bipartite_graph_with_attributes(df, attr_indices, labels):
  """
  df: DataFrame
  attr_indices: a list of two integers.
                ex: [0,9]
                The first integer element represents the starting index of the attributes in the given df.
                The second integer element represents the ending index of the attributes in the given df.
  labels : a list of three string.
                ex: ["Users", "Products", "Buy"]
                The first string element represents the name of the first set of the bipartite graph.
                The second string element represents the name of the second set of the bipartite graph.
                The third string element represents the name of the edges(relation) between the two sets of the bipartite graph.
  """   
    start_idx = attr_indices[0]
    end_idx = attr_indices[1]
    set1_label = labels[0]
    set2_label = labels[1]
    edge_label = labels[2]

    B = nx.Graph()
    
    for i in df.index:
        attributes = df.loc[i][start_idx:end_idx+1]  # range of df columns that are used as node attributes 
        att_names = attributes.index.to_list()
        att_values = attributes.values
        att_dict = row_to_attribute_dict(att_names, att_values)
        att_dict["bipartite"] = 0
        attrs = {}
        attrs[i] = att_dict
        #B.add_node(i, bipartite = 0)          # Add node to the first set of the bipartite graph
        #B.add_node(i)
        B.add_node(i, label=set1_label)
        nx.set_node_attributes(B, attrs)       # Add node attributes
      
        for j in df.columns[end_idx+1:]:  
            #B.add_node(j, bipartite= 1)       # Add node to the second set of the bipartite graph
            B.add_node(j, bipartite=1, label=set2_label)  
            if (df.loc[i, j] > 0):
                #B.add_edge(i, j, weight=df.loc[i, j])
                B.add_edge(i, j, weight=df.loc[i, j], label=edge_label)
    return B



def NodeAttributesByIndex(graph, node_idx, attr_names):
"""
graph: Networkx graph object
node_idx: index number of a given node
attr_namaes: list of attributes names(string type) you want to retrieve
"""
  current_node = list(graph.nodes(data=True))[node_idx]
  node_name = current_node[0]
  node_attributes = current_node[1]

attr_values = []
dict = {}

for i in range(len(attr_names)):
  dict[attr_names[i]] = node_attributes[attr_names[i]]
  attr_values.append(dict[attr_names[i]])

return (node_name, attr_values)


def NodeAttributes(graph, node_name):
    """
    Returns all attributes belonging to a node specified by the node_name
    """
    attrs = graph.nodes.data()[node_name]
    return attrs
