from ._anvil_designer import methodsTemplate
from anvil import *
from anvil.js import import_from
StandardMerkleTree = import_from("@openzeppelin/merkle-tree").StandardMerkleTree
class methods(methodsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  def build_merkle(self, data, format):
    tree = StandardMerkleTree.of(data, format)
    root = tree.root
    proofs = [{"proof":tree.getProof(data.index(r)), "address":r[0], "merkle_value":r[1]} for r in data]
    return tree, root, proofs

    # Any code you write here will run before the form opens.
