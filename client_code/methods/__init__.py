from ._anvil_designer import methodsTemplate
from anvil import *
import json
from anvil.js import import_from
StandardMerkleTree = import_from("@openzeppelin/merkle-tree").StandardMerkleTree
class methods(methodsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  def build_merkle(self, data, format, identifier, value):
    """
    Builds a Merkle tree from the provided data and format, and generates proofs for each data entry.
    
    Parameters:
    - data: The dataset to be used in the Merkle tree.
    - format: The format of the data. ["address", "uint256] if list of lists.
    - identifier: The field name to be used as an identifier for each entry.
    - value: The field name to be used as the value for each entry.
    
    Returns:
    A tuple containing the Merkle tree, its root, and the proofs for each entry.
    """
    # Create the Merkle tree
    tree = StandardMerkleTree.of(data, format)
    root = tree.root
    
    # Generate proofs for each entry in the dataset
    proofs = [{"proof": tree.getProof(data.index(r)), identifier: r[0], value: r[1]} for r in data]
    
    return tree, root, proofs