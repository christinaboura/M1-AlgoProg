#-*- coding: utf-8 -*-

class Node :
    def __init__(self, symbol, freq, left, right) :
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

def insert(nodes, node, k) : #nodes is sorted
    nodes += [node]
    while k > 0 and nodes[k-1].freq <= node.freq :
        nodes[k] = nodes[k-1]
        k -= 1;
    nodes[k] = node

def createTree(symbols,freqs) :
    nodes=[]
    for i in range(len(symbols)) :
        insert(nodes,Node(symbols[i],freqs[i],None,None),i)
        n = len(nodes)
    for i in range (n,1,-1) :
        left = nodes.pop()
        right = nodes.pop()
        insert(nodes,Node(None,left.freq+right.freq,left,right),i-2)
    return nodes.pop()

def traversal(node, code, codes) :
    if node.symbol != None :
        codes[node.symbol]=code
    if node.left != None :
        traversal(node.left, code+'1', codes)
    if node.right != None :
        traversal(node.right, code+'0', codes)
    
def createCode(node) :
    codes={}
    code=""
    traversal(node, code, codes)
    return codes

symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
freqs = [0.03, 0.12, 0.01, 0.06, 0.04, 0.04, 0.04, 0.01, 0.04, 0.06, 0.04, 0.03, 0.02, 0.02, 0.01, 0.10, 0.01, 0.06, 0.01, 0.03, 0.01, 0.03, 0.02, 0.03, 0.06, 0.07]
tree = createTree(symbols, freqs)
dico = createCode(tree)
print dico

def encoder(codes, phrase) :
    code = ''
    for char in phrase :
        if char != ' ' :
            code += dico[char]
    return code

code = encoder(dico, 'l algorithmique c est super top')
print code

def inverseDictionnaire(dico) :
    dicoInv = {}
    for cle in dico :
        dicoInv[dico[cle]] = cle
    return dicoInv

def decoder(codes, code) :
    codesInv = inverseDictionnaire(codes)
    phrase = ''
    i = 0
    tmp = ''
    while i < len(code) :
        while tmp not in codesInv :
            tmp += code[i]
            i += 1
        phrase += codesInv[tmp]
        tmp = ''
    return phrase

code = '0001100101011111011111010000000010110100001010000011001101110001011000000000011110\
1010101100000000011000001001111101111101001100000111100000110101110000001100100000000001011'

phrase = decoder(dico, code)
print phrase
