def row_to_attribute_dict(key_list, value_list):
    dict={}
    for (key, value) in zip(key_list, value_list):
        #print(key, ": ", value)
        dict[key] = value
    return dict


def convert_df_to_bipartite_graph_with_attributes(df_feats, df_labels, attr_indices, labels):
  """
  Returns a bipartite graph generated from the given two dataframes.
  
  One group of nodes will be created based on the index of df_feats, 
  and the other gorup of nodes will be created based on the columns of df_labels.
  
      1. df_feats : feature dataframe  
      2. df_labels: labels dataframe  
      3. attr_indices: a list of two integers.
                    ex: [0,9]
                    The first integer element represents the starting index of the attributes in the given df.
                    The second integer element represents the ending index of the attributes in the given df.
      4. labels : a list of three string.
                    ex: ["Users", "Products", "Buy"]
                    The first string element represents the name of the first set of the bipartite graph.
                    The second string element represents the name of the second set of the bipartite graph.
                    The third string element represents the name of the edges(relation) between the two sets of the bipartite graph.
  """   
    set1_name = structure[0]; set2_name = structure[1]; edge_name = structure[2]
    attr_start_idx = attr_indices[0]; attr_end_idx = attr_indices[1]

    B = nx.Graph()

    # nodes creation from df_labels (bipartite group 1) 
    for species in df_labels.columns[:]:
        B.add_node(species, bipartite = 1, label=set2_name)
        # nx.set_node_attributes() 

    for sample_id in df_feats.index:  # i: Sample_ID
        attributes = df_feats.loc[sample_id][attr_start_idx: attr_end_idx + 1]  #  Return pd.Series 
        attr_names = attributes.index.to_list() 
        attr_values = attributes.values         # Return np.array 1D
        
        #####################################################################
        # a nested dictionary object is required for nx.set_node_attributes() 
        name_value_dict = {}
        for (key, value) in zip(attr_names, attr_values):
            name_value_dict[key] = value    
        
        attrs_dict = {}
        attrs_dict[sample_id] = name_value_dict 
        #####################################################################
       
        # nodes creation from df_feats (bipartite group 0) 
        B.add_node(sample_id, bipartite = 0,   label=set1_name)        
        nx.set_node_attributes(B, attrs_dict) 

        # edge 생성
        for species in df_labels.columns[:]:
            cell_count = df_labels.loc[sample_id][species] 
            if (cell_count > 0):
                B.add_edge(sample_id, species, weight=cell_count, label=edge_name)

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

        node_name: Name of a node
    """
    attrs = graph.nodes.data()[node_name]
    return attrs
