# HuffmanEncoding
Compress and decompress a file using the Huffman encoding technique

Begin by initializing a new Huffman object by h = Huffman()

## Building the Tree

To build the tree call h.building_tree("your input")
"your input" must be a string.
A binary tree will then be built from the input string using the Huffman encoding technique

## Viewing the Tree

after building the tree it can be viewed by calling h.view_tree(h.get_data())

## Encoding

To encode a file and compress it call h.encode('file to encode', 'output file')
The 'file to encode' should be a document containing text.
The 'output file' should be a binary file. An example input would be 'output.bin'

## Decoding

To decode and decompress the file call h.decode('file to decode', 'output file')
The 'file to decode' should be a compressed binary file such as previously mentioned 'output.bin'
The output file should now be a text document an example being 'output.txt'
