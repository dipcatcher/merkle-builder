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
    '''pass data and format, name of fields'''
    tree = StandardMerkleTree.of(data, format)
    root = tree.root
    #proofs = [{"proof":json.dumps(tree.getProof(data.index(r))), identifier:r[0], value:r[1]} for r in data]
    proofs = [{"proof":tree.getProof(data.index(r)), identifier:r[0], value:r[1]} for r in data]
    return tree, root, proofs

    # Any code you write here will run before the form opens.
